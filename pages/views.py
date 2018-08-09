from django.shortcuts import render
from django.views.generic import TemplateView   #NEW

# Create your views here.
class HomePageView(TemplateView):   #NEW
    template_name = 'home.html'     #NEW

class AboutPageView(TemplateView):  #NEW
    template_name = 'about.html'    #NEW
