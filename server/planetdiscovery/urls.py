from django.urls import path
from planetdiscovery.views import PlanetDiscoveryCreateView


urlpatterns = [
    path('', PlanetDiscoveryCreateView.as_view()),
    path('planetdiscovery/', PlanetDiscoveryCreateView.as_view()),
]