from django.urls import path
from . import views
from .views import BlogListView,BlogDetailView,BlogListViewEdebiyat,BlogListViewTekno,BlogListViewTarih,BlogListViewEgitim

urlpatterns = [
    path('post/<int:pk>/',BlogDetailView.as_view(),name="post_detail"),
    path('',BlogListView.as_view(),name='index'),
    path('teknoloji',BlogListViewTekno.as_view(), name = 'teknoloji'),
    path('edebiyat', BlogListViewEdebiyat.as_view(), name = 'edebiyat'), 
    path('tarih', BlogListViewTarih.as_view(), name = 'tarih'), 
    path('egitim', BlogListViewEgitim.as_view(), name = 'egitim'),       
]