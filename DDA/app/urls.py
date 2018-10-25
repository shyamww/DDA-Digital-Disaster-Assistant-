
from django.urls import path
from django.views.generic import TemplateView
from app.views import EntryList, CampList, CampDetail, EntryDetail, CampCreate, EntryCreate
from app import views

urlpatterns = [
    # home/ ['']
    path('', TemplateView.as_view(template_name='app/home.html'), name='base'),
    path('home/', TemplateView.as_view(template_name='app/home.html'), name='home'),
    # home/prepare
    path('home/prepare/', TemplateView.as_view(template_name='app/prepare.html'), name='prepare'),
    # home/types
    path('home/types/', TemplateView.as_view(template_name='app/types.html'), name='types'),


    # entry/1---/camps---
    #path('entry/<int:pk>/camp', TemplateView.as_view(template_name='app/list/entry_camp.html'), name='entry-camp-list'),

    # camps/
    path('camp/', CampList.as_view(), name='camp'),

    # entries/
    path('entry/', EntryList.as_view(), name='entries'),

    # camp/1---
    path('camp/<int:pk>/', CampDetail.as_view(), name='camp-detail'),


    # entry/1---
    path('entry/<int:pk>/', EntryDetail.as_view(), name='entry-detail'),

    # AddCamp
    path('addCamp/', CampCreate.as_view(), name='camp-create'),

    # AddEntry
    path('addEntry/', EntryCreate.as_view(), name='entry-create'),

    # search
    path('search/', views.search, name='search'),



]












