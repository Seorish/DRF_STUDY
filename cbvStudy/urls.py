from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_new"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
]