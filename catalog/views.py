from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catalog.models import Product
from django.views import generic as g


# Create your views here.

class HomeListView(g.ListView):
    model = Product
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


class ContactsCreateView(g.CreateView):
    model = Product
    template_name = "catalog/contacts.html"
    fields = ()
    extra_context = {"title": "Контакты"}
    success_url = "#"

    def form_valid(self, form) -> HttpResponse:
        data = form.cleaned_data
        return super().form_valid(form)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        name_from_form = request.POST.get("name")
        email_from_form = request.POST.get("email")
        message_from_form = request.POST.get("massage")
        print(f"""
Имя: {name_from_form};
Электронная почта: {email_from_form};
Сообщение от пользователя: {message_from_form}
""")
        return super().post(request, *args, **kwargs)



class ProductCardTemplateView(g.TemplateView):
    pass


def product1(request, pk):
    products_list = Product.objects.filter(id=pk)

    product_item = Product.objects.get(pk=pk)
    context = {
        "object_list": products_list,
        "title": f"Здесь вы найдете лучшие {product_item} в Мордовии!"
    }
    return render(request, "catalog/product1.html", context)
