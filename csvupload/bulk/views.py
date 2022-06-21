from csv import DictReader
from io import TextIOWrapper

from django.shortcuts import render
from django.views.generic.base import View

from .forms import ImportForm, ProductForm


class ImportView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "import.html", {"form": ImportForm()})

    def post(self, request, *args, **kwargs):
        products_file = request.FILES["products_file"]
        rows = TextIOWrapper(products_file, encoding="utf-8", newline="")
        for row in DictReader(rows):
            form = ProductForm(row)
            if not form.is_valid():
                return render(
                    request,
                    "import.html",
                    {"form": ImportForm(), "form_errors": form.errors}
                )
            form.save()
        return render(request, "import.html", {"form": ImportForm()})
