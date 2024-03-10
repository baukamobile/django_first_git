from django.urls import path
from Mymoney.views import *

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('',showPage, name='home'),
    path('about/', about,name='about'),
    path('contact/', contact, name='contact'),
    path('terms/', Terms, name='terms'),
    path('ourproducts/', OurProducts, name='ourproducts'),
    path('post/<int:post_id>/', showpost, name='post')
]

# urlpatterns+=staticfiles_urlpatterns()