import django_filters
from django_filters import FilterSet, CharFilter, DateFromToRangeFilter, ModelChoiceFilter, ModelMultipleChoiceFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Category
from django.contrib.auth.models import User


# создаём фильтр

class PostFilter(FilterSet):
    postCategory = ModelChoiceFilter(
        # field_name='PostCategory.name',
        queryset=Category.objects.all(),
        label='Категория'
    )
    dateCreation = DateFromToRangeFilter()
    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'categoryType' : ['exact'],
            'title' : ['icontains'],
        }
# dateCreation': ['lt', 'gt'],
#Кастомный фильтр
class UserFilter(FilterSet):
    username = CharFilter(method='my_filter')
    class Meta:
        model = User
        fields = [
            'username'
        ]
    def my_filter(self, queryset, name, value):
        return queryset.filter(**{
            name : value
        })

