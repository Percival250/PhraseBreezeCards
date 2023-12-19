from django.shortcuts import render
from .models import Info
# Create your views here.
def info_list_view(request):
    if request.method == 'GET':
        info_list = Info.objects.all()
        return render(request, template_name='menu/about_us.html', context={'info_list': info_list})

