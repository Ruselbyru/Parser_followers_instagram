from django.shortcuts import render,redirect
from django.views.generic import CreateView , ListView
from .models import Profile






# Create your views here.

# create profile model
class ProfileView (CreateView):
    model = Profile
    template_name = 'home.html'
    fields = ['name']

# list profile model
class ProfileList (ListView):
    model = Profile
    template_name = 'list.html'



# delete profile model
def delete_profile (request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('/list')


