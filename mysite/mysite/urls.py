"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SIH.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('second/',SEcond, name='se'),
    path('login/',Login, name='l'),
    path('about',about, name='A'),
    path('Gov',Gov, name='G'),
    path('Loan',Loan, name='L'),
    path('Scheme',scheme, name='S'),
    path('graph',graph, name='g'),
    path('pest',pest_data, name='P'),
    path('pest_details/<int:pid>',pest_details, name='Pd'),
    path('crop',crop, name='C'),
    path('crop_details/<int:cid>',crop_details, name='cd'),
    path('Logout',Logout, name='r'),
    path('mess', send_sms, name='M'),
    path('profile', profile, name='Pr'),
    path('fertilizer', fertilizer, name='Fr'),
    path('Soil_details',Soil_details, name='Soil'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
