from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze, name='analyze'),
    path('analyze/results/', views.analyze_results, name='analyze_results'),
    path('analyze/delete_pills/', views.delete_pills, name='delete_pills'),
    # path('submit_deletions/', views.submit_deletions, name='submit_deletions'),
    path('aianalyzelist/', views.analyzelist, name='aianalyzelist'),
    ]
