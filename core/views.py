# coding:utf-8
from django.shortcuts import render_to_response, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from models import Photo
import json


def index(request):
    return render_to_response('index.html')


def response_json_error(data, status_code=400):
    response = HttpResponse(json.dumps(data), content_type='application/json', status=status_code)
    response['Access-Control-Allow-Origin'] = '*'
    return response


@csrf_exempt
def upload_images(request):
    if request.method == 'POST':
        file = request.FILES.get('fileList')
        images = Photo(image=file)
        try:
            images.save()
            url = images.image.url
            return HttpResponse(url)
        except Exception as e:
            return response_json_error(e)
    else:
        return redirect('/')
