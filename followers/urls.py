from django.urls import path
from . import views,download_table,save_followers


urlpatterns = [
    path('',views.ProfileView.as_view(),name= 'home'),
    path('list',views.ProfileList.as_view(),name = 'list'),
    path('delete/<int:id>', views.delete_profile,name= 'delete'),
    path('save',save_followers.save_followers,name='save'),
    path('download', download_table.download_table,name= 'download'),
]