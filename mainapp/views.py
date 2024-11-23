from django.shortcuts import render
from mainapp.models import File
# Create your views here.

def index(requests):
    if requests.method == 'POST':
        file_name = requests.POST.get('file_name')
        code = requests.POST.get('code') 

        new_file = File(file_name=file_name, content=code)
        new_file.save()
        return render(requests, 'home.html')
    return render(requests, 'home.html')

def saved_files(requests):
    files_data = File.objects.all()
    return render(requests, 'savedFiles.html', {'files':files_data})

