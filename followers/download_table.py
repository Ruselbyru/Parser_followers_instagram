from .models import Profile,Files
from django.shortcuts import redirect
import pandas as pd
from instaproject import settings
import os


def download_table(request):
    table_name = ''
    data=pd.DataFrame()
    for profile in Profile.objects.filter(download=True):
        prof = Profile.objects.get(name = profile.name)
        table_name+=str(prof.id)+','
        followers_list = []
        for followee in prof.followers_set.all():
            followers_list.append(followee.followers)
        result = pd.Series(followers_list,name=profile.name)
        data = pd.concat([data,result], axis=1)


    if not os.path.isdir(settings.BASE_DIR.joinpath('media_cdn')):
        os.makedirs(settings.BASE_DIR.joinpath('media_cdn/media'))

    data.to_excel(settings.BASE_DIR.joinpath(f'media_cdn/media/{table_name}.xlsx'))
    f= Files(adminupload=f'media/{table_name}.xlsx', title = f'{table_name}')
    f.save()

    # print(data)
    return redirect('/load')