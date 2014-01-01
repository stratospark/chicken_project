from django.conf.urls import patterns, include, url

from django.contrib import admin
from webapp import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chicken.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^add_data$', views.add_data, name='add_data'),
)
