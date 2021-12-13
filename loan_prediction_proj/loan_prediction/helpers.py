import joblib
import os

model = joblib.load('loan_prediction/model/loan.obj')

scaler = joblib.load('loan_prediction/model/scaler.obj')

property_dict = {"Rural":0,"Urban":2,"Semi urban":1}

credit_history_dict = {"1":1,"0":0}

dependents_dict = {"0":0,"1":1,"2":2,"3+":3}

self_employed_dict = {"True":1,"False":0}

married_dict = {"Married":1,"Single":0}

gender_dict = {"Male":1,"Female":0}

education_dict = {"Graduate":0, "Not Graduate":1}