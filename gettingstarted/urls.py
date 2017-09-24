from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sort', hello.views.sort, name='db'),
    url(r'^heist', hello.views.heist, name='db'),
    url(r'^stringcompression/RLE', hello.views.rle, name='db'),
    url(r'^stringcompression/LZW', hello.views.lzw, name='db'),
    url(r'^stringcompression/WDE', hello.views.wde, name='db'),
    url(r'^calculateemptyarea', hello.views.cal, name='db'),
    url(r'^releaseSchedule', hello.views.schedx, name='db'),
    url(r'^trainPlanner', hello.views.plan, name='db'),
    url(r'^horse-racing', hello.views.horse, name='db'),
    url(r'^warehouse-keeper/game-start', hello.views.ware, name='db')
]
