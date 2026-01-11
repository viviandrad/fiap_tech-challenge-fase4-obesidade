import streamlit as st
import pandas as pd
import joblib
import numpy as np

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================
st.set_page_config(
    page_title="Avaliação de Risco de Obesidade",
    page_icon="🩺",
    layout="centered"
)

# =====================================================
# CARREGAR MODELO
# =====================================================
modelo = joblib.load("../models/modelo_obesidade.pkl")
COLUNAS_MODELO = list(modelo.feature_names_in_)

# =====================================================
# MAPAS (IGUAIS AO TREINO)
# =====================================================
MAPA_FCVC = {"Raramente": 1, "Às vezes": 2, "Sempre": 3}
MAPA_NCP = {"1 refeição": 1, "2 refeições": 2, "3 refeições": 3, "4 ou mais refeições": 4}
MAPA_CH2O = {"Menos que 1 litro/dia": 1, "1-2 litros/dia": 2, "Mais que 2 litros/dia": 3}
MAPA_FAF = {"Nenhuma": 0, "1–2x/semana": 1, "3–4x/semana": 2, "5x ou mais": 3}
MAPA_TUE = {"0-2 horas/dia": 0, "3-5 horas/dia": 1, "Mais que 5 horas/dia": 2}

MAPA_CAEC = {"Não": "no", "Às vezes": "Sometimes", "Frequentemente": "Frequently"}
MAPA_CALC = {"Não": "no", "Às vezes": "Sometimes", "Frequentemente": "Frequently"}
MAPA_MTRANS = {
    "Carro": "Automobile",
    "Transporte público": "Public_Transportation",
    "Bicicleta": "Bike",
    "A pé": "Walking"
}

MAPA_RESULTADO_MODELO = {
    "abaixo_do_peso": "Abaixo do peso",
    "peso_normal": "Peso adequado",
    "sobrepeso": "Sobrepeso",
    "obesidade_i": "Obesidade – Grau I",
    "obesidade_ii": "Obesidade – Grau II",
    "obesidade_iii": "Obesidade – Grau III"
}

# =====================================================
# CABEÇALHO
# =====================================================
st.title("🩺 Avaliação de Risco de Obesidade")
st.markdown(
    "Ferramenta de apoio à decisão clínica para estimativa de risco de obesidade, "
    "utilizando **Machine Learning** com base em dados físicos, hábitos alimentares "
    "e estilo de vida."
)
st.divider()

# =====================================================
# FORMULÁRIO – ENTRADA DE DADOS
# =====================================================
with st.form("form_obesidade"):

    st.header("1️⃣ Dados Pessoais")
    col1, col2 = st.columns(2)

    with col1:
        idade = st.number_input("Idade", min_value=1, value=20, step=1)
        altura = st.number_input("Altura (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)

    with col2:
        genero = st.selectbox("Gênero", ["Feminino", "Masculino"])
        peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.5)

    st.header("2️⃣ Histórico Clínico")
    col1, col2 = st.columns(2)

    with col1:
        historico = st.radio("Histórico familiar de excesso de peso?", ["Não", "Sim"], horizontal=True)
        fuma = st.radio("Paciente é fumante?", ["Não", "Sim"], horizontal=True)

    with col2:
        caloricos = st.radio("Consome alimentos calóricos frequentemente?", ["Não", "Sim"], horizontal=True)
        monitora = st.radio("Monitora ingestão calórica?", ["Não", "Sim"], horizontal=True)

    st.header("3️⃣ Hábitos Alimentares")
    col1, col2 = st.columns(2)

    with col1:
        ncp_label = st.selectbox("Refeições por dia", MAPA_NCP.keys())
        ch2o_label = st.selectbox("Consumo diário de água", MAPA_CH2O.keys())
        caec_label = st.selectbox("Come entre as refeições?", MAPA_CAEC.keys())

    with col2:
        fcvc_label = st.selectbox("Consumo de vegetais", MAPA_FCVC.keys())
        calc_label = st.selectbox("Consumo de bebidas alcoólicas", MAPA_CALC.keys())

    st.header("4️⃣ Estilo de Vida")
    col1, col2 = st.columns(2)

    with col1:
        faf_label = st.selectbox("Atividade física semanal", MAPA_FAF.keys())
        tue_label = st.selectbox("Tempo diário em telas", MAPA_TUE.keys())

    with col2:
        mtrans_label = st.selectbox("Meio de transporte", MAPA_MTRANS.keys())

    st.divider()
    submit = st.form_submit_button("🔍 Gerar avaliação de risco", use_container_width=True)

