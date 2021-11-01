from django.shortcuts import render
from django.views.generic import ListView,DetailView

from django.http import HttpResponse
from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name='pages/index.html'
    ordering = ['-id']
class BlogDetailView(DetailView):
    model = Post
    template_name='pages/post_detail.html'
class BlogListViewEdebiyat(ListView):
    model = Post
    template_name='pages/edebiyat.html'
    ordering = ['-id']
class BlogListViewTekno(ListView):
    model = Post
    template_name='pages/teknoloji.html'
    ordering = ['-id']
class BlogListViewTarih(ListView):
    model = Post
    template_name='pages/tarih.html'
    ordering = ['-id']
class BlogListViewEgitim(ListView):
    model = Post
    template_name='pages/egitim.html'
    ordering = ['-id']
def index(request):   
    return render(request,'pages/index.html')
def teknoloji(request):
    return render(request,'pages/teknoloji.html')
def edebiyat(request):   
    return render(request,'pages/edebiyat.html')
def tarih(request):   
    return render(request,'pages/tarih.html')
def egitim(request):   
    return render(request,'pages/egitim.html')
def post_detail(request):
    return render(request,'pages/post_detail.html')





