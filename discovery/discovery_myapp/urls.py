from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze, name='analyze'),
    path('analyze/results/', views.analyze_results, name='analyze_results'),
    path('aianalyzelist/', views.aianalyzelist, name='aianalyzelist'),
]
