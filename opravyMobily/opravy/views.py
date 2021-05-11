from django.shortcuts import render

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