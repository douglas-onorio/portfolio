import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Portfólio | Douglas Onorio",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main-header {font-size: 2.5rem; font-weight: 700; color: #333;}
    .sub-header {font-size: 1.5rem; color: #555;}
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .card:hover {transform: scale(1.02);}
    .card-title {font-size: 1.2rem; font-weight: bold; margin-bottom: 10px;}
    .card-desc {font-size: 0.95rem; color: #666; margin-bottom: 15px;}
    .tech-tag {
        display: inline-block;
        background-color: #f0f2f6;
        color: #31333F;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    .internal-badge {
        display: inline-block;
        background-color: #fff3cd;
        color: #856404;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: bold;
        border: 1px solid #ffeeba;
    }
    /* Ajuste para botões de idioma */
    .stButton button {
        width: 100%;
        padding: 5px;
        font-size: 20px; 
    }
    /* Estilo dos links dentro dos cards */
    .card a {
        color: #007BFF;
        text-decoration: none;
        font-weight: 500;
    }
    .card a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# --- GERENCIAMENTO DE ESTADO (IDIOMA) ---
if 'language' not in st.session_state:
    st.session_state['language'] = 'pt'

def set_language(lang):
    st.session_state['language'] = lang

# --- DICIONÁRIO DE TEXTOS (TRADUÇÕES: PT / EN / ES) ---
translations = {
    'pt': {
        'role': 'Desenvolvedor Python & Soluções de Dados',
        'bio': """Especialista em transformar processos manuais complexos em aplicações web inteligentes e automatizadas. 
                  Foco em **Python, Análise de Dados e Automação de E-commerce (Mercado Livre)**. 
                  Abaixo estão algumas das soluções que desenvolvi para resolver problemas reais de negócio.""",
        'section_title': '🛠️ Projetos Open Source',
        'section_internal': '🔒 Soluções Internas / Corporativas',
        'footer': '© 2025 Douglas Onorio. Desenvolvido com Streamlit.',
        'btn_app': '👉 Ver App Online',
        'btn_repo': '📂 Ver Código',
        'btn_desktop': 'App Desktop/Offline',
        'lbl_private': '🔒 Projeto Privado (Uso Interno)',
        
        # Projetos Públicos
        'p1_title': 'Auditoria Financeira Mercado Livre',
        'p1_desc': 'Sistema completo para auditar vendas do ML. Realiza cálculo de margem real, integra com API do Google Sheets para custos e possui algoritmo complexo para rateio de "Pacotes" (Bundles), exportando relatórios Excel com fórmulas.',
        'p2_title': 'Dashboard de Estoque Full',
        'p2_desc': 'Migração de legado VBA para Web App. Dashboard interativo para gestão de estoque Full Fulfillment. Processa grandes volumes de dados, simula reposição de estoque e gerencia múltiplas empresas simultaneamente.',
        'p3_title': 'Curva A - Scraper de Preços',
        'p3_desc': 'Aplicação Desktop com interface gráfica para monitoramento de concorrência. Coleta preços, visitas e dados de vendedores automaticamente, com comportamento humanizado para evitar bloqueios.',
        
        # Projetos Internos (Novos)
        'p4_title': 'Monitor de Vendas Real-Time (Playwright)',
        'p4_desc': 'Dashboard estratégico que monitora vendas ao vivo via Web Scraping avançado. Extrai dados JSON injetados no HTML (Server-Side Data) para precisão absoluta e plota comparativos "Hoje vs Ontem" em tempo real.',
        'p5_title': 'Orquestrador de Agentes SAC (Multi-Contas)',
        'p5_desc': 'Painel de controle centralizado para gestão de bots de atendimento. Gerencia múltiplas lojas/sessões simultaneamente, disparando workers em background para responder perguntas sem bloquear a interface do usuário.',
        'p6_title': 'Cérebro IA (Integração Gemini API)',
        'p6_desc': 'Backend de inteligência artificial para E-commerce. Utiliza Google Gemini para gerar respostas contextualizadas por produto, aplicando assinaturas dinâmicas e regras de negócio específicas para cada uma das 8 lojas do grupo.',
    },
    'en': {
        'role': 'Python Developer & Data Solutions',
        'bio': """Specialist in transforming complex manual processes into intelligent, automated web applications. 
                  Focus on **Python, Data Analysis, and E-commerce Automation (Mercado Livre)**. 
                  Below are some of the solutions I developed to solve real business problems.""",
        'section_title': '🛠️ Open Source Projects',
        'section_internal': '🔒 Internal / Corporate Solutions',
        'footer': '© 2025 Douglas Onorio. Built with Streamlit.',
        'btn_app': '👉 View Live App',
        'btn_repo': '📂 View Code',
        'btn_desktop': 'Desktop App/Offline',
        'lbl_private': '🔒 Private Project (Internal Use)',

        # Public Projects
        'p1_title': 'Mercado Livre Financial Audit',
        'p1_desc': 'Complete system for auditing ML sales. Calculates real profit margins, integrates with Google Sheets API for costs, and features a complex algorithm for "Bundles" allocation, exporting Excel reports with live formulas.',
        'p2_title': 'Full Fulfillment Inventory Dashboard',
        'p2_desc': 'Migration from legacy VBA to Web App. Interactive dashboard for Full Fulfillment inventory management. Processes large data volumes, simulates stock replenishment, and manages multiple companies simultaneously.',
        'p3_title': 'Curve A - Price Scraper',
        'p3_desc': 'Desktop Application with GUI for competitor monitoring. Automatically collects prices, visits, and seller data, featuring humanized behavior to avoid IP blocking.',

        # Internal Projects
        'p4_title': 'Real-Time Sales Monitor (Playwright)',
        'p4_desc': 'Strategic dashboard monitoring live sales via advanced Web Scraping. Extracts JSON data injected into HTML (Server-Side Data) for absolute precision and plots "Today vs Yesterday" comparisons in real-time.',
        'p5_title': 'CS Agent Orchestrator (Multi-Account)',
        'p5_desc': 'Centralized control panel for customer service bots. Manages multiple stores/sessions simultaneously, launching background workers to answer questions without blocking the UI.',
        'p6_title': 'AI Brain (Gemini API Integration)',
        'p6_desc': 'Artificial Intelligence backend for E-commerce. Uses Google Gemini to generate context-aware answers per product, applying dynamic signatures and specific business rules for each of the group\'s 8 stores.',
    },
    'es': {
        'role': 'Desarrollador Python & Soluciones de Datos',
        'bio': """Especialista en transformar procesos manuales complejos en aplicaciones web inteligentes y automatizadas. 
                  Enfoque en **Python, Análisis de Datos y Automatización de E-commerce (Mercado Libre)**. 
                  A continuación, presento algunas soluciones que desarrollé para resolver problemas reales de negocio.""",
        'section_title': '🛠️ Proyectos Open Source',
        'section_internal': '🔒 Soluciones Internas / Corporativas',
        'footer': '© 2025 Douglas Onorio. Desarrollado con Streamlit.',
        'btn_app': '👉 Ver App Online',
        'btn_repo': '📂 Ver Código',
        'btn_desktop': 'App de Escritorio/Offline',
        'lbl_private': '🔒 Proyecto Privado (Uso Interno)',

        # Public Projects
        'p1_title': 'Auditoría Financiera Mercado Libre',
        'p1_desc': 'Sistema completo para auditar ventas de ML. Calcula márgenes reales, integra costos vía Google Sheets API y posee un algoritmo complejo para el prorrateo de "Paquetes" (Bundles), exportando informes en Excel con fórmulas.',
        'p2_title': 'Dashboard de Inventario Full',
        'p2_desc': 'Migración de legado VBA a Web App. Tablero interactivo para gestión de inventario Full Fulfillment. Procesa grandes volúmenes de datos, simula reposición de stock y gestiona múltiples empresas simultáneamente.',
        'p3_title': 'Curva A - Scraper de Precios',
        'p3_desc': 'Aplicación de Escritorio con interfaz gráfica para monitoreo de competencia. Recolecta precios, visitas y datos de vendedores automáticamente, con comportamiento humanizado para evitar bloqueos.',

        # Internal Projects
        'p4_title': 'Monitor de Ventas Real-Time (Playwright)',
        'p4_desc': 'Dashboard estratégico que monitorea ventas en vivo vía Web Scraping avanzado. Extrae datos JSON inyectados en HTML (Server-Side Data) para precisión absoluta y grafica comparativas "Hoy vs Ayer" en tiempo real.',
        'p5_title': 'Orquestador de Agentes SAC (Multi-Cuenta)',
        'p5_desc': 'Panel de control centralizado para gestión de bots de atención. Gestiona múltiples tiendas/sesiones simultáneamente, lanzando workers en segundo plano para responder preguntas sin bloquear la interfaz.',
        'p6_title': 'Cerebro IA (Integración Gemini API)',
        'p6_desc': 'Backend de inteligencia artificial para E-commerce. Utiliza Google Gemini para generar respuestas contextualizadas por producto, aplicando firmas dinámicas y reglas de negocio específicas para cada una de las 8 tiendas.',
    }
}

# Seleciona o dicionário atual com base no estado
t = translations[st.session_state['language']]

# --- BARRA SUPERIOR (BANDEIRAS) ---
col_spacer, col_br, col_en, col_es = st.columns([7, 1, 1, 1])

with col_br:
    if st.button("🇧🇷", key='pt_btn', help="Português"):
        set_language('pt')
        st.rerun()

with col_en:
    if st.button("🇺🇸", key='en_btn', help="English"):
        set_language('en')
        st.rerun()

with col_es:
    if st.button("🇪🇸", key='es_btn', help="Español"):
        set_language('es')
        st.rerun()

# --- CABEÇALHO E BIO ---
col1, col2 = st.columns([1, 3])

with col1:
    try:
        # Foto do GitHub
        st.image("https://github.com/douglas-onorio.png", width=130)
    except:
        st.title("👨‍💻")

with col2:
    st.markdown('<div class="main-header">Douglas Onorio</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">{t["role"]}</div>', unsafe_allow_html=True)
    st.write(t['bio'])
    
    # Ícones de Redes Sociais
    st.markdown("""
    <a href="https://www.linkedin.com/in/douglas-onorio-584766173/" target="_blank" style="text-decoration:none; color:#0077b5; font-weight:bold;">🔗 LinkedIn</a> • 
    <a href="https://github.com/douglas-onorio" target="_blank" style="text-decoration:none; color:#333; font-weight:bold;">💻 GitHub</a>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- FUNÇÃO PARA CRIAR CARDS DE PROJETO ---
def project_card(title, desc, techs, app_link, repo_link, icon="🚀"):
    tech_html = "".join([f'<span class="tech-tag">{tech}</span>' for tech in techs])
    
    # Textos traduzidos
    txt_app = t['btn_app']
    txt_repo = t['btn_repo']
    txt_desk = t['btn_desktop']
    lbl_priv = t['lbl_private']

    # Construção dos Links
    if app_link:
        btn_app_html = f'<a href="{app_link}" target="_blank"><strong>{txt_app}</strong></a>'
    else:
        # Se não tiver link do App, verifica se é desktop ou interno
        if repo_link is None:
             btn_app_html = "" # Não exibe nada no lugar do App link se for interno puro
        else:
             btn_app_html = f'<span style="color:#666; font-style:italic;">{txt_desk}</span>'
        
    # Lógica para Repositório Privado vs Público
    if repo_link:
        btn_repo_html = f'<a href="{repo_link}" target="_blank">{txt_repo}</a>'
        separator = "&nbsp;|&nbsp;" if btn_app_html else ""
    else:
        btn_repo_html = f'<span class="internal-badge">{lbl_priv}</span>'
        separator = "<br><br>" # Quebra de linha para ficar bonito se for interno

    st.markdown(f"""
    <div class="card">
        <div class="card-title">{icon} {title}</div>
        <div class="card-desc">{desc}</div>
        <div style="margin-bottom: 15px;">{tech_html}</div>
        {btn_app_html} {separator} {btn_repo_html}
    </div>
    """, unsafe_allow_html=True)

# --- LISTA DE PROJETOS OPEN SOURCE ---
st.subheader(t['section_title'])

# Projeto 1: Auditoria
project_card(
    title=t['p1_title'],
    desc=t['p1_desc'],
    techs=["Python", "Streamlit", "Pandas", "Google Sheets API", "XlsxWriter"],
    app_link="https://auditoria-mercadolivre.streamlit.app/",
    repo_link="https://github.com/douglas-onorio/Auditoria-Mercado-Livre",
    icon="💰"
)

# Projeto 2: Análise Full
project_card(
    title=t['p2_title'],
    desc=t['p2_desc'],
    techs=["Python", "Pandas", "Business Intelligence", "VBA to Python"],
    app_link="https://estoque-full.streamlit.app/",
    repo_link="https://github.com/douglas-onorio/analise-full-dashboard",
    icon="📦"
)

# Projeto 3: Curva A (Scraper)
project_card(
    title=t['p3_title'],
    desc=t['p3_desc'],
    techs=["Python", "Web Scraping", "Playwright", "Tkinter", "Automation"],
    app_link=None, 
    repo_link="https://github.com/douglas-onorio/Curva-A---ML",
    icon="🕷️"
)

# --- LISTA DE PROJETOS INTERNOS ---
st.markdown("<br>", unsafe_allow_html=True)
st.subheader(t['section_internal'])

# Projeto 4: Vendas ao Vivo
project_card(
    title=t['p4_title'],
    desc=t['p4_desc'],
    techs=["Streamlit", "Playwright", "RegEx (JSON Extract)", "Matplotlib", "Data Visualization"],
    app_link=None,
    repo_link=None, # Define como Privado
    icon="📈"
)

# Projeto 5: Orquestrador de Agentes
project_card(
    title=t['p5_title'],
    desc=t['p5_desc'],
    techs=["Python", "Streamlit", "Subprocess Management", "Cookies/Auth", "Multi-Tenancy"],
    app_link=None,
    repo_link=None, # Define como Privado
    icon="🤖"
)

# Projeto 6: Cérebro Gemini
project_card(
    title=t['p6_title'],
    desc=t['p6_desc'],
    techs=["Google Gemini API", "LLM Integration", "JSON", "Prompt Engineering", "Python Backend"],
    app_link=None,
    repo_link=None, # Define como Privado
    icon="🧠"
)

st.markdown("---")
st.caption(t['footer'])
