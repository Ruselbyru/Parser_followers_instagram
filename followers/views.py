from django.shortcuts import render,redirect
from django.views.generic import CreateView , ListView
from .models import Profile, Followers
from .forms import DownloadUpdateForm



import pandas as pd
import instaloader
import openpyxl

# Create your views here.


class ProfileView (CreateView):
    model = Profile
    template_name = 'home.html'
    fields = ['name']


class ProfileList (ListView):
    model = Profile
    template_name = 'list.html'


def download_update(request,id):
    profile = Profile.objects.get(id=id)
    form = DownloadUpdateForm(instance=profile)
    if request.method == 'POST':
        form = DownloadUpdateForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form
    }
    return render(request,'update.html',context=context)


def delete_profile (request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('/')




def save_followers(request):
    L = instaloader.Instaloader()

    login = 'axyanon245'
    password = '8215mi4ru'
    L.login(login, password)

    for prof in Profile.objects.filter(download=True):
        profile = instaloader.Profile.from_username(L.context, prof.name)
        for followee in profile.get_followers():
            profile_model= Profile.objects.get(name=prof.name)
            profile_model.followers_set.create(followers=followee.username)

    return redirect('/')

def download_table(request):

    data=pd.DataFrame()
    for profile in Profile.objects.filter(download=True):
        prof = Profile.objects.get(name = profile.name)
        followers_list = []
        for followee in prof.followers_set.all():
            followers_list.append(followee.followers)
        result = pd.Series(followers_list,name=profile.name)
        data = pd.concat([data,result], axis=1)
    data.to_excel('exel.xlsx')
    return redirect('/')
