from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "POST":
        loam_amount = request.POST.get("loan_amount")
        marital_status = request.POST.get("marital_status")
        dependents = request.POST.get("dependents")
        education = request.POST.get("education")
        employement_status = request.POST.get("employement_status")
        credit_history = request.POST.get("credit_history")
        applicant_income = request.POST.get("applicant_income")
        loan_amount_term = request.POST.get("loan_amount_term")
        property_area = request.POST.get("property_area") 
        print(property_area)
    return render(request, 'index.html')
