from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.cache import cache
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Category, Author
from .filters import PostFilter, UserFilter
from django.shortcuts import render, get_object_or_404, redirect
# from .tasks import text
from .forms import PostForm, CategoryForm, AuthorForm


class PostList(ListView):
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 10

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj

class PostCreateView(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    permission_required = ('news.add_post',)
    raise_exception = True
    template_name = 'news/post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        user = get_object_or_404(User, username=self.request.user)
        if not Author.objects.filter(authorUser__username=user).exists():#проверка, есть ли связь юзер-автор
            author = Author(authorUser=user)
            author.save()
        form.instance.author = self.request.user.author
        return super().form_valid(form)

class CatCreateView(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    permission_required = ('news.add_category',)
    raise_exception = True
    template_name = 'news/category_create.html'
    form_class = CategoryForm
    success_url = '/posts/'


class AuthorCreateView(LoginRequiredMixin, CreateView):
    raise_exception = True
    template_name = 'news/create_author.html'
    form_class = AuthorForm
    success_url = '/posts/'


# дженерик для редактирования объекта
class PostUpdateView(UpdateView, PermissionRequiredMixin):
    permission_required = ('news.change_post',)
    template_name = 'news/post_update.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

# дженерик для удаления товара
class PostDeleteView(DeleteView, PermissionRequiredMixin):
    permission_required = ('news.delete_post',)
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


def user_filter(request):
    u = UserFilter(request.GET, queryset=User.objects.all())
    return render(request, 'news/user_filter.html', {'filter': u})


class CatListView(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.category).order_by('-dateCreation')
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

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})

# class WeekView(View):
#     def get(self, request):
#         notify_about_new_post.delay()
#         return redirect("/")
#
#
#
# class WeekViews(View):
#     def get(self, request):
#         notify_weekly.delay()
#         return redirect("/")

# def create_post(request):
#     form = PostForm()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/posts/')
#     return render(request, 'post_create.html', {'form' : form})

# def index(request):
#     text.delay()
#     return render(request, 'news/index.html')