from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

# Create your views here.
from .models import Noticia, Tag


class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'


class NoticiasResumoView(TemplateView):
    template_name = 'app_noticias/resumo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Noticia.objects.count()
        return context


class NoticiaDetalhesView(DetailView):
    model = Noticia
    template_name = 'app_noticias/detalhes.html'


def noticias_da_tag(request, tag_slug):
    try:
        tag = Tag.objects.get(slug=tag_slug)
        noticias = Noticia.objects.filter(tags__in=[tag])
    except Tag.DoesNotExist:
        raise Http404('Tag não encontrada')
    return render(request, 'app_noticias/noticias_da_tag.html', {'tag': tag, 'noticias': noticias})
