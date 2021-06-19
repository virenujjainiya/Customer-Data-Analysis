# import matplotlib.pyplot as plt
# import seaborn as sbn
# from io import BytesIO
# import base64
# def get_image():
#     #create byte buffer to save image 
#     buffer=BytesIO()    
#     #create the plot with use of ByteIO object as its "file"
#     plt.savefig(buffer,format='png')
#     #set the cursor to the begining of stream
#     buffer.seek(0)
#     #retrieve entire content of file
#     image_png = buffer.getvalue()
#     graph=base64.b64encode(image_png)
#     graph=graph.decode('utf-8')

#     #free the buffer momery
#     buffer.close()

#     return graph
    

# def get_chart(chart_value,*args, **kwargs):
#     #from matplotlib backend
#     plt.switch_backend('AGG')
#     fig =plt.figure(figsize=(10,4))
#     # what is need to draw a graph is ?
#     # x
#     # y
#     # data frame(df)
#     x= kwargs.get('x')
#     y= kwargs.get('y')
#     data=kwargs.get('data')
#     if chart_value == 'bar plot':
#         title="Bar Plot"
#         plt.title(title)
#         plt.bar(x,y)
#     elif chart_value=='line plot':
#         title="Line Plot"
#         plt.title(title)
#         plt.plot(x,y)
#     else:
#         title="Count Plot"
#         plt.title(title)
#         sbn.countplot('name',data=data)
#     plt.tight_layout()
#     graph=get_image()
    
#     return graph   


from django.db.models.expressions import Value
import matplotlib.pyplot as plt
import seaborn as sbn
from io import BytesIO
import base64
from django.contrib.auth.models import User

def get_user_name(val):
    salesman=User.objects.get(id=val)
    return salesman

def get_image():
    #create byte buffer to save image 
    buffer=BytesIO()    
    #create the plot with use of ByteIO object as its "file"
    plt.savefig(buffer,format='png')
    #set the cursor to the begining of stream
    buffer.seek(0)
    #retrieve entire content of file
    image_png = buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')

    #free the buffer momery
    buffer.close()

    return graph
    

def get_simple_plot(chart_type,*args, **kwargs):
    #from matplotlib backend
    plt.switch_backend('AGG')
    fig =plt.figure(figsize=(10,4))
    # what is need to draw a graph is ?
    # x
    # y
    # data frame(df)
    x= kwargs.get('x')
    y= kwargs.get('y')
    data=kwargs.get('data')
    if chart_type == 'bar plot':
        title="Bar Plot"
        plt.title(title)
        plt.bar(x,y)
    elif chart_type=='line plot':
        title="Line Plot"
        plt.title(title)
        plt.plot(x,y)
    else:
        title="Count Plot"
        plt.title(title)
        sbn.countplot('name',data=data)
        plt.xlabel('Products')
    plt.xticks(rotation=60)
    plt.tight_layout()
    graph=get_image()
    
    return graph   


        
