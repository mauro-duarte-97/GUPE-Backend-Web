from django.urls import path
from apps.materia.views import MateriaDetailView
from apps.opinion.views import OpinionListView # Importa la vista de opiniones

urlpatterns = [
    path("detalle/<int:pk>", MateriaDetailView.as_view(), name="detalle_materia"),
    path('<int:entity_id>/opinion_historica/', OpinionListView.as_view(), kwargs={'model_name': 'materia'}, name='opiniones_materia'),
]