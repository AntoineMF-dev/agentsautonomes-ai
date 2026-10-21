# Configuration propre au site agentsautonomes.ai
BASE = 'https://agentsautonomes.ai'
SITE = 'AgentsAutonomes.ai'
LEGAL = ['mentions-legales', 'confidentialite']
EXTRA = ['pack-agents-ia-n8n']          # page de vente (hors articles)
META = {
 'agent-ia-comptabilite': ("Agent IA comptabilité : saisie et rapprochements", None),
 'agent-ia-compte-rendu-de-reunion': ("Agent IA de compte rendu de réunion : du brut au CR", "Agent IA de compte rendu : des notes brutes à un CR structuré (décisions, actions, échéances), relecture humaine et règles CNIL si vous enregistrez."),
 'agent-ia-demandes-de-devis': ("Agent IA pour les demandes de devis : qualifier et préparer", "Agent IA pour demandes de devis : qualifier, préparer le devis depuis votre grille tarifaire et relancer, avec un humain qui valide chaque envoi."),
 'agent-ia-factures-fournisseurs': ("Agent IA factures fournisseurs : architecture et garde-fous", "Factures fournisseurs en données structurées depuis sept. 2026 : architecture d'un agent IA qui contrôle et prépare la saisie, avec garde-fous anti-fraude."),
 'agent-ia-prospection-commerciale': ("Agent IA de prospection commerciale : comment le créer", None),
 'agent-ia-rh-recrutement': ("Agent IA recrutement : automatiser sans déshumaniser", None),
 'agent-ia-sav': (None, "Automatiser son SAV avec un agent IA : cas concrets, outils, limites et ROI. Guide pour PME qui veulent réduire les délais sans recruter."),
 'agent-ia-trier-emails-n8n': (None, "Construire un agent IA de tri d'emails avec n8n : classification, étiquettes, brouillons validés par un humain, journal de contrôle et risques."),
 'agent-ia-vs-chatbot-pme': (None, "Chatbot ou agent IA autonome ? La différence réelle, ce que ça change pour une PME et comment choisir l'outil selon votre cas d'usage."),
 'ai-act-pme-agent-ia-obligations-2026': ("AI Act et PME : obligations 2026 avec un agent IA", "AI Act : transparence depuis le 2 août 2026, maîtrise de l'IA, haut risque reporté à fin 2027. Ce que cela impose à une PME qui déploie un agent IA."),
 'meilleurs-outils-agent-ia-sans-developpeur': (None, "Comparatif des meilleurs outils no-code pour déployer un agent IA : n8n, Make, Zapier, Relevance AI. Avantages, limites et cas d'usage."),
 'pack-agents-ia-n8n': ("Pack 5 agents IA n8n pour PME : workflows prêts à importer", "5 workflows n8n prêts à importer : tri des e-mails, relance des factures impayées, SAV, veille concurrentielle et devis. Guide en français."),
}
LEGAL_DESC = {}
ARTICLES = ['agent-ia-comptabilite','agent-ia-factures-fournisseurs','agent-ia-relance-factures-impayees','roi-agent-ia',
 'agent-ia-prospection-commerciale','agent-ia-demandes-de-devis','agent-ia-veille-concurrentielle','agent-ia-sav',
 'agent-ia-rh-recrutement','agent-ia-gestion-projet','agent-ia-compte-rendu-de-reunion','agent-ia-trier-emails-n8n',
 'ai-act-pme-agent-ia-obligations-2026','erreurs-agent-ia',
 'meilleurs-outils-agent-ia-sans-developpeur','autogpt-crewai-n8n-quel-agent-choisir','agent-ia-vs-chatbot-pme','agent-ia-pme-zero-budget',
 'agents-ia-bilan-2025','agents-ia-multimodaux','agents-ia-remplacent-salarie']
