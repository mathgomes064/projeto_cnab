from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from formularioCNAB.serializers import TransactionsSerializer
from .models import Transactions
from rest_framework.response import Response
from rest_framework.views import Request

# import ipdb


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
                for line in f.readlines():
                    data = {
                        "tipo": line[0],
                        "data": line[1:9],
                        "valor": line[9:19],
                        "cpf": line[19:30],
                        "cartao": line[30:42],
                        "hora": line[42:48],
                        "donoDaLoja": line[48:62].strip(),
                        "nomeLoja": line[62:81].strip(),
                    }
                    serializer = TransactionsSerializer(data=data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

            return HttpResponseRedirect("upload_data/")

        else:
            form = UploadFileForm()
            return render(request, "home.html", {"form": form})


def upload_data(request: Request) -> Response:
    data = Transactions.objects.all()
    serializer = TransactionsSerializer(data, many=True)
    context = {"data": serializer.data}
    # print(context["data"][0])
    for item in context["data"]:
        print(item)

    return render(request, "data.html", context)
