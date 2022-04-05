from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='list-article'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='single-article'),
    path('new/', views.ArticleCreateView.as_view(), name='add-article'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='edit-article'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='delete-article'),
]