from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# create your views here

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html')


def display_webpages(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html')

def display_Accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'Accessrecord':QLAO}
    return render(request,'display_Accessrecord.html')




def insert_topics(request):
    tn=input('Enter Topic: ')
    QLTO=Topic.objects.get_or_create(topic_name=tn)
    QLTO.save()
    # return HttpResponse('Topic is create successfully!!!!!')
    return render(request,'display_topic.html')