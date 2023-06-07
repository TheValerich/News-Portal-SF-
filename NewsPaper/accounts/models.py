from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def update_rating(self):  # Не знаю как реализовать
        pass


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category.title()

    def get_category(self):
        return self.name


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    CHOICE_POST = [
        (article, 'Статья'),
        (news, 'Новость')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    choice = models.CharField(max_length=2, choices=CHOICE_POST, verbose_name='Выбор')
    time_post = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    categories = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория')
    title_post = models.CharField(max_length=255, verbose_name='Заголовок')
    text_post = models.TextField(verbose_name='Текст')
    rating_post = models.IntegerField(default=0, verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_post']

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return str(self.text_post) + '...'

    def __str__(self):
        return self.title_post.title()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
