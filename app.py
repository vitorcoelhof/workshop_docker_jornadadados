
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# Configuração da página
st.set_page_config(
    page_title="Hello World App ✨",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para estilizar a aplicação
st.markdown("""
<style>
    /* Fundo gradiente */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Cartões customizados */
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    /* Título principal */
    .main-title {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: #f0f0f0;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Botões customizados */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

def hello_world():
    """Função principal que retorna mensagem personalizada"""
    user_name = st.session_state.get('user_name', 'Visitante')
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"🌟 Olá, {user_name}! Bem-vindo ao nosso app incrível! 🌟"

def create_sample_chart():
    """Cria um gráfico de exemplo bonito"""
    # Dados de exemplo
    data = {
        'Categoria': ['Python', 'Streamlit', 'Docker', 'Git', 'Poetry'],
        'Conhecimento': [85, 70, 60, 75, 65],
        'Interesse': [95, 90, 80, 85, 70]
    }
    df = pd.DataFrame(data)
    
    # Gráfico radar
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=df['Conhecimento'],
        theta=df['Categoria'],
        fill='toself',
        name='Conhecimento Atual',
        line_color='#667eea'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=df['Interesse'],
        theta=df['Categoria'],
        fill='toself',
        name='Nível de Interesse',
        line_color='#764ba2'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="📊 Radar de Habilidades Técnicas",
        font=dict(size=14),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def create_metrics_dashboard():
    """Cria dashboard com métricas"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🚀 Projetos Completados",
            value="12",
            delta="3 este mês"
        )
    
    with col2:
        st.metric(
            label="⭐ Rating médio",
            value="4.8",
            delta="0.2"
        )
    
    with col3:
        st.metric(
            label="📈 Produtividade",
            value="95%",
            delta="5%"
        )
    
    with col4:
        st.metric(
            label="🎯 Metas atingidas",
            value="8/10",
            delta="2"
        )

def main():
    """Função principal da aplicação"""
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎛️ Configurações")
        
        # Input do nome do usuário
        user_name = st.text_input(
            "Qual é o seu nome?",
            value="Vitor",
            key="user_name"
        )
        
        st.markdown("---")
        
        # Seleção de tema
        theme = st.selectbox(
            "🎨 Escolha um tema:",
            ["Moderno", "Clássico", "Neon", "Minimalista"]
        )
        
        # Botão de informações
        if st.button("ℹ️ Sobre este App"):
            st.info("""
            🌟 **Hello World App Avançado**
            
            ✨ Criado com Streamlit
            🐳 Rodando em Docker  
            🚀 Interface moderna e responsiva
            
            Versão: 2.0.0
            """)
        
        st.markdown("---")
        st.markdown("### 📊 Estatísticas em tempo real")
        
        # Placeholder para atualização em tempo real
        status_placeholder = st.empty()
        
    # Conteúdo principal
    st.markdown('<h1 class="main-title">🌟 Hello World App Moderno 🌟</h1>', 
                unsafe_allow_html=True)
    
    st.markdown('<p class="subtitle">Uma interface linda criada com Streamlit</p>', 
                unsafe_allow_html=True)
    
    # Mensagem principal
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="
            background: white; 
            padding: 2rem; 
            border-radius: 15px; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
            margin: 2rem 0;
        ">
            <h3 style="color: #667eea; margin-bottom: 1rem;">
                {hello_world()}
            </h3>
            <p style="color: #666; font-size: 1.1rem;">
                ⏰ Horário atual: <strong>{datetime.now().strftime("%H:%M:%S")}</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Dashboard de métricas
    st.markdown("### 📊 Dashboard Interativo")
    create_metrics_dashboard()
    
    # Separador visual
    st.markdown("---")
    
    # Gráfico interativo
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.plotly_chart(create_sample_chart(), use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Funcionalidades")
        
        features = [
            "✅ Interface responsiva",
            "✅ Gráficos interativos", 
            "✅ Métricas em tempo real",
            "✅ Design moderno",
            "✅ Fácil personalização",
            "✅ Pronto para produção"
        ]
        
        for feature in features:
            st.markdown(f"**{feature}**")
        
        # Botão de ação
        if st.button("🚀 Começar Agora!", key="start_btn"):
            st.balloons()
            st.success("🎉 Bem-vindo ao futuro das interfaces web!")
    
    # Seção de feedback
    st.markdown("---")
    st.markdown("### 💬 Seu Feedback")
    
    col1, col2 = st.columns(2)
    
    with col1:
        rating = st.slider("⭐ Avalie este app:", 1, 5, 5)
        feedback = st.text_area("💭 Deixe sua opinião:")
        
        if st.button("📤 Enviar Feedback"):
            st.success(f"Obrigado pelo seu feedback! Rating: {rating}⭐")
    
    with col2:
        st.markdown("#### 🔥 Recursos Premium")
        st.info("""
        🎨 **Temas personalizados**  
        📊 **Mais gráficos**  
        🔔 **Notificações**  
        💾 **Salvar configurações**  
        🌙 **Modo escuro**
        """)
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🏠 Início**")
    with col2:
        st.markdown("**📧 Contato**")
    with col3:
        st.markdown("**📱 Redes Sociais**")
    
    # Atualização em tempo real na sidebar
    with status_placeholder.container():
        current_time = datetime.now()
        st.markdown(f"""
        **🕒 Última atualização:**  
        {current_time.strftime("%H:%M:%S")}
        
        **👥 Usuários online:** 42  
        **📊 Sessões hoje:** 127
        """)

if __name__ == "__main__":
    main()
