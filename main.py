import pickle
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
import numpy as np
import pandas as pd
import streamlit as st

st.title("""
    Você tem probabilidade de doenças do coração?
Responda:
    """)

age = st.slider(label='Idade' ,min_value=12, max_value=110)
trestbps = st.slider(label='Pressao sanguinea' ,min_value=30, max_value=200)
chol = st.slider(label='Colesterol LDL' ,min_value=50, max_value=200)
thalach = st.slider(label='Maximo de batimentos cardiacas em repouso' ,min_value=30, max_value=200)
sex = st.radio(label='Sexo', options=['Feminino','Masculino'])
if sex == 'Feminino':
    sex_0 = 1
    sex_1 = 0
else:
    sex_0 = 0
    sex_1 = 1

cp = st.radio(label='Dor no peito', options=['Sinto dor no peito','Sinto muita dor no peito','Sem dor no peito','Assintomatico'])
if cp == 'Sinto dor no peito':
    cp_0 = 1
    cp_1 = 0
    cp_2 = 0
    cp_3 = 0
elif cp == 'Sinto muita dor no peito':
    cp_0 = 0
    cp_1 = 1
    cp_2 = 0
    cp_3 = 0
elif cp == 'Sem dor no peito':
    cp_0 = 0
    cp_1 = 0
    cp_2 = 1
    cp_3 = 0
else:
    cp_0 = 0
    cp_1 = 0
    cp_2 = 0
    cp_3 = 1

fbs = st.radio(label='Glicemia acima de 120mg/dl ?',options=['Sim','Não'])
if fbs == 'Sim':
    fbs_0 = 0
    fbs_1 = 1
else:
    fbs_0 = 1
    fbs_1 = 0

exang = st.radio(label='Sente dor no peito quando faz exercício?', options=['Sim', 'Não'])
if exang == 'Sim':
    exang_0 = 0
    exang_1 = 1
else:
    exang_0 = 1
    exang_1 = 0

TESTDATA = StringIO(f"""age;trestbps;chol;thalach;sex_0;sex_1;cp_0;cp_1;cp_2;cp_3;fbs_0;fbs_1;exang_0;exang_1
{age};{trestbps};{chol};{thalach};{sex_0};{sex_1};{cp_0};{cp_1};{cp_2};{cp_3};{fbs_0};{fbs_1};{exang_0};{exang_1}
    """)

df = pd.read_csv(TESTDATA, sep=";")

pkl_filename = "random_forest_model.pkl"
with open (pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

predict = pickle_model.predict_proba(np.array(df).reshape((1, -1)))
print(predict)

def resposta():
    if predict[0][1] > 0.5:
        container2.info(f"voce tem probabilidade de ter doenças do coração")
    else:
        container2.info(f"Você não tem probabilidade de ter doenças do coração")

st.button(label='Resposta', on_click=resposta)

container2 = st.container()
container2.write("Resultado:")