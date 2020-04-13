from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('override/', admin.site.urls),
    path('viewer/', DataView.as_view(), name='data_user_view'),
    path('login/', UserAuthView.as_view(), name='auth_user_view'),
    path('logout/', UserDeauthView.as_view(), name='deauth_user_view'),
    path('add/', DataAddition.as_view(), name='add_data_view'),
    path('delete/', DataDeletion.as_view(), name='delete_data_view'),
    path('update/', DataUpdate.as_view(), name='update_data_view'),
]
