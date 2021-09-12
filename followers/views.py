import os.path

from django.shortcuts import render,redirect
from django.views.generic import CreateView , ListView
from .models import Profile, Files
from django.http import HttpResponse,Http404
import os
from instaproject import settings





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


# table list
def home(request):
    context= {'file': Files.objects.all()}
    return render(request, 'download.html', context=context)


#download table
def download (request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open (file_path, 'rb') as fh:
            responce= HttpResponse(fh.read(), content_type='applications/adminupload')
            responce['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return responce

    raise Http404


#delete table
def delete_table (request, id):
    table = Files.objects.get(id=id)
    os.remove(settings.BASE_DIR.joinpath(f'media_cdn/{table.adminupload}'))
    table.delete()
    return redirect('/load')