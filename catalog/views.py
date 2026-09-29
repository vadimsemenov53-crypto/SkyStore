from itertools import product

from django.shortcuts import render, redirect
from catalog.models import Product, ContactInfo

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, View
from django.views import View
from django.urls import reverse_lazy, reverse

from .forms import ProductForm, ProductModeratorForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.services import ProductService

class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        return ProductService.get_products_from_cache()


class ProductCategoryView(View):

    def get(self, request, category_id):
        products = ProductService.get_products_by_category_cache(category_id)

        return render(request, 'category_products.html', {'products': products})




class ProductAddCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user

        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm

        if user == self.object.owner:
            return ProductForm

        raise PermissionDenied


@method_decorator(cache_page(60), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


class ContactView(View):

    def get(self, request):
        contacts_all = ContactInfo.objects.all()

        return render(request,'contacts.html',{'contacts': contacts_all})

    def post(self, request):
        ContactInfo.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            address=request.POST.get('address')
        )
        return redirect('catalog:contacts')
