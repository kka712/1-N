from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    # Article
    # Create
    path('create/', views.create, name='create'),
    # Read
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    # Comment
    # Create
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
]






