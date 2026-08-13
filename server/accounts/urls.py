from django.urls import path
from accounts.views import AccountListCreateView


urlpatterns = [
    path('', AccountListCreateView.as_view()),
    path('accounts/', AccountListCreateView.as_view()),
]