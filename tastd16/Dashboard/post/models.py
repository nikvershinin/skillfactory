from django.db import models
from django.contrib.auth.models import User
from redactor.fields import RedactorField


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.pk}'

    def __str__(self):
        return self.authorUser.username

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} {self.commentUser.username} {self.commentPost.title[:200]}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    postCategory = models.ManyToManyField(Category, verbose_name='Категория')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    short_text = RedactorField(verbose_name=u'Text')

    def __str__(self):
        return f'{self.title()}: {self.text[:20]}...'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/post/{self.pk}'

    def preview(self):
        return self.text[0:123] + '...'

class Category(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    Tanks = 'ТК'
    Heals = 'ХЛ'
    DD = 'ДД'
    Traders = 'ТЦ'
    GuildMasters = 'ГМ'
    Smiths = 'КЦ'
    Skinmakers = 'КЖ'
    Poisonmakers = 'ЗВ'
    Spellmasters = 'МЗ'

    CATEGORY_CHOISES = (
        (Tanks, 'Танки'),
        (Heals, 'Хилы'),
        (DD, 'ДД'),
        (Traders, 'Торговцы'),
        (GuildMasters, 'Гилдмастеры'),
        (Smiths, 'Кузнецы'),
        (Skinmakers, 'Кожевники'),
        (Poisonmakers, 'Зельевары'),
        (Spellmasters, 'Мастера заклинаний'),
    )
