from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import ipdb


def home(request):
    form = UploadFileForm()
    return render(request, "home.html", {"form": form})


def handle_uploaded_file(f):
    with open("CNAB.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            with open("CNAB.txt", "r") as f:
                for chunk in request.FILES["file"].chunks():
                    f.read(chunk)
            return HttpResponseRedirect("home/")

        else:
            form = UploadFileForm()
            return render(request, "home.html", {"form": form})
