import pandas as pd
import scipy.stats
import streamlit as st
import time

estas são variáveis persistentes preservadas à medida que o Streamlin executa novamente esse script
import streamlit as st
import numpy as np
import pandas as pd

st.title('Simulação de lançamento de moedas')

number_of_trials = st.slider(
    'Número de lançamentos:',
    10, 10000, 100
)

def toss_coin(number_of_trials):
    results = np.random.choice([0, 1], size=number_of_trials)

    means = np.cumsum(results) / np.arange(1, number_of_trials + 1)

    return means

mean = toss_coin(number_of_trials)

df = pd.DataFrame({
    'Média acumulada': mean
})

st.line_chart(df)

def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]],
                     columns=['no', 'iterations', 'mean'])
        ],
        axis=0)
    st.session_state['df_experiment_results'] = \
        st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])