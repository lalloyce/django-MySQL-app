from django.urls import path
from .views import home, portfolio_details, service_details, starter_page

urlpatterns = [
    path('', home, name='home'),
    path('portfolio-details/', portfolio_details, name='portfolio_details'),
    path('service-details/', service_details, name='service_details'),
    path('starter-page/', starter_page, name='starter_page'),
]