#!/usr/bin/env python3
"""Applique les corrections SEO (balises, maillage, redirections). Idempotent."""
import re, glob, html, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
H = html.escape
def rd(f): return open(f, encoding='utf8').read()
def wr(f, s): open(f, 'w', encoding='utf8').write(s)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_config import *

def set_meta(slug, s, new_t, new_d):
    old_t = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())
    m = re.search(r'<meta name="description" content="(.*?)"', s)
    old_d = html.unescape(m.group(1)) if m else None
    if new_t:
        for pat in (old_t, H(old_t), H(old_t, quote=False)):
            s = s.replace(pat, H(new_t, quote=False)) if False else s
        s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % H(new_t, quote=False), s, count=1, flags=re.S)
        s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + H(new_t), s)
        s = re.sub(r'(<meta name="twitter:title" content=")[^"]*', lambda m: m.group(1) + H(new_t), s)
    if new_d:
        s = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + H(new_d), s, count=1)
        s = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + H(new_d), s)
        s = re.sub(r'(<meta name="twitter:description" content=")[^"]*', lambda m: m.group(1) + H(new_d), s)
        if old_d:
            s = s.replace('"description": "%s"' % old_d.replace('"', '\\"'), '"description": "%s"' % new_d.replace('"', '\\"'))
    return s

# ---------- 2. Maillage ----------
def h1_of(slug):
    return re.search(r'<h1>(.*?)</h1>', rd(slug + '.html'), re.S).group(1).strip()

def article_body_span(s):
    a = s.index('<article>'); b = s.index('<section class="related"')
    return a, b

def own_links(seg):
    return set(l.strip('/') for l in re.findall(r'href="(/[^"#?]*)"', seg))

def add_inline(slug, s, report):
    a, b = article_body_span(s)
    body = s[a:b]
    have = [t for t in own_links(body) if t in ARTICLES and t != slug]
    want = [t for t in INLINE[slug] if t != slug]
    need = [t for t in want if t not in have]
    n_have = len(have)
    for t in need:
        if n_have >= 3: break
        rx = re.compile(PHRASES[t], re.I)
        done = False
        # paragraphes <p>, hors .disclaimer/.cta-box/.nl-inline/.sig-type
        for pm in re.finditer(r'<(p|li)(?: [^>]*)?>(.*?)</\1>', body, re.S):
            pre = body[:pm.start()]
            if (pre.count('<div') != pre.count('</div>')): continue
            inner = pm.group(2)
            parts = re.split(r'(<a\b.*?</a>|<[^>]+>)', inner, flags=re.S)
            inlink = False
            for i, p in enumerate(parts):
                if p.startswith('<a'): continue
                if p.startswith('<'): continue
                m = rx.search(p)
                if m:
                    parts[i] = p[:m.start()] + '<a href="/%s">%s</a>' % (t, m.group(0)) + p[m.end():]
                    new_inner = ''.join(parts)
                    body = body[:pm.start(2)] + new_inner + body[pm.end(2):]
                    done = True; report.append((slug, t, 'ancre: ' + m.group(0))); break
            if done: break
        if not done:
            # repli : phrase courte en fin de 2e paragraphe d'article
            ps = [pm for pm in re.finditer(r'<(p)(?: [^>]*)?>(.*?)</\1>', body, re.S)
                  if body[:pm.start()].count('<div') == body[:pm.start()].count('</div>')]
            pm = ps[min(1 + n_have, len(ps) - 1)]
            tpl = ('Pour approfondir, lisez notre article sur', 'Sur ce point, voir aussi notre article sur', 'À ce sujet, consultez notre article sur')[sum(map(ord, slug + t)) % 3]
            ins = ' %s <a href="/%s">%s</a>.' % (tpl, t, H(SHORT[t], quote=False))
            body = body[:pm.end(2)] + ins + body[pm.end(2):]
            report.append((slug, t, 'REPLI phrase'))
        n_have += 1
    return s[:a] + body + s[b:]

def related_block(slug):
    lis = ''.join('<li><a href="/%s">%s</a></li>' % (t, h1_of(t)) for t in RELATED[slug])
    return '<section class="related" aria-label="À lire aussi"><h2>À lire aussi</h2><ul>%s</ul></section>' % lis

NAV_OLD_ARTICLE = '<nav><a href="/">Accueil</a><a href="/#newsletter">Newsletter</a></nav>'
NAV_NEW_ARTICLE = '<nav><a href="/">Accueil</a><a href="/articles">Tous les articles</a><a href="/#newsletter">Newsletter</a></nav>'

def main():
    report = []
    for slug in ARTICLES:
        f = slug + '.html'; s = rd(f)
        t, d = META.get(slug, (None, None))
        if t or d: s = set_meta(slug, s, t, d)
        if slug in RELATED:
            s = add_inline(slug, s, report)
            s = re.sub(r'<section class="related".*?</section>', lambda m: related_block(slug), s, flags=re.S)
        s = s.replace(NAV_OLD_ARTICLE, NAV_NEW_ARTICLE)
        wr(f, s)
    # about
    if 'about' in META:
        s = rd('about.html'); s = set_meta('about', s, *META['about']); wr('about.html', s)
    for ex in EXTRA:
        if ex in META:
            s = rd(ex + '.html'); s = set_meta(ex, s, *META[ex]); wr(ex + '.html', s)
    # pages légales : description + canonical
    for slug, d in LEGAL_DESC.items():
        s = rd(slug + '.html')
        if 'name="description"' not in s:
            s = s.replace('<meta name="robots"', '<meta name="description" content="%s"><link rel="canonical" href="%s/%s"><meta name="robots"' % (H(d), BASE, slug), 1)
        wr(slug + '.html', s)
    for r in report: print(*r)

if __name__ == '__main__':
    main()
