from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from main.forms import SendForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = SendForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        pass