# =====================================================
# PROCESSAMENTO E RESULTADOS (FUNDO COLORIDO)
# =====================================================
if submit:

    # -----------------------------
    # Cálculo do IMC
    # -----------------------------
    imc = peso / (altura ** 2)

    # -----------------------------
    # Montagem do DataFrame
    # -----------------------------
    df = pd.DataFrame(0, index=[0], columns=COLUNAS_MODELO)
    df["idade"] = idade
    df["peso"] = peso
    df["altura"] = altura
    df["imc"] = imc
    df["frequencia_consumo_vegetais"] = MAPA_FCVC[fcvc_label]
    df["numero_refeicoes_por_dia"] = MAPA_NCP[ncp_label]
    df["consumo_diario_agua"] = MAPA_CH2O[ch2o_label]
    df["frequencia_atividade_fisica_semanal"] = MAPA_FAF[faf_label]
    df["tempo_dispositivos_eletronicos"] = MAPA_TUE[tue_label]

    if genero == "Masculino":
        df["genero_masculino"] = 1
    if historico == "Sim":
        df["historico_familiar_sim"] = 1
    if fuma == "Sim":
        df["fuma_sim"] = 1
    if caloricos == "Sim":
        df["consumo_alimentos_caloricos_sim"] = 1
    if monitora == "Sim":
        df["monitora_calorias_sim"] = 1

    df[f"come_entre_refeicoes_{MAPA_CAEC[caec_label]}"] = 1
    df[f"consumo_alcool_{MAPA_CALC[calc_label]}"] = 1
    df[f"meio_transporte_{MAPA_MTRANS[mtrans_label]}"] = 1

    df = df[COLUNAS_MODELO]

    # -----------------------------
    # Predição
    # -----------------------------
    resultado_bruto = modelo.predict(df)[0]
    nivel_modelo = MAPA_RESULTADO_MODELO.get(resultado_bruto, resultado_bruto)

    st.divider()

