import pandas as pd
import streamlit as st

marketDf = pd.read_csv('P1_CPX/supermarket_sales.csv',sep = ';')


# 1 - Faturamento por dia

colunas = ['cogs','Date']

marketDf['cogs'] = marketDf['cogs'].str.replace(',', '.').astype(float) #Tive que fazer isso, o pandas estava concatenando os valores ao invés de somar
marketDf['cogs'] = pd.to_numeric(marketDf['cogs']) 

faturamento_por_dia = marketDf[colunas].groupby('Date').sum()

st.title('Faturamento por Dia')
st.line_chart(faturamento_por_dia)

# 2 - Faturamento por tipo de produto

colunas = ['cogs','Product line']
faturamento_por_produto = marketDf[colunas].groupby('Product line').sum()

st.title('Faturamento por tipo de produto')
st.line_chart(faturamento_por_produto)

# 3 - Faturamento por filial

colunas = ['cogs','Branch']
faturamento_por_filial = marketDf[colunas].groupby('Branch').sum()

st.title('Faturamento por filial')
st.line_chart(faturamento_por_filial)

# 4 - Faturamento por tipo de pagamento

colunas = ['cogs','Payment']
faturamento_por_Payment = marketDf[colunas].groupby('Payment').sum()

st.title('Faturamento por tipo de pagamento')
st.line_chart(faturamento_por_Payment)

# 5 - Avaliações das filiais

marketDf['Rating'] = marketDf['Rating'].str.replace(',', '.').astype(float)

colunas = ['Branch','Rating']
avaliação_por_filial = marketDf[colunas].groupby('Branch').sum()

st.title('Avaliações das filiais')
st.line_chart(avaliação_por_filial)