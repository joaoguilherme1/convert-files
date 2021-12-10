from typing import final
from django.conf import settings
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.template.response import TemplateResponse
#from django.views.generic import TemplateView
from django.http import FileResponse #, HttpResponse
import PyPDF2
import pyheif
from PIL import Image
import os
import zipfile as zp

def home(request):
    return TemplateResponse(request, 'home.html', {})

def pdf_merge(request):
    if request.method == 'GET':
        return TemplateResponse(request, 'pdf_merge.html', {})

    elif request.method == 'POST':

        final_name = request.POST['final_name']
        arqpdf_1 = request.FILES.getlist('arqpdf_1')
        arqpdf_2 = request.FILES.getlist('arqpdf_2')
        name_dir_with_main_dir = f'/tmp/{final_name}.pdf'

        dados_arq1 = PyPDF2.PdfFileReader(open(arqpdf_1[0].temporary_file_path(), "rb"))
        dados_arq2 = PyPDF2.PdfFileReader(open(arqpdf_2[0].temporary_file_path(), "rb"))

        merge = PyPDF2.PdfFileMerger()

        merge.append(dados_arq1)
        merge.append(dados_arq2)

        merge.write(name_dir_with_main_dir)
        final = open(name_dir_with_main_dir, "rb")
        return FileResponse(final)

def pdf_exclude_and_merge(request):
    return TemplateResponse(request, 'pdf_exclude_and_merge.html', {})

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