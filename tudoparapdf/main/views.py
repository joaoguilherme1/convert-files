from django.conf import settings
from django.shortcuts import render
from django.urls.conf import path
from django.views.generic import TemplateView
from django.http import HttpResponse, FileResponse, response
import random
import pyheif
import tempfile
from PIL import Image
import os
import pathlib

# def download(request):
#     file_server = pathlib.Path('/static/')
#     if not file_server.exists():
#         menssages.error(request, 'file not found.')
#     else:
#         file_to_download = open(str('cubomagico64666'), 'rb')
#         response = FileResponse(file_to_download, content_type='application/force-download')
#         response['Content-Disposition'] = 'inline; filename="thisone"'
#         return response
#     return redirect('a_url_path')

def index_test(request):

    if request.method == 'GET':
        return render(request, 'home.html')

    elif request.method == 'POST':
        tmp = tempfile.NamedTemporaryFile(delete=False)
        nome = request.POST['nome_arquivo']
        heif_file = pyheif.read(request.FILES['myfile'].temporary_file_path())
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )
        image.save("/tmp/"+nome, "JPEG")
        #tmp = tempfile.NamedTemporaryFile(delete=False)
            # write to your tempfile, mode may vary
        #fl = open(request.FILES['myfile'].temporary_file_path(), 'rb')
        fl = open("/tmp/"+nome, 'rb')
        response = FileResponse(fl)
        response['Content-Disposition'] = "attachment; filename=%s" % nome
        return response