from django.urls import path, include
from .views import contact_form

app_name = 'contact'
urlpatterns = [
    path('', contact_form, name = 'contact-form')
]