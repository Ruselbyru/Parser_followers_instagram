from django.shortcuts import render,redirect
from django.views.generic import CreateView , ListView,UpdateView
from .models import Profile, Followers
from .forms import DownloadUpdateForm
from django.db.models.signals import post_save


import instaloader

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
    profile_list = Profile.objects.filter(download=True)
    for profile_true in profile_list:
        L = instaloader.Instaloader()

        login = 'axyanon245'
        password = '8215mi4ru'

        L.login(login, password)


        profile = instaloader.Profile.from_username(L.context, profile_true)
        for followee in profile.get_followers():
            profile_model= Profile.objects.get(name=profile_true)
            profile_model.followers_set.create(followers=followee.username)

    return redirect('/')

# post_save.connect(save_profile,sender=Profile)