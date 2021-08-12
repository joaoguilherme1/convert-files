from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from main.forms import SendForm

def index_test(request):
    dct = {
        'Method': request.method,
        #get data
        'GET_Data': request.GET,
        #post data
        'POST_Data': request.POST,
        #querry string
        'query_string': request.META['QUERY_STRING'],
        #calcula o quadrado do campo
        'goddam': request.POST['calculadora'],
        'calculo_do_quadrado': (int(request.POST['calculadora']))**2,
        #'ARQUIVO': request.FILES['myfile'],
        #checar se arquivo é pdf
        #'IS_PDF_?': (True if request.FILES['myfile'].name[-4:] == '.pdf' else False),
        #checar o caminho temporario do arquivo
        'check_path': request.FILES['myfile'].temporary_file_path()
    }
    context={
        'data': dct,
    }

    if request.FILES:
        uplfile=request.FILES['myfile']
        context['filename']=uplfile.name
        context['filesize']=uplfile.size
        context['contenttype']=uplfile.content_type
        context['filedata']=uplfile.read()
        context['filecharset']=uplfile.charset

    return render(request, 'home.html', context)


# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get(self, request):
#         form = SendForm()
#         return render(request, self.template_name, {'form': form})
    
#     def post(self, request):
#         pass