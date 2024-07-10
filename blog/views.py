from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
	x = {"blog":Blog.objects.filter(active=True)}
	return render(request, 'index.html' , x)
def main(request , id):
	m = {"blog":Blog.objects.get(id=id)}
	return render(request, 'main.html' , m)
