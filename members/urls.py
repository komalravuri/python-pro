from django.urls import path
from .views import userregistration

urlpatterns = [
    path('registration/',userregistration.as_view(), name='registr'),
]
