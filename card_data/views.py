from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User # User =see and create user data in database, auth for authentication
#from django.contrib import auth
from .models import IdCard



# Create your views here.

def home(request):
    return render(request,'card_data/home.html',{})



def contact(request):
    return render(request,'card_data/contact.html',{})

def database(request):
    data=IdCard.objects.values()
    return render(request,'card_data/database.html',{'data':data})


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas        

def single_id(request,id):
    card = IdCard.objects.get(id=id)#,last_name=last_name)

    if request.GET.get('pdf')=='Export To PDF':
    
        pass
            #url = request.build_absolute_uri


        #         buffer=io.BytesIO()
        #         p = canvas.Canvas(buffer)
        #         p.drawString(10,10,
        #         f"""Name: {card.first_name}
        #         Surname: {card.last_name}
        #         Personal No: {card.personal_no}

        #         """
        #         )
        #         p.showPage()
        #         p.save()
        #         buffer.seek(0)
        #         return FileResponse(buffer,as_attachment=True,filename=f'{card.first_name+" "+card.last_name}.pdf')

        


            
        # print(request.build_absolute_uri())
    return render(request,'card_data/single_id.html',{'card':card})
