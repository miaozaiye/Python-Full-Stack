"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.views import index,form,detail,detail_comment,listing,index_login,index_register,detail_vote,listingTag,detail_ilike,personal_page,renew
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', index_login,name = 'login'),
    url(r'^register/$', index_register,name = 'register'),
    url(r'^logout/$', logout,{'next_page':'/register'},name = 'logout'),
    url(r'^index/$',index,name='index'),
    url(r'^form',form,name='form'),
    url(r'^detail/(?P<head_line>\w+[\-\w+]*)/comment$',detail_comment,name='comment'),
    url(r'^detail/vote/(?P<head_line>\w+[\-\w+]*)$',detail_vote,name='detail_vote'),
    url(r'^article/ilike/(?P<head_line>\w+[\-\w+]*)$',detail_ilike,name='detail_ilike'),
    url(r'^detail/(?P<id>\d+)/comment$',detail_comment,name='comment'),
    url(r'^detail/(?P<head_line>\w+[\-\w+]*)$',detail,name='detail'),
    url(r'^list/$',listing,name='listing'),
    url(r'^list/tag/(?P<tag>\w+)$',listingTag,name ='listingTag'),
    url(r'^list/(?P<cate>\w+)$',listing,name ='listing'),
    url(r'^personal_page/$', personal_page,name = 'personal_page'),
    url(r'^personal_page/renew/$', renew,name = 'renew'),


]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)