# 📊 FIAP Tech Challenge – Fase 4  
## Predição de Obesidade com Machine Learning e Streamlit

Este repositório contém a solução desenvolvida para o **Tech Challenge – Fase 4** da Pós-Tech em **Data Analytics** da FIAP.  
O projeto consiste no desenvolvimento de um **modelo de Machine Learning** capaz de prever o nível de obesidade de um paciente, além do **deploy do modelo em uma aplicação interativa utilizando Streamlit**, com uma visão analítica integrada.

---

## 🧠 Contexto do Problema

A obesidade é uma condição médica caracterizada pelo acúmulo excessivo de gordura corporal, podendo causar diversos impactos negativos à saúde, como doenças cardiovasculares, diabetes e hipertensão.

Diante desse cenário, o desafio proposto consiste em desenvolver uma solução preditiva que auxilie **equipes médicas e gestores de saúde** na identificação de pacientes com maior risco de obesidade, contribuindo para ações preventivas e decisões clínicas mais assertivas.

---

## 🎯 Objetivo do Projeto

- Desenvolver um **modelo de Machine Learning** para classificar o nível de obesidade de indivíduos  
- Criar um **sistema preditivo acessível** por meio de uma aplicação web  
- Gerar **insights analíticos** a partir dos dados para apoiar a tomada de decisão da equipe médica  

---

## 📊 Base de Dados

O projeto utiliza a base de dados `obesity.csv`, que contém informações demográficas, físicas e comportamentais dos indivíduos, tais como:

- Gênero e idade  
- Altura e peso  
- Hábitos alimentares  
- Consumo de água e álcool  
- Frequência de atividade física  
- Histórico familiar de sobrepeso  

A variável alvo é o **nível de obesidade** do indivíduo.

---

## 🧩 Solução Desenvolvida

A solução contempla:

✔️ Análise exploratória dos dados  
✔️ Etapas de **feature engineering** e preparação dos dados  
✔️ Treinamento de modelo de Machine Learning com acurácia superior a 75%  
✔️ Deploy do modelo em uma aplicação interativa com **Streamlit**  
✔️ Dashboard analítico com principais insights sobre obesidade  

---

## 🚀 Aplicação em Produção (Deploy) - Streamlit

A aplicação foi publicada no **Streamlit Cloud** e pode ser acessada no link abaixo:

👉 **Acesse o app:**  
https://fiaptech-challenge-fase4-2026.streamlit.app/

Na aplicação, é possível:
- Inserir dados de um paciente  
- Obter a predição do nível de obesidade  
- Visualizar análises e insights sobre os dados  

---

## 📊 Visão Analítica (Dashboard)

O projeto também apresenta uma **visão analítica integrada**, com gráficos e análises que permitem identificar padrões relevantes, como:

- Distribuição dos níveis de obesidade  
- Relação entre atividade física e obesidade  
- Influência dos hábitos alimentares nos níveis de obesidade  

Esses insights auxiliam a equipe médica na compreensão dos fatores associados à obesidade e no planejamento de estratégias preventivas.

---

## 🗂️ Estrutura do Repositório
'''
fiap-tech-challenge-fase4-obesidade/
│
├── app/
│   └── app.py
│       # Aplicação Streamlit responsável pela interface do usuário
│       # Permite a predição do nível de obesidade e exibição de insights
│
├── data/
│   └── Obesity.csv
│       # Dataset original utilizado para análise e modelagem
│
├── models/
│   └── modelo_obesidade.pkl
│       # Modelo de Machine Learning treinado e serializado
│       # Utilizado pela aplicação Streamlit para inferência
│
├── notebooks/
│   └── analise_obesidade.ipynb
│       # Notebook com análise exploratória, tratamento de dados,
│       # criação de features (IMC), comparação de modelos e validação
│
├── requirements.txt
│   # Lista de dependências necessárias para executar o projeto
│
└── README.md
    # Documentação geral do projeto
'''

## ⚙️ Tecnologias Utilizadas
- Python
- Pandas e NumPy
- Scikit-learn
- Streamlit
- Git e GitHub
- Streamlit Cloud (deploy)


## 🧮 Metodologia

### 1. Pré-processamento dos Dados

Nesta etapa, os dados foram preparados para garantir qualidade e compatibilidade com os modelos de Machine Learning. As principais atividades realizadas foram:

- Tratamento e limpeza dos dados  
- Codificação das variáveis categóricas  
- Normalização e padronização das variáveis numéricas  
- Feature Engineering  

---

### 2. Modelagem

Após o pré-processamento, foram avaliados diferentes algoritmos de Machine Learning para a tarefa de classificação do nível de obesidade.

**Modelos testados:**
- Random Forest *(modelo final escolhido)*  
- Logistic Regression  

**Métricas avaliadas:**
- Acurácia  
- F1-Score  
- Matriz de confusão  

O modelo **Random Forest** apresentou o melhor desempenho geral, atingindo acurácia superior a 75%, sendo selecionado como modelo final.

---

### 3. Deploy

O modelo treinado foi disponibilizado em um ambiente de produção, garantindo acessibilidade e reprodutibilidade da solução.

- Aplicação web desenvolvida com Streamlit  
- Modelo versionado e persistido em arquivo `.joblib`  
- Ambiente reproduzível com controle de dependências via `requirements.txt`  
- Deploy realizado no Streamlit Cloud  

## 👨‍💻 Grupo - Grupo 203
Viviane Barbosa

Obrigada por visitar o meu projeto! 🎉

