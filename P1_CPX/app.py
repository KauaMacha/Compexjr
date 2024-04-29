import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dashboards import Dashboards

class App:
    def __init__(self, market_df):
        self.market_df = market_df
        self.dashboards = Dashboards(market_df)

    def run(self):
        st.sidebar.title('Opções de Visualização')
        opcao = st.sidebar.radio('Escolha uma opção:', ('Todos os Dashboards', 'Faturamento por Dia', 'Faturamento por Tipo de Produto', 'Faturamento por Filial', 'Faturamento por Tipo de Pagamento', 'Avaliações das Filiais'))

        if opcao == 'Todos os Dashboards':
            self.dashboards.fatura_por_dia()
            col1, col2 = st.columns(2)
            with col1:
                self.dashboards.fatura_por_produto()
                self.dashboards.fatura_por_pagamento()
            with col2:
                self.dashboards.fatura_por_filial()
                self.dashboards.avaliacao_filial()

            
        elif opcao == 'Faturamento por Dia':
            self.dashboards.fatura_por_dia()
            self.mostrar_valores('Faturamento por Dia')
        elif opcao == 'Faturamento por Tipo de Produto':
            self.dashboards.fatura_por_produto()
            self.mostrar_valores('Faturamento por Tipo de Produto')
        elif opcao == 'Faturamento por Filial':
            self.dashboards.fatura_por_filial()
            self.mostrar_valores('Faturamento por Filial')
        elif opcao == 'Faturamento por Tipo de Pagamento':
            self.dashboards.fatura_por_pagamento()
            self.mostrar_valores('Faturamento por Tipo de Pagamento')
        elif opcao == 'Avaliações das Filiais':
            self.dashboards.avaliacao_filial()
            self.mostrar_valores('Avaliações das Filiais')

    def mostrar_valores(self, titulo):
        st.subheader('Tabela Valores:')
        estilo_tabela = [
            {'selector': 'thead th', 'props': [('background-color', '#0077b6'), ('color', 'white'), ('border', 'none')]},  # Estilo para cabeçalhos
            {'selector': 'tbody tr:nth-of-type(odd)', 'props': [('background-color', '#f0f0f0')]},  # Estilo para linhas ímpares
            {'selector': 'tbody tr:hover', 'props': [('background-color', '#ddd')]}  # Estilo para linhas ao passar o mouse
        ]
        if titulo == 'Faturamento por Dia':
            dados = self.market_df.groupby('Date')['cogs'].sum().reset_index()
        elif titulo == 'Faturamento por Tipo de Produto':
            dados = self.market_df.groupby('Product line')['cogs'].sum().reset_index()
        elif titulo == 'Faturamento por Filial':
            dados = self.market_df.groupby('Branch')['cogs'].sum().reset_index()
        elif titulo == 'Faturamento por Tipo de Pagamento':
            dados = self.market_df.groupby('Payment')['cogs'].sum().reset_index()
        elif titulo == 'Avaliações das Filiais':
            dados = self.market_df.groupby('Branch')['Rating'].mean().reset_index()
        st.table(dados.style.set_table_styles(estilo_tabela))


def main():
    market_df = pd.read_csv('P1_CPX/supermarket_sales.csv', sep=';')
    market_df['cogs'] = market_df['cogs'].str.replace(',', '.').astype(float)
    market_df['Rating'] = market_df['Rating'].str.replace(',', '.').astype(float)

    app = App(market_df)
    app.run()

if __name__ == "__main__":
    main()
