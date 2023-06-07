from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from datetime import datetime
from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy
from .filters import NewsFilter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class NewsList(ListView):
    model = Post
    ordering = '-time_post'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['time_now'] = datetime.utcnow()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['time_now'] = datetime.utcnow()
        return context


class NewsSearch(ListView):
    model = Post
    ordering = '-time_post'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = 'accounts.add_post'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.choice = 'NW'
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm
    permission_required = 'accounts.change_post'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
