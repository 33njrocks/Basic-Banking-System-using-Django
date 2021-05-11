from django.shortcuts import render
from banking.models import Customers

# Create your views here.
def index(request):
    customer_list = Customers.objects.all()
    return render(request,"index.html",{'customer_list':customer_list})

