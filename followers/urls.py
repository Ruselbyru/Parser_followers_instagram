from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProfileView.as_view(),name= 'home'),
    path('list',views.ProfileList.as_view(),name = 'list'),
    path('update/<int:id>',views.download_update,name = 'update'),
    path('delete/<int:id>', views.delete_profile,name= 'delete'),
    path('save',views.save_followers,name='save'),
    path('download', views.download_table,name= 'download'),
]