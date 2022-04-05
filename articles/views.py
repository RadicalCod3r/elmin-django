from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from .models import Article

# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'articles/article_list.html'
    model = Article
    context_object_name = 'articles'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'articles/single_article.html'
    model = Article
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'articles/article_create.html'
    model = Article
    fields = ('title', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'articles/article_update.html'
    model = Article
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/article_delete.html'
    model = Article
    success_url = reverse_lazy('list-article')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
