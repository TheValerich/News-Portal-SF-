from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms


class NewsFilter(FilterSet):
    date_time__gt = DateFilter(field_name='time_post',
                               widget=forms.DateInput(attrs={'type': 'date'}),
                               lookup_expr='gt',
                               label='Опубликовано после')

    class Meta:
        model = Post
        fields = [
            'title_post',
            'author'
        ]
