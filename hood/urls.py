from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home_page, name = 'home'),
    url('post/neighborhood/',views.post_neighborhood,name = 'post_neighborhood'),
    url('profile/',views.profile, name='profile_page'),
    url('profiles/update/', views.update_profile, name='update_profile'),
    url('business/',views.business,name = 'business_list'),
    url('add/busines/',views.post_business,name='post_business'),
    url('businesss/(?P<id>\d+)', views.single_business, name='view_business'),
    url('search/', views.search, name='search'),
    url('post/',views.create_post, name = 'create_post'),
    url('posts/',views.posts_page,name = 'posts'),
    url('single/pots/(?P<id>\d+)', views.single_post, name = 'single_post'),
    url('hood/(?P<id>\d+)', views.single_neighborhood, name = 'hood'),
    url('police/',views.post_police,name = 'post_police'),
    url('health/',views.post_health, name = 'post_health'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)