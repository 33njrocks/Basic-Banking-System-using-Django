from django.shortcuts import render
from .models import Customers,Transfer
from django.contrib import messages

all_customer_list=Customers.objects.all().order_by('id')

# Create your views here.
def customer(request):
    all_customer_list=Customers.objects.all().order_by('id')
    return render(request,"customer.html",{'custs':all_customer_list})

def history(request):
    transfer = Transfer.objects.all()

    return render(request,"history.html",{'transfer':transfer})


def profile(request, id):
    sender=Customers.objects.get(pk=id)
    if request.method=="POST":
        amount=request.POST['amount']
        value=request.POST['select']
        if (amount==""):
            messages.error(request,'Enter a valid amount')
        else:
            amount=float(amount)
            if value=='Select an option':
                messages.error(request,'Please select a customer')
            else:
                receiver=Customers.objects.get(id=value)
                if amount<sender.balance:
                    sender.balance = sender.balance-amount
                    receiver.balance = receiver.balance+amount
                    receiver.save()
                    sender.save()
                    transfered_amount = Transfer(sender=sender,receiver=receiver,transaction_amount=amount)
                    transfered_amount.save()
                    messages.success(request,'Amount Transferred Successfully')
                else:
                    messages.error(request,'Insufficient Balance')
    return render(request,"profile.html",{'customer_list':all_customer_list,'sender':sender})

