from django.conf.urls import url

from reports import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    # url(r'^admin/', include(admin.site.urls)),
]