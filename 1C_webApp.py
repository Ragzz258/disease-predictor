from select import select
from flask import Flask
from pywebio.input import *
from pywebio.output import *
from pywebio.output import put_text 
from pywebio import start_server
import pandas as pd
import pickle

sd = pd.read_csv('data\symptom_Description.csv')
sp = pd.read_csv('data\symptom_precaution.csv')

with open('code\DecisionTree.pkl','rb') as f:
    mp  = pickle.load(f)

app = Flask(__name__)

def predict():
    All_Symptoms = ['none','itching', ' skin_rash', ' nodal_skin_eruptions',
       ' dischromic _patches', ' continuous_sneezing', ' shivering',
       ' chills', ' watering_from_eyes', ' stomach_pain', ' acidity',
       ' ulcers_on_tongue', ' vomiting', ' cough', ' chest_pain',
       ' yellowish_skin', ' nausea', ' loss_of_appetite',
       ' abdominal_pain', ' yellowing_of_eyes', ' burning_micturition',
       ' spotting_ urination', ' passage_of_gases', ' internal_itching',
       ' indigestion', ' muscle_wasting', ' patches_in_throat',
       ' high_fever', ' extra_marital_contacts', ' fatigue',
       ' weight_loss', ' restlessness', ' lethargy',
       ' irregular_sugar_level', ' blurred_and_distorted_vision',
       ' obesity', ' excessive_hunger', ' increased_appetite',
       ' polyuria', ' sunken_eyes', ' dehydration', ' diarrhoea',
       ' breathlessness', ' family_history', ' mucoid_sputum',
       ' headache', ' dizziness', ' loss_of_balance',
       ' lack_of_concentration', ' stiff_neck', ' depression',
       ' irritability', ' visual_disturbances', ' back_pain',
       ' weakness_in_limbs', ' neck_pain', ' weakness_of_one_body_side',
       ' altered_sensorium', ' dark_urine', ' sweating', ' muscle_pain',
       ' mild_fever', ' swelled_lymph_nodes', ' malaise',
       ' red_spots_over_body', ' joint_pain', ' pain_behind_the_eyes',
       ' constipation', ' toxic_look_(typhos)', ' belly_pain',
       ' yellow_urine', ' receiving_blood_transfusion',
       ' receiving_unsterile_injections', ' coma', ' stomach_bleeding',
       ' acute_liver_failure', ' swelling_of_stomach',
       ' distention_of_abdomen', ' history_of_alcohol_consumption',
       ' fluid_overload', ' phlegm', ' blood_in_sputum',
       ' throat_irritation', ' redness_of_eyes', ' sinus_pressure',
       ' runny_nose', ' congestion', ' loss_of_smell', ' fast_heart_rate',
       ' rusty_sputum', ' pain_during_bowel_movements',
       ' pain_in_anal_region', ' bloody_stool', ' irritation_in_anus',
       ' cramps', ' bruising', ' swollen_legs', ' swollen_blood_vessels',
       ' prominent_veins_on_calf', ' weight_gain',
       ' cold_hands_and_feets', ' mood_swings', ' puffy_face_and_eyes',
       ' enlarged_thyroid', ' brittle_nails', ' swollen_extremeties',
       ' abnormal_menstruation', ' muscle_weakness', ' anxiety',
       ' slurred_speech', ' palpitations', ' drying_and_tingling_lips',
       ' knee_pain', ' hip_joint_pain', ' swelling_joints',
       ' painful_walking', ' movement_stiffness', ' spinning_movements',
       ' unsteadiness', ' pus_filled_pimples', ' blackheads', ' scurring',
       ' bladder_discomfort', ' foul_smell_of urine',
       ' continuous_feel_of_urine', ' skin_peeling',
       ' silver_like_dusting', ' small_dents_in_nails',
       ' inflammatory_nails', ' blister', ' red_sore_around_nose',
       ' yellow_crust_ooze']

    s  = [ ]

    for i in range(1,18):
        Symptom1 = select('symptom'+str(i),All_Symptoms,name = f's{i}')
        s.append(Symptom1)

    s = input_group('Select the Symptoms you have',s)
    s= list(s.values())

    for i in range(len(All_Symptoms)):
        if All_Symptoms[i] in s:
            All_Symptoms[i] = 1
        else: 
            All_Symptoms[i] = 0  

    All_Symptoms = pd.DataFrame(All_Symptoms).T  
   
    prediction =  mp.predict(All_Symptoms)
   
    put_html("<h2 style = 'color:blue'>You might have :</h2> ")

    put_html(f"<p style = 'color:red;font-size: 50px'>{prediction[0]}</p> ")

    put_column([put_html("<h2>Disease description:</h2> "),put_html(list(sd[sd['Disease'] == prediction[0]]['Description'])[0])])
            
    put_html("<h2 style='color:green'>Precautions to take:</h2>")

    x=[]
    for i in range(1,5):
        x.append(put_text(str(list(sp[sp['Disease'] == prediction[0]]['Precaution_'+str(i)])[0])))

    put_column(x)

    put_html('<a href="/" style="font-size:30px;background-color:black;margin-left:380px;color:white">Return</a>') 

if __name__ == '__main__':
    start_server(predict, port=8000, debug=True)