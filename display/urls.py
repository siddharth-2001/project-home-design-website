from django.urls import path
from .views import all_designs_view, detail_design_view, all_concept_ctgry_view, all_concepts_view, concept_detail_view


urlpatterns = [
    path('designs/<str:choice>', all_designs_view, name= 'all-designs' ),
    path('designs/detail/<int:id>', detail_design_view, name = 'design-detail'),
    path('concepts', all_concept_ctgry_view, name = 'all-concepts'),
    path('concepts/<int:id>', all_concepts_view, name = 'all-concepts'),
    path('concepts/detail/<int:id>', concept_detail_view, name = 'concept-detail')
]