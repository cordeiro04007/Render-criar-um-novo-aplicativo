import streamlit as st
import numpy as np
import pandas as pd

# Inicialização das variáveis
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame()

st.title('Simulação de lançamento de moedas')

number_of_trials = st.slider(
    'Número de lançamentos:',
    10, 10000, 100
)

def toss_coin(number_of_trials):
    results = np.random.choice([0, 1], size=number_of_trials)

    mean = np.cumsum(results) / np.arange(1, number_of_trials + 1)

    return mean

mean = toss_coin(number_of_trials)

df = pd.DataFrame({
    'Média acumulada': mean,
    'Probabilidade teórica': 0.5
})

st.line_chart(df)

if st.button('Executar experimento'):
    st.session_state['experiment_no'] += 1

    st.session_state['df_experiment_results'] = pd.concat(
        [
            st.session_state['df_experiment_results'],
            pd.DataFrame({
                'Experimento': [st.session_state['experiment_no']],
                'Média final': [mean[-1]]
            })
        ],
        ignore_index=True
    )

st.subheader('Resultados dos experimentos')

st.write(st.session_state['df_experiment_results'])