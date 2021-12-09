from django.shortcuts import render
from .helpers import *
import pandas as pd
# Create your views here.



def index(request):
    if request.method == "POST":

        gender = request.POST.get("gender")
        loan_amount = request.POST.get("loan_amount")
        marital_status = request.POST.get("marital_status")
        dependents = request.POST.get("dependents")
        education = request.POST.get("education")
        employement_status = request.POST.get("employement_status")
        credit_history = request.POST.get("credit_history")
        applicant_income = request.POST.get("applicant_income")
        co_applicant_income = request.POST.get("co_applicant_income")
        loan_amount_term = request.POST.get("loan_amount_term")
        property_area = request.POST.get("property_area")
        
        

        applicant_income = float(applicant_income)**(1./3.)

        co_applicant_income = float(co_applicant_income)**(1./3.)

        loan_amount = float(loan_amount)**(1./3.)

        gender = float(gender_dict[gender])

        dependents = float(dependents_dict[dependents])

        education = float(education_dict[education])

        credit_history = float(credit_history_dict[credit_history])

        employement_status = float(self_employed_dict[employement_status])

        marital_status = float(married_dict[marital_status])

        property_area = float(property_dict[property_area])

        x_test = {"Gender":gender,
        "Married":marital_status,
         "Dependents":dependents,
         "Education":education,
         "Self_Employed":employement_status,
         "ApplicantIncome":applicant_income,
         "CoapplicantIncome":co_applicant_income,
         "LoanAmount":loan_amount,
         "Loan_Amount_Term":loan_amount_term,
         "Credit_History":credit_history,
         "Property_Area":property_area}

        test_df = pd.DataFrame([x_test])

        loan_status = model.predict(scaler.transform(test_df))[0]

        if loan_status == 1:
            loan_status = "Approved"
            image = "loan-approved.jpg"
        else:
            loan_status = "Denied"
            image = "loan-denied.jpg"
            
        context = {"loan_status":loan_status,
                    "loan_image":image}
        return render(request, 'index.html', context)
    return render(request, "index.html")
