import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.views import generic

from .models import Book, Author, LiteraryFormat

from django.urls import reverse


def hello_world(request: HttpRequest, unique_number: int = None) -> HttpResponse:
    now = datetime.datetime.now()
    print(f"Request params: {request.GET}")
    print(f"Unique number: {unique_number}")
    return HttpResponse("<html>"
                        "<h1>Hello, world</h1>"
                        f"<h4>Current moment: {now}<h4>"
                        f"<h4>Unique number: {unique_number}<h4>"
                        "</html>")



@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_format = LiteraryFormat.objects.count()
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_format": num_literary_format,
        "num_visits": num_visits + 1,
    }
    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"
    # queryset = LiteraryFormat.objects.filter(name__endswith="y")

def literary_format_list_view(request: HttpRequest) -> HttpResponse:
    literary_format_list = LiteraryFormat.objects.all()
    context = {
        "literary_format_list": literary_format_list,
    }
    return render(request, "catalog/literary_format_list.html", context=context)


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    # template_name = "catalog/book_list.html"
    # context_object_name = "book_list"
    paginate_by = 2

    # def get_absolute_ulr(sel(self):
    #     return reverse("catalog:book-detail")


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    context = {"book": book}
    return render(request, "catalog/book_detail.html", context=context)


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


def test_session_view(request: HttpRequest) -> HttpResponse:
    # request.session["book"] = "test session book"
    return HttpResponse(f"<h1>Test session: {request.session["book"]}</h1>")



