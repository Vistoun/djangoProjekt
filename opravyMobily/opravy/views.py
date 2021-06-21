from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from opravy.forms import ModelForm
from opravy.models import Brand, Oprava, Model, Opravar

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_models = Model.objects.all().count()
    models = Model.objects.all()
    brands = Brand.objects.all()
    

    context = {
        'num_models': num_models,
        'models': models,
        'brands': brands,
    
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ModelListView(ListView):
    model = Model

    context_object_name = 'models_list'   # your own name for the list as a template variable
    template_name = 'model/list.html'  # Specify your own template name/location
    #paginate_by = 3

    def get_queryset(self):
        if 'brand_name' in self.kwargs:
            print("brand_name")
            return Model.objects.filter(znacka__name__contains=self.kwargs['brand_name']).all() # Get 5 books containing the title war
        else:
            return Model.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_models'] = len(self.get_queryset())
        context['brands'] = Brand.objects.all()
        #context['models'] = Model.objects.all()
        """
        if 'brand_name' in self.kwargs:
            context['view_title'] = f"Žánr: {self.kwargs['genre_name']}"
            context['view_head'] = f"Žánr filmu: {self.kwargs['genre_name']}"
        else:
            context['view_title'] = 'Filmy'
            context['view_head'] = 'Přehled filmů'
        """    
        return context


class ModelDetailView(DetailView):
    model = Model

    context_object_name = 'model_detail'   # your own name for the list as a template variable
    template_name = 'model/detail.html'  # Specify your own template name/location


class BrandListView(ListView):
    model = Brand

    content_object_name = 'brands'
    template_name = 'brand/brand_list.html'
    queryset = Brand.objects.order_by('name').all()

class OpravarAbout(TemplateView): 
    model = Opravar

    context_object_name = 'opravari'   # your own name for the list as a template variable
    template_name = 'opravar/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['opravari'] = Opravar.objects.all()
        return context

class ModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Model
    fields = ['name', 'znacka', 'fotka', 'cena_baterka', 'cena_displej', 'cena_stav_a', 'popis']
    login_url = '/accounts/login/'
    permission_required = 'opravy.add_model'

class ModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Model
    template_name = 'model/form_edit.html'
    form_class = ModelForm
    login_url = '/accounts/login/'
    permission_required = 'opravy.change_model'

    #fields = '__all__' # Not recommended (potential security issue if more fields added)


class ModelDelete( LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Model
    success_url = reverse_lazy('index')
    login_url = '/accounts/login/'
    permission_required = 'opravy.delete_model'

