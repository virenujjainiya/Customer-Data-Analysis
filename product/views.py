
from django.shortcuts import render
from .models import Product,Purchase
import pandas as pd
from .utils import get_image, get_simple_plot,get_user_name
from .form import Purchaseform
import matplotlib.pyplot as plt
import seaborn as sbn
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def sales_dist_views(request):
    df=pd.DataFrame(Purchase.objects.all().values())
   
    df['salesman_id']=df['salesman_id'].apply(get_user_name)
    df.rename({'salesman_id':'salesman'},axis=1,inplace=True)
    df['date']=df['date'].apply(lambda x : x.strftime('%Y-%m-%d'))
   
    plt.switch_backend('AGG')
    plt.xticks(rotation=45)
    sbn.barplot(x='date',y='total_price',hue='salesman', data=df)
    plt.tight_layout()
    graph=get_image()

    return render(request,'product/sales.html',{'graph':graph})

@login_required
def Chart_select(request):
    graph=None
    error=None
    df=None
    df2=None
    price=None
    try:
        product_df=pd.DataFrame(Product.objects.all().values())
        purchase_df=pd.DataFrame(Purchase.objects.all().values())
        product_df['product_id']=product_df['id']
        
        price=purchase_df['total_price']
       
        if purchase_df.shape[0] > 0:
            
            df= pd.merge(purchase_df,product_df ,on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis=1)
            
            if request.method == 'POST':
                
                chart_type=request.POST['sales']
                date_from=request.POST['date_from']
                date_to=request.POST['date_to']
               
                df['date']=df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                df2= df.groupby('date',as_index=False)['total_price'].agg('sum')
                
                if chart_type != "":
                    if date_from !='' and date_to !='':
                        df=df[df['date'].between(date_from,date_to,inclusive=True)]
                        df2=df.groupby('date',as_index=False)['total_price'].agg('sum')
                       
                        graph = get_simple_plot(chart_type , x = df2['date'], y = df2['total_price'],data=df)
                        
                    graph = get_simple_plot(chart_type , x = df2['date'], y = df2['total_price'],data=df)
                else:
                    error="select the chart type"
        else:
            error="no data available "
    except:
            purchase_df=None
            product_df=None
            price=None
        
    context={
            'graph':graph,
            'error':error,
            'price':price
        }

    return render(request,'product/main.html',context)

@login_required
def add_purchase(request):
     
    error_message=None
    form=Purchaseform(request.POST or None)
    add_message=None  
    
    if form.is_valid():

                form=Purchaseform(request.POST)
                form.save()
                add_message="record has been saved"
            
    else:
        error_message="Invalid details"
    

    context={
          'form':form,
          'add_message':add_message,
          'error_message':error_message,
          
      }
    return render(request,"product/add.html",context)