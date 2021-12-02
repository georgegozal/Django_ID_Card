# ადამიანთა სიიდან რომელიმის არჩევის შემთხვევაში გამოაქვს მისი მთლიანი მინაცემები 
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from card_data.models import IdCard

import io
from django.http import HttpResponse,FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import Image,SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
#from PIL import Image
from reportlab.lib.pagesizes import A4,letter
from reportlab.lib.units import cm,inch
import requests
@login_required
def single_id(request,id,dp):
    #dp = 'dp'

    card = IdCard.objects.get(id=id)
    other = [item for item in card.other_info.all()]

    columns = ['First_name',
                'Last_name', 
                'Personal ID', 
                'Sex', 
                'Brith Date',
                'Birth Place',
                'Department',
                'დასაქმების ტიპი',
                'ცვლა',
                'Drivers License']
    rows = [card.first_name, 
            card.last_name,
            card.personal_no.zfill(11),
            card.sex, 
            card.birth_date, 
            card.birth_place, 
            card.department, 
            str(other[0]), 
            str(other[1]), 
            str(other[2])]


    if request.method == 'GET':
        if request.GET.get('excel'):
            import csv
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{card.first_name}-{card.last_name}.csv"'
            writer = csv.writer(response)
            writer.writerow(columns)
            writer.writerow(rows)
            return response

    if request.method == 'GET':
        if request.GET.get('pdf'):
            #prints with a pic
            # doc = SimpleDocTemplate(f"{card.first_name}-{card.last_name}",
            #                         pagesize=letter,
            #                         rightMargin=72,
            #                         leftMargin=72,
            #                         topMargin=72,
            #                         bottomMargin=18)

            # story = [] # data container

            # img = Image('media/'+str(card.photo),4*cm, 5.7*cm)
            # story.append(img)
            # story.append(Spacer(1, 12))
            # styles = getSampleStyleSheet()
            # styles.add(ParagraphStyle(name='Justify'))#, alignment=TA_JUSTIFY))

            # for row,col in zip(rows,columns):
            #     story.append(Paragraph(f"{col}:{row}", styles["Normal"]))
            #     story.append(Spacer(1, 12))

            # doc.build(story)

###################################################################################################################################33
            # prints without a pic
            buffer = io.BytesIO()
            # Create the PDF object, using the buffer as its "file."
            p = canvas.Canvas(buffer)
            img = Image('media/'+str(card.photo))

            first_row = 580
            for row,col in zip(rows[::-1],columns[::-1]):
                first_row +=20
                p.drawString(50, first_row, f"{col}:{row}") #595 x 842
            # Close the PDF object cleanly, and we're done.
            p.showPage()
            p.save()
            # FileResponse sets the Content-Disposition header so that browsers
            # present the option to save the file.
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename=f'{card.first_name}-{card.last_name}.pdf')


    return render(request,'pdf_csv/single_id.html',{'card':card})




