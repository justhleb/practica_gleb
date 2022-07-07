from django.shortcuts import render
from .forms import *
import datetime
import os


# def search_media_path():
#     wd = os.getcwd()
#     wd = str(wd)
#     pathtoviews=wd.split("\\")
#     print(pathtoviews)


def make_result_file(checkbox_results):
    scenes = {'sea': 'море',
              'city': 'город',
              'forest': 'лес',
              'field': 'поле', }

    objects = {'cat': 'кот',
               'home': 'дом',
               'chair': 'стул',
               'table': 'стол', }
    filename1 = datetime.datetime.now().strftime('result%d_%m_%Y-%H_%M_%S')
    result_file = open(f'{filename1}.txt', 'w',encoding='UTF-8')

    if checkbox_results:
        result_file = open(f'{filename1}.txt', 'w')
        result_file.write("Отмеченные сцены: ")
        for key in checkbox_results:
            if key in list(scenes.keys()):
                result_file.write(f"{scenes[key]}, ")
        result_file.write("\nОтмеченные объекты: ")
        for key in checkbox_results:
            if key in list(objects.keys()):
                result_file.write(f"{objects[key]}, ")
    else:
        result_file.write("нет отмеченных сцен или объектов\n")
    media = os.listdir('media')
    fold = os.walk('media')
    if media:
        result_file.write("\nНа сервере присутствуют следующие директории и файлы:\n")
        for folder in media:
            result_file.write(f"{folder}\n")
            images = os.listdir(f'media\\{folder}')
            if images:
                for image in images:
                    result_file.write(f"\t{image}\n")
                    file = '\\'.join(['media', folder, image])

    else:
        result_file.write("\nфайлы на сервере отсутствуют\n")


def refactor_form(request):
    """Process images uploaded by users"""
    if request.method == 'POST' and 'imagebutton' in request.POST:
        form1 = ImageForm(request.POST, request.FILES)
        form2 = CheckboxForm()
        if form1.is_valid():
            form1.save()
            # Get the current instance object to display in the template
            img_obj = form1.instance
            return render(request, 'index.html', {'form1': form1, 'img_obj': img_obj, 'form2': form2})
    elif request.method == 'POST' and 'checkboxbutton' in request.POST:
        form2 = CheckboxForm(request.POST)
        form1 = ImageForm()
        data = form2.data
        keys = []
        if data:
            keys = list(data.keys())
            keys.pop(-1)
            keys.pop(0)
        make_result_file(keys)
        # f.write(data)
    else:
        form1 = ImageForm()
        form2 = CheckboxForm()
    return render(request, 'index.html', {'form1': form1, 'form2': form2})
