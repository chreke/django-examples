from csv import DictReader

from django.shortcuts import render
from django.views.generic.base import View

from .forms import ImportForm, ProductForm


class ImportView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "import.html", {"form": ImportForm()})

    def post(self, request, *args, **kwargs):
        rows = request.FILES["data_file"].read().decode("utf-8")
        for row in DictReader(rows):
            form = ProductForm(row)
            if not form.is_valid():
                return render(
                    request,
                    "import.html",
                    {"form": ImportForm(), "errors": form.errors}
                )
            form.save()
        return render(request, "import.html", {"form": ImportForm()})
