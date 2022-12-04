from django.urls import path
from .views import *
# PostList, PostDetail, PostDeleteView, UserFilter, \
#     user_filter, PostCreateView, CatCreateView, PostUpdateView, AuthorCreateView, CatListView, subscribe, \
    # index  # импортируем наше представление

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('user_list/', user_filter, name="users-list"),
    path('create_category/', CatCreateView.as_view(), name='create_category'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('create_author/', AuthorCreateView.as_view(), name='create_author'),
    path('category/<int:pk>', CatListView.as_view(), name='category_list'),
    path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
    # path('index/', index)

]
#
# path('create/', PostCreateView.as_view(), name='post_create'),
#     path('create/<int:pk>', PostUpdateView.as_view(), name='post_create')