RELATED = {
 'agent-ia-comptabilite': ['agent-ia-factures-fournisseurs','agent-ia-relance-factures-impayees','roi-agent-ia'],
 'agent-ia-compte-rendu-de-reunion': ['agent-ia-gestion-projet','agent-ia-trier-emails-n8n','ai-act-pme-agent-ia-obligations-2026'],
 'agent-ia-demandes-de-devis': ['agent-ia-prospection-commerciale','agent-ia-veille-concurrentielle','agent-ia-relance-factures-impayees'],
 'agent-ia-factures-fournisseurs': ['agent-ia-comptabilite','agent-ia-relance-factures-impayees','ai-act-pme-agent-ia-obligations-2026'],
 'agent-ia-gestion-projet': ['agent-ia-compte-rendu-de-reunion','agent-ia-rh-recrutement','agent-ia-trier-emails-n8n'],
 'agent-ia-pme-zero-budget': ['meilleurs-outils-agent-ia-sans-developpeur','agent-ia-vs-chatbot-pme','agent-ia-trier-emails-n8n'],
 'agent-ia-prospection-commerciale': ['agent-ia-demandes-de-devis','agent-ia-veille-concurrentielle','roi-agent-ia'],
 'agent-ia-relance-factures-impayees': ['agent-ia-comptabilite','agent-ia-factures-fournisseurs','roi-agent-ia'],
 'agent-ia-rh-recrutement': ['ai-act-pme-agent-ia-obligations-2026','agent-ia-gestion-projet','erreurs-agent-ia'],
 'agent-ia-sav': ['erreurs-agent-ia','agent-ia-vs-chatbot-pme','autogpt-crewai-n8n-quel-agent-choisir'],
 'agent-ia-trier-emails-n8n': ['agent-ia-compte-rendu-de-reunion','autogpt-crewai-n8n-quel-agent-choisir','meilleurs-outils-agent-ia-sans-developpeur'],
 'agent-ia-veille-concurrentielle': ['agent-ia-prospection-commerciale','agent-ia-demandes-de-devis','agents-ia-multimodaux'],
 'agent-ia-vs-chatbot-pme': ['agent-ia-pme-zero-budget','agents-ia-remplacent-salarie','agent-ia-sav'],
 'agents-ia-bilan-2025': ['agents-ia-remplacent-salarie','roi-agent-ia','agents-ia-multimodaux'],
 'agents-ia-multimodaux': ['agent-ia-factures-fournisseurs','agents-ia-bilan-2025','agent-ia-veille-concurrentielle'],
 'agents-ia-remplacent-salarie': ['agents-ia-bilan-2025','agent-ia-vs-chatbot-pme','roi-agent-ia'],
 'ai-act-pme-agent-ia-obligations-2026': ['erreurs-agent-ia','agent-ia-rh-recrutement','agent-ia-factures-fournisseurs'],
 'autogpt-crewai-n8n-quel-agent-choisir': ['meilleurs-outils-agent-ia-sans-developpeur','agent-ia-trier-emails-n8n','agent-ia-pme-zero-budget'],
 'erreurs-agent-ia': ['ai-act-pme-agent-ia-obligations-2026','roi-agent-ia','agent-ia-sav'],
 'meilleurs-outils-agent-ia-sans-developpeur': ['autogpt-crewai-n8n-quel-agent-choisir','agent-ia-pme-zero-budget','agent-ia-trier-emails-n8n'],
 'roi-agent-ia': ['agent-ia-relance-factures-impayees','agents-ia-bilan-2025','erreurs-agent-ia'],
}
INLINE = dict(RELATED)
Q = r"(?:'|’|&#x27;|&#39;)"
PHRASES = {
 'agent-ia-comptabilite': r"comptabilité",
 'agent-ia-factures-fournisseurs': r"factures? fournisseurs?",
 'agent-ia-relance-factures-impayees': r"relances? (?:de |des )?factures?(?: impayées?)?|factures? impayées?",
 'roi-agent-ia': r"(?-i:\bROI\b)|retour sur investissement",
 'agent-ia-prospection-commerciale': r"prospection(?: commerciale)?",
 'agent-ia-demandes-de-devis': r"demandes? de devis",
 'agent-ia-veille-concurrentielle': r"veille concurrentielle",
 'agent-ia-rh-recrutement': r"recrutement",
 'agent-ia-gestion-projet': r"gestion de projet",
 'agent-ia-compte-rendu-de-reunion': r"comptes? rendus?(?: de réunion)?",
 'agent-ia-trier-emails-n8n': r"trier (?:ses |vos |les )?e-?mails?|tri des e-?mails?",
 'agent-ia-pme-zero-budget': r"zéro budget|budget zéro|sans budget",
 'meilleurs-outils-agent-ia-sans-developpeur': r"sans développeur|outils no-code",
 'autogpt-crewai-n8n-quel-agent-choisir': r"AutoGPT|CrewAI",
 'agent-ia-vs-chatbot-pme': r"chatbots?",
 'agents-ia-bilan-2025': r"bilan 2025|agents IA en 2025",
 'agents-ia-multimodaux': r"multimodaux?",
 'agents-ia-remplacent-salarie': r"remplace(?:nt|r)? (?:déjà )?un salarié",
 'ai-act-pme-agent-ia-obligations-2026': r"AI Act",
 'erreurs-agent-ia': r"erreurs à éviter|erreurs de déploiement",
 'agent-ia-sav': r"service après-vente|SAV",
}
SHORT = {
 'agent-ia-comptabilite': "l'agent IA en comptabilité",
 'agent-ia-factures-fournisseurs': "l'agent IA de traitement des factures fournisseurs",
 'agent-ia-relance-factures-impayees': "l'agent IA de relance des factures impayées",
 'roi-agent-ia': "le calcul du ROI d'un agent IA",
 'agent-ia-prospection-commerciale': "l'agent IA de prospection commerciale",
 'agent-ia-demandes-de-devis': "l'agent IA pour les demandes de devis",
 'agent-ia-veille-concurrentielle': "l'agent IA de veille concurrentielle",
 'agent-ia-rh-recrutement': "l'agent IA pour le recrutement",
 'agent-ia-gestion-projet': "l'agent IA en gestion de projet",
 'agent-ia-compte-rendu-de-reunion': "l'agent IA de compte rendu de réunion",
 'agent-ia-trier-emails-n8n': "l'agent IA de tri d'emails avec n8n",
 'agent-ia-pme-zero-budget': "démarrer avec un agent IA à zéro budget",
 'meilleurs-outils-agent-ia-sans-developpeur': "les meilleurs outils d'agent IA sans développeur",
 'autogpt-crewai-n8n-quel-agent-choisir': "le choix entre AutoGPT, CrewAI et n8n",
 'agent-ia-vs-chatbot-pme': "la différence entre agent IA et chatbot",
 'agents-ia-bilan-2025': "le bilan des agents IA en 2025",
 'agents-ia-multimodaux': "les agents IA multimodaux",
 'agents-ia-remplacent-salarie': "les agents IA qui remplacent déjà un salarié",
 'ai-act-pme-agent-ia-obligations-2026': "les obligations AI Act d'une PME",
 'erreurs-agent-ia': "les erreurs à éviter avec un agent IA",
 'agent-ia-sav': "l'agent IA pour le SAV",
}
THEMES = [
 ('Finance et comptabilité', ['agent-ia-comptabilite','agent-ia-factures-fournisseurs','agent-ia-relance-factures-impayees','roi-agent-ia']),
 ('Ventes et marketing', ['agent-ia-prospection-commerciale','agent-ia-demandes-de-devis','agent-ia-veille-concurrentielle','agent-ia-sav']),
 ('RH et organisation', ['agent-ia-rh-recrutement','agent-ia-gestion-projet','agent-ia-compte-rendu-de-reunion','agent-ia-trier-emails-n8n']),
 ('Conformité et bonnes pratiques', ['ai-act-pme-agent-ia-obligations-2026','erreurs-agent-ia']),
 ('Choisir ses outils et démarrer', ['meilleurs-outils-agent-ia-sans-developpeur','autogpt-crewai-n8n-quel-agent-choisir','agent-ia-vs-chatbot-pme','agent-ia-pme-zero-budget']),
 ('Panorama et tendances', ['agents-ia-bilan-2025','agents-ia-multimodaux','agents-ia-remplacent-salarie']),
]
ARTICLES_TITLE = 'Tous les articles : agents IA autonomes pour PME'
ARTICLES_DESC = "Les 21 articles d'AgentsAutonomes.ai par thème : finance, ventes, RH, conformité AI Act, choix des outils, panorama des agents IA."
ARTICLES_INTRO = "Les 21 articles d'AgentsAutonomes.ai, classés par thème : finance, ventes, RH, conformité AI Act, outils et panorama des agents IA."
EXTRA_LINKS = [('Ressource : pack de workflows', ['pack-agents-ia-n8n'])]
INDEX_NAV_OLD = '<nav><a href="#articles">Articles</a>'
INDEX_NAV_NEW = '<nav><a href="/articles">Tous les articles</a>'
