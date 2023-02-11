from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('desktop1.html')  # templates 폴더에 있는 html 파일 정보를 가져온다.
    return HttpResponse(template.render())  # template을 view에 표현한다.
