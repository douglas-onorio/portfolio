import streamlit as st
from PIL import Image

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
    /* Estilo para os botões de bandeira ficarem alinhados e bonitos */
    .stButton button {
        background: none;
        border: none;
        font-size: 20px;
        padding: 0px 10px;
    }
    .stButton button:hover {
        background: #f0f2f6;
        border-radius: 5px;
    }
    a {text-decoration: none; color: inherit;}
    </style>
""", unsafe_allow_html=True)

# --- GERENCIAMENTO DE ESTADO (IDIOMA) ---
if 'language' not in st.session_state:
    st.session_state['language'] = 'pt'

def set_language(lang):
    st.session_state['language'] = lang

# --- DICIONÁRIO DE TEXTOS (TRADUÇÕES) ---
translations = {
    'pt': {
        'role': 'Desenvolvedor Python & Soluções de Dados',
        'bio': """Especialista em transformar processos manuais complexos em aplicações web inteligentes e automatizadas. 
                  Foco em **Python, Análise de Dados e Automação de E-commerce (Mercado Livre)**. 
                  Abaixo estão algumas das soluções que desenvolvi para resolver problemas reais de negócio.""",
        'section_title': '🛠️ Projetos em Destaque',
        'footer': '© 2025 Douglas Onorio. Desenvolvido com Streamlit.',
        'btn_app': '👉 Ver App Online',
        'btn_repo': '📂 Ver Código',
        'btn_desktop': 'App Desktop/Offline',
        # Projetos
        'p1_title': 'Auditoria Financeira Mercado Livre',
        'p1_desc': 'Sistema completo para auditar vendas do ML. Realiza cálculo de margem real, integra com API do Google Sheets para custos e possui algoritmo complexo para rateio de "Pacotes" (Bundles), exportando relatórios Excel com fórmulas.',
        'p2_title': 'Dashboard de Estoque Full',
        'p2_desc': 'Migração de legado VBA para Web App. Dashboard interativo para gestão de estoque Full Fulfillment. Processa grandes volumes de dados, simula reposição de estoque e gerencia múltiplas empresas simultaneamente.',
        'p3_title': 'Curva A - Scraper de Preços',
        'p3_desc': 'Aplicação Desktop com interface gráfica para monitoramento de concorrência. Coleta preços, visitas e dados de vendedores automaticamente, com comportamento humanizado para evitar bloqueios.',
    },
    'en': {
        'role': 'Python Developer & Data Solutions',
        'bio': """Specialist in transforming complex manual processes into intelligent, automated web applications. 
                  Focus on **Python, Data Analysis, and E-commerce Automation (Mercado Livre)**. 
                  Below are some of the solutions I developed to solve real business problems.""",
        'section_title': '🛠️ Featured Projects',
        'footer': '© 2025 Douglas Onorio. Built with Streamlit.',
        'btn_app': '👉 View Live App',
        'btn_repo': '📂 View Code',
        'btn_desktop': 'Desktop App/Offline',
        # Projects
        'p1_title': 'Mercado Livre Financial Audit',
        'p1_desc': 'Complete system for auditing ML sales. Calculates real profit margins, integrates with Google Sheets API for costs, and features a complex algorithm for "Bundles" allocation, exporting Excel reports with live formulas.',
        'p2_title': 'Full Fulfillment Inventory Dashboard',
        'p2_desc': 'Migration from legacy VBA to Web App. Interactive dashboard for Full Fulfillment inventory management. Processes large data volumes, simulates stock replenishment, and manages multiple companies simultaneously.',
        'p3_title': 'Curve A - Price Scraper',
        'p3_desc': 'Desktop Application with GUI for competitor monitoring. Automatically collects prices, visits, and seller data, featuring humanized behavior to avoid IP blocking.',
    }
}

# Seleciona o dicionário atual com base no estado
t = translations[st.session_state['language']]

# --- BARRA SUPERIOR (BANDEIRAS) ---
# Usamos colunas para jogar as bandeiras para a direita
col_spacer, col_br, col_en = st.columns([8, 1, 1])

with col_br:
    if st.button("🇧🇷"):
        set_language('pt')
        st.rerun()

with col_en:
    if st.button("🇺🇸"):
        set_language('en')
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
    <a href="https://www.linkedin.com/in/douglas-onorio-584766173/" target="_blank">🔗 LinkedIn</a> • 
    <a href="https://github.com/douglas-onorio" target="_blank">💻 GitHub</a>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- FUNÇÃO PARA CRIAR CARDS DE PROJETO ---
def project_card(title, desc, techs, app_link, repo_link, icon="🚀"):
    tech_html = "".join([f'<span class="tech-tag">{tech}</span>' for tech in techs])
    
    # Botões traduzidos
    txt_app = t['btn_app']
    txt_repo = t['btn_repo']
    txt_desk = t['btn_desktop']

    btn_app_html = f'[**{txt_app}**]({app_link})' if app_link else f"*{txt_desk}*"
    btn_repo_html = f'[{txt_repo}]({repo_link})'
    
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{icon} {title}</div>
        <div class="card-desc">{desc}</div>
        <div style="margin-bottom: 15px;">{tech_html}</div>
        {btn_app_html} &nbsp;|&nbsp; {btn_repo_html}
    </div>
    """, unsafe_allow_html=True)

# --- LISTA DE PROJETOS ---
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
    app_link=None, # App Desktop
    repo_link="https://github.com/douglas-onorio/app-curva-a",
    icon="🕷️"
)

st.markdown("---")
st.caption(t['footer'])
