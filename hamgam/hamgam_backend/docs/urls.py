from django.urls import path 
from . import views
urlpatterns = [
    path('',views.DocListView.as_view()),
    path('<int:pk>/',views.DocDetailView.as_view()),
]