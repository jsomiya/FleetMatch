from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
# from rest_framework.decorators import action
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from django.shortcuts import redirect
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from django.http import HttpResponse


from .serializers import UserSerializer, SignupSerializer, RegisterSerializer
from .models import Registration

# Create your views here.
class SignupAPI(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#Login API
class LoginAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user is not None and user.is_active:
            auth.login(request, user)
            print(user)
            return super(LoginAPI, self).post(request, format=None)
        else:
            return HttpResponse(status = 404)

# class RegisterAPI(generics.ListCreateAPIView):
#     queryset = Registration.objects.all()
#     serializer_class = RegisterSerializer

def hello(request):
    return HttpResponse(status=status.HTTP_200_OK)

class Register(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @api_view(['POST'])
    def register(request):
        user = request.user
        print(user)
        if user.is_authenticated:
            registration = Registration.objects.create(user=user)
            print(registration)
            data=request.data
            serializer = RegisterSerializer(registration,data, many= False)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "registered successfully"
                return Response(data = data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view()
    def dashboard(request):
        user = request.user
        print(user)
        if user.is_authenticated:
            print(user)
            profile = Registration.objects.filter(user = user)
            print(profile)
            serializer = RegisterSerializer(profile, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("Nope")
            return HttpResponse(status=404)


    @api_view(['PUT'])
    def update_profile(request):
        user = request.user
        print(user)
        if request.method == "PUT":
            registration = Registration.objects.get(user = user)
            print(registration)
            serializer = RegisterSerializer(registration, data = request.data, many = False)
            print(serializer)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update successful"
                return Response(data = data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @api_view(['DELETE'])
    def delete_profile(request):
        user = request.user
        print(user)
        if request.method == "DELETE":
            registration = Registration.objects.get(user = user)
            print(registration)
            operation = registration.delete()
            data = {}
            if operation:
                data["success"] = "delete successful"
            else:
                data["failure"] = "delete unsuccessful"
                return Response(data = data)
    

