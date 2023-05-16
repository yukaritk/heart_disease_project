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
    """)

Age = st.slider(label='Idade (anos)' ,min_value=12, max_value=110)
RestingBP = st.slider(label='Pressao arterial em repouso (mm/Hg)' ,min_value=0, max_value=200)
Cholesterol = st.slider(label='Colesterol Sérico (LDL)' ,min_value=0, max_value=384)
MaxHR = st.slider(label='Frequência cardíaca máxima alcançada' ,min_value=60, max_value=202)
Sex = st.radio(label='Sexo', options=['Feminino','Masculino'])
if Sex == 'Feminino':
    Sex_F = 1
    Sex_M = 0
else:
    Sex_F = 0
    Sex_M = 1

cp = st.radio(label='Dor no peito', options=['Tipica dor no peito','Atipica dor no peito','Sem dor no peito','Assintomatico'])
if cp == 'Tipica dor no peito':
    ChestPainType_ASY = 0
    ChestPainType_ATA = 0
    ChestPainType_NAP = 0
    ChestPainType_TA = 1
elif cp == 'Atipica dor no peito':
    ChestPainType_ASY = 0
    ChestPainType_ATA = 1
    ChestPainType_NAP = 0
    ChestPainType_TA = 0
elif cp == 'Sem dor no peito':
    ChestPainType_ASY = 0
    ChestPainType_ATA = 0
    ChestPainType_NAP = 1
    ChestPainType_TA = 0
else:
    ChestPainType_ASY = 1
    ChestPainType_ATA = 0
    ChestPainType_NAP = 0
    ChestPainType_TA = 0


fbs = st.radio(label='Glicose em jejum esta acima de 120mg/dl ?',options=['Sim','Não'])
if fbs == 'Sim':
    FastingBS_0 = 0
    FastingBS_1 = 1
else:
    FastingBS_0 = 1
    FastingBS_1 = 0


exang = st.radio(label='Sente dor no peito quando faz exercício?', options=['Sim', 'Não'])
if exang == 'Sim':
    ExerciseAngina_N = 0
    ExerciseAngina_Y = 1
else:
    ExerciseAngina_N = 1
    ExerciseAngina_Y = 0


ecg = st.radio(label = 'Resultado do eletrocardiograma em repouso', options=['Normal','Anormalidade da onda ST-T','Mostrando hipertrofia ventricular'])
if ecg == 'Normal':
    RestingECG_LVH = 0
    RestingECG_Normal = 1
    RestingECG_ST = 0
elif ecg == 'Anormalidade da onda ST-T':
    RestingECG_LVH = 0
    RestingECG_Normal = 0
    RestingECG_ST = 1
else:
    RestingECG_LVH = 1
    RestingECG_Normal = 0
    RestingECG_ST = 0

TESTDATA = StringIO(f"""Age;RestingBP;Cholesterol;MaxHR;Sex_F;Sex_M;ChestPainType_ASY;ChestPainType_ATA;ChestPainType_NAP;ChestPainType_TA;FastingBS_0;FastingBS_1;RestingECG_LVH;RestingECG_Normal;RestingECG_ST;ExerciseAngina_N;ExerciseAngina_Y
{Age};{RestingBP};{Cholesterol};{MaxHR};{Sex_F};{Sex_M};{ChestPainType_ASY};{ChestPainType_ATA};{ChestPainType_NAP};{ChestPainType_TA};{FastingBS_0};{FastingBS_1};{RestingECG_LVH};{RestingECG_Normal};{RestingECG_ST};{ExerciseAngina_N};{ExerciseAngina_Y}
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