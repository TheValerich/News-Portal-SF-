from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from datetime import datetime
from .forms import PostForm
from .models import Post, Category
from django.urls import reverse_lazy
from .filters import NewsFilter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


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


class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-time_post')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    message = "Вы успешно подписались на рассылку новостей в категории"
    return render(request, 'subscribe.html', {'category': category, 'message': message})
