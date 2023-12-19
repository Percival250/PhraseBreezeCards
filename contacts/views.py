from django.shortcuts import render
from .models import Contacts
# Create your views here.
def contacts_list_view(request):
    if request.method == 'GET':
        contacts_list = Contacts.objects.all()
        return render(request, template_name='menu/contacts.html', context={'contacts_list': contacts_list})

