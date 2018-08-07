from django.shortcuts import render

from django.template.response import TemplateResponse

#hello()関数
def hello(request):


    context = {"message": "メッセージ"}
    return TemplateResponse(request, "item/message.html", context)


