from django.urls import path
from roles.views import RolesCreateView

urlpatterns = [
    path('roles/', RolesCreateView.as_view())
]