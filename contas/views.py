from django.shortcuts import render
from django import db

def mostrar_hello(request):
  return render(request, 'index.html')