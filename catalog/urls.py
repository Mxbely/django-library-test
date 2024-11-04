from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path

from catalog.views import (hello_world, index, literary_format_list_view,
                           LiteraryFormatListView, BookListView, AuthorListView,
                           book_detail_view, BookDetailView, test_session_view, AuthorDetailView)

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("hello/", hello_world),
    # path("hello/<int:unique_number>/", hello_world),
    path("", index, name="index"),
    # path("literary-formats/", literary_format_list_view, name="literary-format-list"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    # path("books/<int:pk>/", book_detail_view, name="book-detail"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("test-session/", test_session_view, name="test-session"),
    # path("hello/", hello_world),
]

app_name = "catalog"