from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('noticias/<int:pk>/', views.NoticiaDetalhesView.as_view(), name='detalhes'),
    path('noticias/resumo/', views.NoticiasResumoView.as_view(), name='resumo'),
    path('tags/<slug:tag_slug>/', views.noticias_da_tag, name='noticias_da_tag'),
]
