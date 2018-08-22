from django.shortcuts import render

from django.template.response import TemplateResponse
from django.http import HttpResponse

#hello()関数
def hello(request):


    context = {"message": "メッセージ"}
    return TemplateResponse(request, "item/message.html", context)

def post(request, post_id):
    return HttpResponse("post_idは = {} です。".format(post_id))


