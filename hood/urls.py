from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home_page, name = 'home'),
    url('post/neighborhood/',views.post_neighborhood,name = 'post_neighborhood'),
    url('profile/',views.profile, name='profile_page'),
    url('profiles/update/', views.update_profile, name='update_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)