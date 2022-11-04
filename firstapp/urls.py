from django.urls import path,re_path
# from firstapp import views
from . import views
# app_name = 'firstapp'

urlpatterns = [
    path('',views.index,name = 'index.html'),
    path('read-number/<int:number>',views.read_number,name = 'read-number.html'),
    re_path(r'^read-year/(?P<year>[0-9]{4})/$',views.read_year),
    re_path(r'^read-page/(?:page-(?P<number>\d+)/)?$',views.page),
    path('websites/',views.read_websites),
]