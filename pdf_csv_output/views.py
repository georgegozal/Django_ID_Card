# ადამიანთა სიიდან რომელიმის არჩევის შემთხვევაში გამოაქვს მისი მთლიანი მინაცემები 
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from card_data.models import IdCard
from django.http import HttpResponse

def single_id(request,id,dp):
    dp = 'dp'

    card = IdCard.objects.get(id=id)

    if request.method == 'GET':
        if request.GET.get('excel'):
            import csv
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
            writer = csv.writer(response)
            writer.writerow(['First_name','Last_name','Personal ID','Sex','Brith Date','Birth Place','Department'])
            writer.writerow([card.first_name,card.last_name,card.personal_no.zfill(11),card.sex,card.birth_date,card.birth_place,card.department])
            return response
    return render(request,'pdf_csv/single_id.html',{'card':card})


