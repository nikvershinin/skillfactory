# Generated by Django 4.1.6 on 2023-02-12 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryType', models.CharField(choices=[('tanks', 'Танки'), ('heals', 'Хилы'), ('dd', 'ДД'), ('traders', 'Торговцы'), ('guildMasters', 'Гилдмастеры'), ('smiths', 'Кузнецы'), ('skinmakers', 'Кожевники'), ('poisonmakers', 'Зельевары'), ('spellmasters', 'Мастера заклинаний')], default='tanks', max_length=32, verbose_name='Категория')),
                ('subscribers', models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.author', verbose_name='Автор')),
                ('postCategory', models.ManyToManyField(to='post.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Объясвление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
