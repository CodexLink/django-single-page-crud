from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', DataView.as_view(), name='data_user_view'),
    path('login/', UserAuthView.as_view(), name='auth_user_view'),
    path('logout/', UserDeauthView.as_view(), name='deauth_user_view'),
    path('register/', UserRegistrationView.as_view(), name='new_user_view'),
    path('admin/', admin.site.urls),
    path ('data/', include([
        path('addNewData/', DataAddition.as_view(), name='implicit_add_data_view'),
        path('updateExistingData/', DataUpdate.as_view(), name='implicit_update_specific_view'),
        path('exportAll/', ExplicitActions.as_view(Action="ExportAll"), name='explicit_export_all_view'),
        path('deleteAll/', ExplicitActions.as_view(Action="DeleteAll"), name='explicit_delete_all_view'),
        path('deleteSpecific/<uuid:dataAttached>', ExplicitActions.as_view(Action="DeleteSpecific"), name='implicit_delete_specific_view'),
    ]))
]
