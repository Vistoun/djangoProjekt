from django.shortcuts import render
from django.views.generic.detail import DetailView

from opravy.models import Oprava, Model, Opravar

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_models = Model.objects.all().count()
    models = Model.objects.all()

    context = {
        'num_models': num_models,
        'models': models
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ModelDetailView(DetailView):
    model = Model

    context_object_name = 'model_detail'   # your own name for the list as a template variable
    template_name = 'model/detail.html'  # Specify your own template name/location