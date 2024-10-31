from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoListView.as_view(), name='list'),
    path('upload/', views.PhotoUploadView.as_view(), name='upload'),
    path('<uuid:pk>/', views.PhotoDetailView.as_view(), name='detail'),
    path('<uuid:pk>/edit/', views.PhotoUpdateView.as_view(), name='edit'),
    path('<uuid:pk>/delete/', views.PhotoDeleteView.as_view(), name='delete'),
]
