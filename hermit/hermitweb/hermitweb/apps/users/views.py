from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from users.serializers import *
from users.models import *


# Create your views here.

def index(request):
    return HttpResponse("<h1>首页</h1>")


def login(request):
    return HttpResponse("登录成功")


class UserRegister(CreateAPIView):
    serializer_class = UserInfoSerial


# class UserLogin(APIView):
#     # authentication_classes = (authentication.TokenAuthentication, )
#     # permission_classes = (permissions.IsAdminUser, )
#
#     def get(self, request):
#         goods_list = UserInfo.objects.all()
#         goods_ser = UserInfoSerial(instance=goods_list, many=True)
#         return Response(goods_ser.data)
#
#     def post(self, request):
#         data = request.data
#         # p_date = datetime.datetime.strptime(data.get('pub_date'), "%Y-%m-%d")
#         # data['pub_date'] = p_date
#         goods_ser = UserInfoSerial(data=data)
#         goods_ser.is_valid()
#         print(type(goods_ser.data.get('pub_date')))
#         # goods_ser.save()
#         # return Response(goods_ser.data)
#         return Response("登录成功")
