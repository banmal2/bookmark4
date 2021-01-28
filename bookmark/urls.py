from django.urls import path
# from .views import BookmarkListView, BookmarkCreateView
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    # <int:pk> 게시판 등에서 글번호로 찾아서 써주겠다. <pk>로 하면 문자열
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]