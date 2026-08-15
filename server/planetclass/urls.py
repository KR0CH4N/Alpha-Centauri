from django.urls import path
from planetclass.views import PlanetClassCreateView


urlpatterns = [
    path('', PlanetClassCreateView.as_view()),
    path('planetclasses/', PlanetClassCreateView.as_view()),
]