"""
Nome do Projeto: Projeto #1 Compex - dashboard Supermercado

Descrição: 
    O projeto consiste em criar um dashboard para um supermercado fictício. 
    O dashboard deve conter as seguintes informações:
    - Faturamento por dia
    - Faturamento por tipo de produto
    - Faturamento por filial
    - Faturamento por tipo de pagamento
    - Avaliações das filiais

Autores:
- Pedro Feitosa
- Kauã Machado
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

marketDf = pd.read_csv('P1_CPX/supermarket_sales.csv', sep=';')

marketDf['cogs'] = marketDf['cogs'].str.replace(',', '.').astype(float)
marketDf['Rating'] = marketDf['Rating'].str.replace(',', '.').astype(float)

# Cores de referência
cores = ['#1f77b4', '#aec7e8', '#d62728']

 # 1 - Faturamento por dia (Gráfico de Linhas)
def fatura_por_dia():  
    faturamento_por_dia_filial = marketDf.pivot_table(index='Date', columns='Branch', values='cogs', aggfunc='sum')

    cores_filial = {'A': '#1f77b4', 'B': '#aec7e8', 'C': '#d62728'}
    chart_data = pd.DataFrame()
    for filial, cor in cores_filial.items():
        chart_data[f'Filial {filial}'] = faturamento_por_dia_filial[filial]

    st.title('Faturamento por Dia')
    st.line_chart(chart_data, use_container_width=True)
  
# 2 - Faturamento por tipo de produto (Gráfico de Colunas)
def fatura_por_produto(): 
    faturamento_por_produto = marketDf.groupby('Product line')['cogs'].sum().sort_values(ascending=False)
    st.title('Faturamento por Tipo de Produto')
    fig, ax = plt.subplots()
    faturamento_por_produto.plot(kind='bar', ax=ax, color=cores[0])
    plt.xlabel('Tipo de Produto')
    plt.ylabel('Faturamento')
    st.pyplot(fig)

#  3 -Faturamento por filial (Gráfico de Pizza)
def fatura_por_filial():
    faturamento_por_filial = marketDf.groupby('Branch')['cogs'].sum()
    st.title('Faturamento por Filial')
    fig, ax = plt.subplots()
    faturamento_por_filial.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=cores)
    plt.ylabel('')
    st.pyplot(fig)

#  4 -Faturamento por tipo de pagamento (Gráfico de Pizza)
def fatura_por_pagamento():
    
    faturamento_por_pagamento = marketDf.groupby('Payment')['cogs'].sum()
    st.title('Faturamento por Tipo de Pagamento')
    fig, ax = plt.subplots()
    faturamento_por_pagamento.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=cores)
    plt.ylabel('')
    st.pyplot(fig)
    
#  5 - Avaliações das filiais (Gráfico de Colunas)
def avaliacao_filial():
    avaliacao_por_filial = marketDf.groupby('Branch')['Rating'].mean()
    st.title('Avaliações das Filiais')
    fig, ax = plt.subplots()
    avaliacao_por_filial.plot(kind='bar', ax=ax, color=cores)
    plt.xlabel('Filial')
    plt.ylabel('Avaliação')
    ax.set_ylim(0, 10)  
    st.pyplot(fig)
    
# Função para plotar os dashboards individualmente
def plot_individual_dashboards():
    fatura_por_dia()
    fatura_por_produto()
    fatura_por_filial()
    fatura_por_pagamento()
    avaliacao_filial()

# Criando o menu lateral
st.sidebar.title('Opções de Visualização')
opcao = st.sidebar.radio('Escolha uma opção:', ('Todos os Dashboards', 'Faturamento por Dia', 'Faturamento por Tipo de Produto', 'Faturamento por Filial', 'Faturamento por Tipo de Pagamento', 'Avaliações das Filiais'))

# Mostrando os dashboards com base na opção selecionada
if opcao == 'Todos os Dashboards':
    plot_individual_dashboards()
elif opcao == 'Faturamento por Dia':
    fatura_por_dia()
elif opcao == 'Faturamento por Tipo de Produto':
    fatura_por_produto()
elif opcao == 'Faturamento por Filial':
    fatura_por_filial()
elif opcao == 'Faturamento por Tipo de Pagamento':
    fatura_por_pagamento()
elif opcao == 'Avaliações das Filiais':
    avaliacao_filial()