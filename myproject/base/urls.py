from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('add',add,name='add'),
    path('complete',complete,name='complete'),
    path('trash',trash,name='trash'),
    path('about',about,name='about'),

    path('completed/<int:pk>',completed,name='completed'),

    path('delete_/<int:pk>',delete_,name='delete_'),

    path('delete_all',delete_all,name='delete_all'),

    path('restore/<int:pk>',restore,name='restore'),

    path('update/<int:a>',update,name='update'),

    path('trestore',trestore,name='trestore'),

    path('crestore_all',crestore_all,name='crestore_all'),
    path('cdelete_all',cdelete_all,name='cdelete_all'),

    path('crestore/<int:pk>',crestore,name='crestore'),

    path('cdelete/<int:a>',cdelete,name='cdelete'),


    path('tdelete/<int:a>',tdelete,name='tdelete'),

    path('tdelete_all',tdelete_all,name='tdelete_all')


]