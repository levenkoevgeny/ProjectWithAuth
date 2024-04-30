from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic.base import RedirectView

from rest_framework import routers

from dictionary import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'dictionaries', views.DictionaryViewSet, basename='dictionaries')
router.register(r'words', views.WordViewSet)
router.register(r'usernames', views.UserNamesViewSet, basename='usernames')

urlpatterns = [
    path('', RedirectView.as_view(url='/api')),
    # path('api/init/', views.init_dict),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/users/me/', views.get_me),
    path('api/google/', views.get_google_access_token),
    path('api/users/user-registration/', views.user_registration),
    path('api/init-dict/', views.init_dict),
    path('api/', include(router.urls)),
]
