from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('pdf_download/',views.DownloadPDF.as_view(),name="pdf_download")
    path('database/<str:dp>/<int:id>',views.single_id),
]
