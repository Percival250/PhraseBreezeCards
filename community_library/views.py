from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models, forms
from django.contrib.auth.models import User
from django.utils.text import slugify
import main_app.models


def create_set_slug(name, user):
    slug = name.lower().replace(' ', '-')
    num = 1
    while slug in main_app.models.Set.objects.filter(user=user).values_list('slug', flat=True):
        slug = slugify(name)
        slug += f'- {num}'
        num += 1
    return slug


def library_view(request):
    if request.method == 'GET':
        sets = models.Set.objects.filter(is_published=True)
        template_name = 'community_library/library.html'
        context = {'sets': sets}
        return render(request, template_name, context)


def set_view(request, username, set_slug):
    if request.method == 'GET':
        user = get_object_or_404(User, username=username)
        set = get_object_or_404(models.Set, slug=set_slug, user=user)
        cards = set.library_cards.all()
        cards_count = set.library_cards.count()
        template_name = 'community_library/set.html'
        context = {
            'set': set,
            'cards': cards,
            'username': username,
            'cards_count': cards_count
        }
        return render(request, template_name, context)


def copy_set_view(request, username, set_slug):
    set_user = get_object_or_404(User, username=username)
    set = get_object_or_404(models.Set, slug=set_slug, user=set_user)
    if request.method == 'POST':
        form = forms.CopySetForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            slug = create_set_slug(name, request.user)
            new_set = main_app.models.Set(
                name=name,
                slug=slug,
                user=request.user,
            )
            new_set.save()
            set.downloads += 1
            set.save()
            for card in set.library_cards.all():
                front_side = card.front_side
                back_side = card.back_side
                new_card = main_app.models.Card(
                    front_side=front_side,
                    back_side=back_side,
                    set=new_set
                )
                new_card.save()
            return redirect('set', slug)
    else:
        form = forms.CopySetForm(request.POST, request.FILES)

    template_name = 'community_library/copy_set.html'
    context = {
        'form': form,
        'set': set,
        'username': username
    }
    return render(request, template_name, context)
