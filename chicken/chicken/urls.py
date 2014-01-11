from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic.base import TemplateView
from webapp import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chicken.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.index, name='index'),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^add_data$', views.add_data, name='add_data'),

    url(r'^api/data$', views.data, name='data')
)
