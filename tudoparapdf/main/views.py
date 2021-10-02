from os import name
from django.conf import settings
from django.shortcuts import render
from django.urls.conf import path
from django.views.generic import TemplateView
from django.http import HttpResponse, FileResponse, response
import random as rd
import pyheif
import tempfile
from PIL import Image
import zipfile as zp

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

def heif_to_jpeg(request):

    if request.method == 'GET':
        return render(request, 'home.html')

    elif request.method == 'POST':

        name_files = request.POST['nome_arquivo']
        name_dir = request.POST['nome_pasta']
        name_dir_with_main_dir = f'/tmp/{name_dir}.zip'
        images_heif = request.FILES.getlist('file[]')

        if name_files == '':
            name_files = 'Convertendo'
        if name_dir == '':
            name_dir = 'Zipando'
        middle_zipfile = zp.ZipFile(name_dir_with_main_dir, 'w')

        for i in range(len(images_heif)):
            heif_file = pyheif.read(images_heif[i].temporary_file_path())
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