# =====================================================
# PROCESSAMENTO E RESULTADOS
# =====================================================
if submit:

    # -----------------------------
    # Cálculo do IMC
    # -----------------------------
    imc = peso / (altura ** 2)

    # -----------------------------
    # Montagem do DataFrame
    # -----------------------------
    df = pd.DataFrame(0, index=[0], columns=COLUNAS_MODELO)
    df["idade"] = idade
    df["peso"] = peso
    df["altura"] = altura
    df["imc"] = imc
    df["frequencia_consumo_vegetais"] = MAPA_FCVC[fcvc_label]
    df["numero_refeicoes_por_dia"] = MAPA_NCP[ncp_label]
    df["consumo_diario_agua"] = MAPA_CH2O[ch2o_label]
    df["frequencia_atividade_fisica_semanal"] = MAPA_FAF[faf_label]
    df["tempo_dispositivos_eletronicos"] = MAPA_TUE[tue_label]

    if genero == "Masculino":
        df["genero_masculino"] = 1
    if historico == "Sim":
        df["historico_familiar_sim"] = 1
    if fuma == "Sim":
        df["fuma_sim"] = 1
    if caloricos == "Sim":
        df["consumo_alimentos_caloricos_sim"] = 1
    if monitora == "Sim":
        df["monitora_calorias_sim"] = 1

    df[f"come_entre_refeicoes_{MAPA_CAEC[caec_label]}"] = 1
    df[f"consumo_alcool_{MAPA_CALC[calc_label]}"] = 1
    df[f"meio_transporte_{MAPA_MTRANS[mtrans_label]}"] = 1

    df = df[COLUNAS_MODELO]

    # -----------------------------
    # Predição
    # -----------------------------
    resultado_bruto = modelo.predict(df)[0]
    nivel_modelo = MAPA_RESULTADO_MODELO.get(resultado_bruto, resultado_bruto)

    st.divider()

    # =====================================================
    # TÍTULO CENTRALIZADO
    # =====================================================
    st.markdown(
        """
        <h3 style="text-align:center; margin-bottom:12px;">
        🧾 Resultado da Avaliação
        </h3>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # CAIXA DE RESULTADO
    # =====================================================
    if nivel_modelo == "Peso adequado":
        bg_color = "#E6F4EA"
        border_color = "#2E7D32"
        icon = "✅"
    else:
        bg_color = "#FDECEA"
        border_color = "#C62828"
        icon = "⚠️"

    st.markdown(
        f"""
        <div style="
            background-color:{bg_color};
            border-left:5px solid {border_color};
            padding:14px;
            border-radius:8px;
            margin-bottom:20px;
            text-align:center;
        ">
            <h4 style="margin:0; font-weight:600;">
                {icon} {nivel_modelo}
            </h4>
            <p style="margin-top:6px; font-size:13px; color:#444;">
                Classificação estimada por modelo preditivo de
                <b>Machine Learning</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # INDICADORES CLÍNICOS 
    # =====================================================
    st.markdown(
        "<h4 style='text-align:center;'>📊 Indicadores Clínicos</h4>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.metric(
                label="Índice de Massa Corporal (IMC)",
                value=f"{imc:.1f} kg/m²"
            )
            st.caption(
                "Classificação conforme diretrizes do Ministério da Saúde."
            )

    with col2:
        with st.container(border=True):
            st.markdown("**Perfil da Avaliação**")
            st.markdown(
                "- Dados clínicos e comportamentais\n"
                "- Hábitos alimentares\n"
                "- Estilo de vida\n"
                "- Modelo preditivo supervisionado"
            )

    # =====================================================
    # INSIGHTS CLÍNICOS
    # =====================================================
    st.markdown(
        "<h4 style='text-align:center; margin-top:24px;'>🩺 Insights Clínicos</h4>",
        unsafe_allow_html=True
    )

    with st.container(border=True):

        insight_exibido = False

        if imc < 18.5:
            st.markdown(
                "⚠ **IMC abaixo do recomendado**  \n"
                "Sugere-se avaliação clínica e nutricional."
            )
            insight_exibido = True

        if imc >= 25:
            st.markdown(
                "⚠ **IMC acima do recomendado**  \n"
                "Recomenda-se acompanhamento nutricional periódico."
            )
            insight_exibido = True

        if df["frequencia_atividade_fisica_semanal"].values[0] <= 1:
            st.markdown(
                "🏃 **Baixa atividade física**  \n"
                "Incentivar prática regular de exercícios."
            )
            insight_exibido = True

        if df.get("consumo_alimentos_caloricos_sim", 0).values[0] == 1:
            st.markdown(
                "🍔 **Consumo frequente de alimentos calóricos**  \n"
                "Orientação nutricional é recomendada."
            )
            insight_exibido = True

        if df.get("historico_familiar_sim", 0).values[0] == 1:
            st.markdown(
                "🧬 **Histórico familiar positivo**  \n"
                "Sugere-se acompanhamento preventivo."
            )
            insight_exibido = True

        if df["tempo_dispositivos_eletronicos"].values[0] >= 2:
            st.markdown(
                "📱 **Sedentarismo elevado**  \n"
                "Reduzir tempo sedentário e estimular movimentação."
            )
            insight_exibido = True

        if not insight_exibido:
            st.markdown(
                "✅ **Perfil associado a menor risco de obesidade**  \n"
                "Manter hábitos saudáveis e acompanhamento periódico."
            )

    # =====================================================
    # NOTA METODOLÓGICA
    # =====================================================
    with st.expander("ℹ️ Nota metodológica e limitações"):
        st.markdown(
            """
            Esta ferramenta utiliza um modelo de *Machine Learning* para **apoio à decisão clínica**.
            Não substitui avaliação médica ou nutricional individualizada.

            **Referência:**  
            Ministério da Saúde — Classificação do IMC  
            https://linhasdecuidado.saude.gov.br/portal/obesidade-no-adulto/
            """
        )
