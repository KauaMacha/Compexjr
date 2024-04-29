import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

class Dashboards:
    def __init__(self, market_df):
        self.market_df = market_df
        self.cores = ['#1f77b4', '#aec7e8', '#d62728']

    def fatura_por_dia(self):
        faturamento_por_dia_filial = self.market_df.pivot_table(index='Date', columns='Branch', values='cogs', aggfunc='sum')
        cores_filial = {'A': '#1f77b4', 'B': '#aec7e8', 'C': '#d62728'}
        chart_data = pd.DataFrame()
        for filial, cor in cores_filial.items():
            chart_data[f'Filial {filial}'] = faturamento_por_dia_filial[filial]

        st.title('Faturamento por Dia')
        st.line_chart(chart_data, use_container_width=True)

    def fatura_por_produto(self):
        faturamento_por_produto = self.market_df.groupby('Product line')['cogs'].sum().sort_values(ascending=False)
        st.title('Faturamento por Tipo de Produto')
        fig, ax = plt.subplots()
        faturamento_por_produto.plot(kind='bar', ax=ax, color=self.cores[0])
        plt.xlabel('Tipo de Produto')
        plt.ylabel('Faturamento')
        st.pyplot(fig)

    def fatura_por_filial(self):
        faturamento_por_filial = self.market_df.groupby('Branch')['cogs'].sum()
        st.title('Faturamento por Filial')
        fig, ax = plt.subplots()
        faturamento_por_filial.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=self.cores)
        plt.ylabel('')
        st.pyplot(fig)

    def fatura_por_pagamento(self):
        faturamento_por_pagamento = self.market_df.groupby('Payment')['cogs'].sum()
        st.title('Faturamento por Tipo de Pagamento')
        fig, ax = plt.subplots()
        faturamento_por_pagamento.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=self.cores)
        plt.ylabel('')
        st.pyplot(fig)

    def avaliacao_filial(self):
        avaliacao_por_filial = self.market_df.groupby('Branch')['Rating'].mean()
        st.title('Avaliações das Filiais')
        fig, ax = plt.subplots()
        avaliacao_por_filial.plot(kind='bar', ax=ax, color=self.cores)
        plt.xlabel('Filial')
        plt.ylabel('Avaliação')
        ax.set_ylim(0, 10)  
        st.pyplot(fig)
