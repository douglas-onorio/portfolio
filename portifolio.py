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
    a {text-decoration: none; color: inherit;}
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO E BIO ---
col1, col2 = st.columns([1, 3])

with col1:
    # Tenta pegar a foto do GitHub, se falhar, usa um emoji
    try:
        st.image("https://github.com/douglas-onorio.png", width=130)
    except:
        st.title("👨‍💻")

with col2:
    st.markdown('<div class="main-header">Douglas Onorio</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Desenvolvedor Python & Soluções de Dados</div>', unsafe_allow_html=True)
    st.write("""
    Especialista em transformar processos manuais complexos em aplicações web inteligentes e automatizadas. 
    Foco em **Python, Análise de Dados e Automação de E-commerce (Mercado Livre)**. 
    Abaixo estão algumas das soluções que desenvolvi para resolver problemas reais de negócio.
    """)
    
    # Ícones de Redes Sociais
    st.markdown("""
    <a href="https://www.linkedin.com/in/douglas-onorio-584766173/" target="_blank">🔗 LinkedIn</a> • 
    <a href="https://github.com/douglas-onorio" target="_blank">💻 GitHub</a>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- FUNÇÃO PARA CRIAR CARDS DE PROJETO ---
def project_card(title, desc, techs, app_link, repo_link, icon="🚀"):
    tech_html = "".join([f'<span class="tech-tag">{t}</span>' for t in techs])
    
    # Botões
    btn_app = f'[👉 Ver App Online]({app_link})' if app_link else "*(App Desktop/Offline)*"
    btn_repo = f'[📂 Ver Código]({repo_link})'
    
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{icon} {title}</div>
        <div class="card-desc">{desc}</div>
        <div style="margin-bottom: 15px;">{tech_html}</div>
        <b>{btn_app}</b> &nbsp;|&nbsp; {btn_repo}
    </div>
    """, unsafe_allow_html=True)

# --- LISTA DE PROJETOS ---
st.subheader("🛠️ Projetos em Destaque")

# Projeto 1: Auditoria
project_card(
    title="Auditoria Financeira Mercado Livre",
    desc="Sistema completo para auditar vendas do ML. Realiza cálculo de margem real, integra com API do Google Sheets para custos e possui algoritmo complexo para rateio de 'Pacotes' (Bundles), exportando relatórios Excel com fórmulas.",
    techs=["Python", "Streamlit", "Pandas", "Google Sheets API", "XlsxWriter"],
    app_link="https://auditoria-mercadolivre.streamlit.app/",
    repo_link="https://github.com/douglas-onorio/Auditoria-Mercado-Livre",
    icon="💰"
)

# Projeto 2: Análise Full
project_card(
    title="Dashboard de Estoque Full",
    desc="Migração de legado VBA para Web App. Dashboard interativo para gestão de estoque Full Fulfillment. Processa grandes volumes de dados, simula reposição de estoque e gerencia múltiplas empresas simultaneamente.",
    techs=["Python", "Pandas", "Business Intelligence", "VBA to Python"],
    app_link="https://estoque-full.streamlit.app/",
    repo_link="https://github.com/douglas-onorio/analise-full-dashboard",
    icon="📦"
)

# Projeto 3: Curva A (Scraper)
project_card(
    title="Curva A - Scraper de Preços",
    desc="Aplicação Desktop com interface gráfica para monitoramento de concorrência. Coleta preços, visitas e dados de vendedores automaticamente, com comportamento humanizado para evitar bloqueios.",
    techs=["Python", "Web Scraping", "Playwright", "Tkinter", "Automação"],
    app_link=None, # App Desktop
    repo_link="https://github.com/douglas-onorio/app-curva-a", # Ajuste se o link for diferente
    icon="🕷️"
)

st.markdown("---")
st.caption("© 2025 Douglas Onorio. Desenvolvido com Streamlit.")
