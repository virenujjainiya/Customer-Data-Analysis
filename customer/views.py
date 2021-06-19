from django.shortcuts import render
# Create your views here.
from .models import Customer
import matplotlib.pyplot as plt
import seaborn as sbn
from product.utils import get_image
import pandas as pd
from django.contrib.auth.decorators import login_required
from .form import customer_register

@login_required
def customer_view(request):
    

    cust=Customer.objects.all().values()
    cust_df=pd.DataFrame(cust)
    correlation=round(cust_df['budget'].corr(cust_df['employment']),2)
   
    
    plt.switch_backend('AGG')
    plt.subplots(figsize=(10,6))
    sbn.regplot(x='budget',y='employment',data=cust_df)
    plt.tight_layout()
    

    graph=get_image()

    context={
        'customer':cust_df.to_html,
        'correlation':correlation,
        'graph':graph,
       
    }
    return render(request,'customer/customer.html',context)

def customer_regi(request):
    add_message=None
    error_message=None
    form=customer_register(request.POST or None)
    if request.method=="POST":
        form=customer_register(request.POST)
        if form.is_valid():
            form.save()
            form()
            add_message="Record has been saved"
        else:
            error_message="Invalid details"
    else:
        form=customer_register()
        
    context={
         'form':form,
         'add_message':add_message,
         'error_message':error_message,
    }
    return render(request,'customer/addcustomer.html',context)
