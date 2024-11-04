

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout

from django.urls import reverse


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "registration/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, "catalog/index.html")
            # return HttpResponseRedirect(reverse("catalog:index"))
        else:
            error_context = {
                "error": "Invalid username or password",
            }
            return render(request, "registration/login.html", context=error_context)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return render(request, "registration/logged_out.html")
