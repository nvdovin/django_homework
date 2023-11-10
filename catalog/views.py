from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from catalog.forms import CreateProduct
from catalog.models import Product, Version
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



class ProductCardView(g.DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product_card"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        version = Version.objects.all()
        context['version'] = version
        return context
    

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs["pk"])
        return queryset


class ProductCreateView(g.CreateView):
    model = Product
    template_name = "catalog/product_create.html"
    form_class = CreateProduct
    success_url = reverse_lazy('catalog:home')
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = False
        return context


class ProductUpdateView(g.UpdateView):
    model = Product
    template_name = "catalog/product_create.html"
    form_class = CreateProduct
    success_url = reverse_lazy('catalog:home')
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True
        return context
    
