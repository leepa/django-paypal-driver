#-*- coding: utf-8 -*-

from django.http import HttpResponse

def cancel_page(request):
    return HttpResponse("You have cancelled your PayPal Payment Process")

def error_page(request):
    return HttpResponse("There occured an error while performing your PayPal Payment Process")

def success_page(request):
    return HttpResponse("You have successfully complete your PayPal Payment Process")
