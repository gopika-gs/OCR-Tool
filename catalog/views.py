import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.http import FileResponse
import pytesseract
from PIL import Image


# Create your views here.


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    
def homepage(request):
    return render (request,'homepage.html')

def uploaded(request):
    if request.method == 'POST':
        if request.FILES:
            image  = request.FILES['image']  
        else:
            message = 'Please select an image to upload.'
            return render(request, 'homepage.html', {'message': message})
        path = os.path.join(settings.MEDIA_ROOT, image.name)  # create a path to the file
        with open(path, 'wb+') as destination:
            for chunk in image.chunks():  # save the file
                destination.write(chunk)
        url = os.path.join(settings.MEDIA_URL, image.name) 
        pil_image = Image.open(image)
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
        extracted_text = pytesseract.image_to_string(pil_image)
        return render(request, 'file_upload.html',  {'url': url,'extracted_text': extracted_text})
    return render(request, 'homepage.html')

def serve_file(request, file_path):
    file = open(file_path, 'rb')
    response = FileResponse(file)
    return response
