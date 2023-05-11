from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return redirect('admin_panel')
    return render(request, 'myapp/upload.html')

def admin_panel(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            files = os.listdir('media/')
            return render(request, 'myapp/admin_panel.html', {'files': files})
    return render(request, 'myapp/login.html')

def download(request, file_name):
    file_path = os.path.join('media', file_name)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response

def open_file(request, file_name):
    file_path = os.path.join('media', file_name)
    if file_name.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_name.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        return HttpResponse('Invalid file format')
    return HttpResponse(data.to_html(), content_type='text/html')