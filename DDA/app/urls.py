
from django.urls import path
from django.views.generic import TemplateView
from app.views import EntryList, CampList, CampDetail, EntryDetail, CampCreate, EntryCreate

urlpatterns = [
    # home/ ['']
    path('', TemplateView.as_view(template_name='app/home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='app/home.html'), name='home'),

    # camps/
    path('camps/', CampList.as_view(), name='camps'),

    # entries/
    path('entries/', EntryList.as_view(), name='entries'),

    # camp/1---
    path('camp/<int:pk>/', CampDetail.as_view(), name='camp-detail'),

    # entry/1---
    path('entry/<int:pk>/', EntryDetail.as_view(), name='entry-detail'),

    # AddCamp
    path('addCamp/', CampCreate.as_view(), name='camp-create'),

    # AddEntry
    path('addEntry/', EntryCreate.as_view(), name='entry-create'),

]
