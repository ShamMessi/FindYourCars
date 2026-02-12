from django.views.generic import ListView, DetailView,TemplateView,CreateView,UpdateView,DeleteView
from .models import Company, Product
from django.urls import reverse_lazy
from Holeapp.form import EMIFORM
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
import math



class All_details(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = "good"


class Company_Detail(DetailView):
    model = Company
    template_name = 'product_detail.html'
    context_object_name = 'company'



class HomeView(TemplateView):
    template_name = 'home.html'


class AddCompanyView(CreateView):
    model = Company
    fields='__all__'
    template_name='company_form.html'
    success_url = reverse_lazy("company_list")



class Add_product(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = reverse_lazy('company_detail')



from django.views.generic import DetailView

class CompanyUpdate(UpdateView):
    model=Company
    fields=['name','ceo','logo']
    template_name='company_form.html'
    success_url = reverse_lazy("company_list")



class Delete_company(DeleteView):
   model=Company 
   success_url=reverse_lazy("company_list")
   template_name='company_confirm_delete.html'



def emi_calculater(request, id):
    product = get_object_or_404(Product, id=id)

    error = None
    loan_error = None
    emi = None
    loan_amount = None
    tenure = None

    annual_interest = 12  # %

    if request.method == "POST":
        tenure = int(request.POST.get("tenure", 0))
        loan_amount = int(request.POST.get("loan_amount", 0))

        if tenure <= 0:
            error = "Tenure must be greater than 0 months"

        elif loan_amount <= 0:
            loan_error = "Loan amount must be greater than 0"

        elif loan_amount > product.price:
            loan_error = "Loan amount cannot be greater than product price"

        else:
            # EMI CALCULATION
            P = loan_amount
            R = annual_interest / (12 * 100)
            N = tenure

            emi = (P * R * math.pow(1 + R, N)) / (math.pow(1 + R, N) - 1)
            emi = round(emi, 2)

    return render(request, "emi_calculator.html", {
        "product": product,
        "error": error,
        "loan_error": loan_error,
        "emi": emi,
        "loan_amount": loan_amount,
        "tenure": tenure,
        "interest": annual_interest
    })



