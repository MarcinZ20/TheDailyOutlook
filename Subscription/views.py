from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def questionare(request):
    context = {}
    return render(request, "questionare.html", context)