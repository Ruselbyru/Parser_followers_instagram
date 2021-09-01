from .models import Profile
from django.shortcuts import redirect
import instaloader
from instaproject import settings


def save_followers(request):
    L = instaloader.Instaloader()
    #connect instaloader
    L.login(settings.INSTA_LOGIN, settings.INSTA_PASSWORD)

    for prof in Profile.objects.filter(download=False):
        profile = instaloader.Profile.from_username(L.context, prof.name)
        # parse followers
        for followee in profile.get_followers():
            profile_model= Profile.objects.get(name=prof.name)
            profile_model.followers_set.create(followers=followee.username)
        # update model profile
        profile = Profile.objects.get(name=prof.name)
        profile.download=True
        profile.save()
    return redirect('/list')