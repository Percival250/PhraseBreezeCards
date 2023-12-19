from django.shortcuts import render
import community_library.models


def home_view(request):
    popular_sets = community_library.models.Set.objects.filter(is_published=True).order_by('downloads')[:3]

    template_name = 'home/home_page.html'
    context = {'popular_sets': popular_sets}
    return render(request, template_name, context)
