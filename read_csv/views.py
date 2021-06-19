from django.shortcuts import render
from .form import csvform
from django .contrib.auth.models import User
from .models import csvs
from product.models import Product, Purchase
import csv
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def upload_file_view(request):
    error=None
    success_message=None
    form=csvform(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        form.save()
        form=csvform()
        try:
                obj= csvs.objects.get(activated=False)
                with open(obj.csv_file.path,'r') as f:
                    reader=csv.reader(f)

                    for row in reader:
                        
                        
                        user=User.objects.get(id=row[3])
                        prod,_=Product.objects.get_or_create(name=row[0])
                        Purchase.objects.create(
                            product=prod,
                            price=int(row[2]),
                            quantity=int(row[1]),
                            date=row[4]+" "+row[5],
                            salesman=user,

                        )
                obj.activated=True
                obj.save()
                success_message="Upload File Sucessfully"
        except:
            error="Oops, Something Want Wrong"

     
    context={
        'file':form,
        'error':error,
        'success_message':success_message
    }
    return render(request,'read_csv/upload.html',context)