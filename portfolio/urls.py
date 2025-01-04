from django.urls import path
from .views import home_view, AboutListView,ContactView,ServicesListView,ServicesListView,PortfolioListView
from .import views
urlpatterns = [    
    path('', home_view, name='index-page'), 
    path('about/', AboutListView.as_view(), name='about-page'),
    path('contact/', ContactView.as_view(), name='contact-page'),
    path('services/', ServicesListView.as_view(), name='services-page'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'),
    path('category/', views.Category, name='category'),
    path('services/', ServicesListView.as_view(), name='services-page'),

]
