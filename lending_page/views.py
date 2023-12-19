from django.shortcuts import render
from .models import Lending, Advantages, Feature
# Create your views here.
def lending_page_view(request):
    if request.method == 'GET':
        lending_list = Lending.objects.all()
        advantages_list = Advantages.objects.all()
        features_list = Feature.objects.all()
        context = {
            'lending_list': lending_list,
            'advantages_list': advantages_list,
            'features_list': features_list,
            }
        template_name = 'lending_page.html'
        return render(request, template_name, context)

