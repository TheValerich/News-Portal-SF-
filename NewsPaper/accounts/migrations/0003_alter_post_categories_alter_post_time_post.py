# Generated by Django 4.2 on 2023-05-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_post_options_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(through='accounts.PostCategory', to='accounts.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_post',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время публикации'),
        ),
    ]