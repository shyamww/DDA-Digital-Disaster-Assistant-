
from django.urls import path
from django.views.generic import TemplateView
from account.views import UserFormView

urlpatterns = [

   path('', TemplateView.as_view(template_name='account/account.html'), name='account'),
   path('registration/', UserFormView.as_view(), name='registration'),


]