from django.urls import path
from .views import (
    personaCreateView,
    personasShowObject,
    personasDeleteView,
    personasListView,
    PersonaListView,
)
app_name = 'personas'
urlpatterns = [
    path('add/', personaCreateView, name='adding'),
    path('<int:myID>/', personasShowObject, name = 'browsing'),
    path('<int:myID>/delete/', personasDeleteView, name = 'deleting'),
    path('', personasListView, name = 'listing'),
    path('', PersonaListView.as_view(), name = 'persona-list'),
]
