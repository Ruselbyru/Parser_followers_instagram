from .models import Profile
from django.shortcuts import redirect
import pandas as pd
import openpyxl


def download_table(request):

    data=pd.DataFrame()
    for profile in Profile.objects.filter(download=True):
        prof = Profile.objects.get(name = profile.name)
        followers_list = []
        for followee in prof.followers_set.all():
            followers_list.append(followee.followers)
        result = pd.Series(followers_list,name=profile.name)
        data = pd.concat([data,result], axis=1)
    data.to_excel('followers.xlsx')
    # print(data)
    return redirect('/list')