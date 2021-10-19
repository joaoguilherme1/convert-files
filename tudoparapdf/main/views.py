from django.conf import settings
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.template.response import TemplateResponse
#from django.views.generic import TemplateView
from django.http import FileResponse #, HttpResponse
import pyheif
from PIL import Image
import os
import zipfile as zp
import random as rd
import time as tm

def home(request):
    return TemplateResponse(request, 'home.html', {})

def pdf(request):
    return TemplateResponse(request, 'pdf.html', {})

def csv(request):
    return TemplateResponse(request, 'csv.html', {})

def docx(request):
    return TemplateResponse(request, 'docx.html', {})
def heic_to_jpeg(request):

    if request.method == 'GET':

        return render(request, 'heic_to_jpeg.html')

    elif request.method == 'POST':

        name_files = request.POST['nome_arquivo']
        name_dir = request.POST['nome_pasta']
        name_dir_with_main_dir = f'/tmp/{name_dir}.zip'
        images_heic = request.FILES.getlist('file[]')

        if name_files == '':
            name_files = 'helpmydoc_arquivo'
        elif name_dir == '':
            name_dir = 'Pasta_helpmydoc'

        if len(images_heic) == 0 or len(images_heic) > 20:
            return HttpResponse(status=403)

        else:
            middle_zipfile = zp.ZipFile(name_dir_with_main_dir, 'w')

            for i in range(len(images_heic)):

                if images_heic[i].size > 4000000:
                    return HttpResponse(status=403)

                else:
                    heif_file = pyheif.read(images_heic[i].temporary_file_path())
                    heif_file_to_jpeg = Image.frombytes(
                        heif_file.mode, 
                        heif_file.size, 
                        heif_file.data,
                        "raw",
                        heif_file.mode,
                        heif_file.stride,
                        )
                    heif_file_to_jpeg.save(f'/tmp/{name_files}_{i}.jpeg', "JPEG")
                    middle_zipfile.write(f'/tmp/{name_files}_{i}.jpeg')

            middle_zipfile.close()
            final_zipfile = open(name_dir_with_main_dir, 'rb')
            return FileResponse(final_zipfile)