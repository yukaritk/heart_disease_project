import pickle
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
import numpy as np
import pandas as pd

print("digite sua idade:")
age = float(input())

TESTDATA = StringIO(f"""age;trestbps;chol;thalach;sex_0;sex_1;cp_0;cp_1;cp_2;cp_3;fbs_0;fbs_1;exang_0;exang_1
{age};125;136;95;1;0;0;0;0;1;1;0;1;0
    """)

df = pd.read_csv(TESTDATA, sep=";")

pkl_filename = "random_forest_model.pkl"
with open (pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

predict = pickle_model.predict_proba(np.array(df).reshape((1, -1)))

if predict[0][0] > 0.5 :
    print(f"voce nao tem chance de ter ataque cardiaco {predict[0][0] * 100:.2f}%")
else:
    print(f"voce tem chance de ter ataque cardiaco {predict[0][1] * 100:.2f}%")