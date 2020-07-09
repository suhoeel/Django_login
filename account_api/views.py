from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import UserAccountSerializer, UserProfileSerializer
from django.db import transaction
from .models import UserAccount, UserProfile
from django.core.mail import send_mail
from django.conf import settings

import datetime, json

def index(request):
    return HttpResponse("INDEX")

@csrf_exempt
def create_account(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['created_at'] = datetime.datetime.now()
        data['user_profile']['last_login_at'] = datetime.datetime.now()
        serializers = UserAccountSerializer(data=data)
        if serializers.is_valid():
            print(repr(serializers))
            serializers.create(serializers.validated_data)
            return JsonResponse(data=data, status=201)
        else:
            return HttpResponse(json.dumps(serializers.errors, ensure_ascii=True), status=404, content_type="application/json")

    return JsonResponse({'error': 'error'}, status=500)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # print(len(data['password']))
        user = UserAccount.objects.get(email=data['email'])
        # print(data)
        print(request.headers)
        if user.password == data['password']:
                print('LOGIN!!')
        else:
            print('FAILED!!')
            return JsonResponse(data=data, status = 404)               
    return JsonResponse(data=data, status = 201)

def send_email(request):
    subject = 'TEST GMAIL'
    message = ''
    # plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['',]
    for x in range(1000):
        message = str(x)
        send_mail(subject, message, email_from, recipient_list)
        # send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)

    return HttpResponse("OKAY")

# def validate_email():
# def validated_password():


