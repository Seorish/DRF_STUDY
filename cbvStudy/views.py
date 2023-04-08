from django.shortcuts import render
#제너릭 뷰 import
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#URL 패턴 로드된 후 URL 생성-> URL패턴 변경으로 인한 오류 방지에 도움
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

#목록 : Post 모델 객체를 리스트 형태로 보여줌
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

#세부정보
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

#생성
class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

#수정
class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

#삭제
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('post_list')