from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import myapp.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', myapp.views.index, name='index'),
    url(r'^db', myapp.views.db, name='db'),
    path('admin/', admin.site.urls),
]
