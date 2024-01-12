from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # contact (CRUD)
    path('<int:contact_id>/', views.contact, name='contact'),
]
