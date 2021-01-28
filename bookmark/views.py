from django.shortcuts import render

# Create your views here.
# 클래스형 뷰(제네릭 뷰):장고에서 미리 정해져 있는 뷰
# 함수형 뷰 : 개인이 직접 만드는 뷰

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
#   글 작성후 돌아갈 페이지를 지정
    success_url = reverse_lazy('list')
#    bookmark_form.html 의 이름을 bookmark.create.html 로 변경
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')