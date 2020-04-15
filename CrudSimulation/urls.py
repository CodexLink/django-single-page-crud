from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', DataView.as_view(), name='data_user_view'),
    path('login/', UserAuthView.as_view(), name='auth_user_view'),
    path('logout/', UserDeauthView.as_view(), name='deauth_user_view'),
    path('add/', DataAddition.as_view(), name='add_data_view'),
    path('delete/', DataDeletion.as_view(), name='delete_data_view'),
    path('update/', DataUpdate.as_view(), name='update_data_view'),
    path('admin/', admin.site.urls),
    path ('data/', include([
        path('exportAll/', ExplicitActions.as_view(Action="ExportAll"), name='explicit_export_all_view'),
        path('deleteAll/', ExplicitActions.as_view(Action="DeleteAll"), name='explicit_delete_all_view'),
        path('updateSpecific/<uuid:dataAttached>', ExplicitActions.as_view(Action="UpdateSpecific"), name='implicit_update_specific_view'),
        path('deleteSpecific/<uuid:dataAttached>', ExplicitActions.as_view(Action="DeleteSpecific"), name='implicit_delete_specific_view'),
    ]))
]
