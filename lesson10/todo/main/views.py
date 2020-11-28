from django.shortcuts import render, HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse("Hello World!")


def test(request):
    return render(request, "test.html")


def page(request):
    return render(request, "page.html")


def fizz_buzz(request):
    a = 10
    if (a % 3 == 0) & (a % 5 == 0):
        return HttpResponse("FizzBuzz")
    elif a % 3 == 0:
        return HttpResponse("Fizz")
    elif a % 5 == 0:
        return HttpResponse("Buzz")
