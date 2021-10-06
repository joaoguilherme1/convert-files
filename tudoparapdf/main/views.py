from django.conf import settings
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.template.response import TemplateResponse
from django.core.exceptions import EmptyResultSet, MultipleObjectsReturned, PermissionDenied
#from django.views.generic import TemplateView
from django.http import FileResponse #, HttpResponse
import pyheif
from PIL import Image
import zipfile as zp
import random as rd
import time as tm

def home(request):
    return TemplateResponse(request, 'home.html', {})


def heic_to_jpeg(request):

    if request.method == 'GET':

        return render(request, 'heic_to_jpeg.html')

    elif request.method == 'POST':

        horario_do_request = tm.strftime("(%d/%m/%Y)|%H:%M", tm.localtime()) # BUGANDO
        name_files = request.POST['nome_arquivo']
        name_dir = request.POST['nome_pasta']
        name_dir_with_main_dir = f'/tmp/{name_dir}.zip'
        images_heic = request.FILES.getlist('file[]')

        if name_files == '':
            name_files = 'Convertendo'
        elif name_dir == '':
            name_dir = 'Zipando'

        if len(images_heic) == 0 or len(images_heic) >= 4:
            raise PermissionDenied('É necessario selecionar no minimo 1 e no maximo 4 para converter')

        else:

            middle_zipfile = zp.ZipFile(name_dir_with_main_dir, 'w')

            for i in range(len(images_heic)):

                if images_heic[i].size > 4000000:
                    raise PermissionDenied('O arquivo deve ser menor que 4mb')

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