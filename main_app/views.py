from django.shortcuts import render, get_object_or_404, redirect
import community_library.models
from . import models, forms
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib import messages
import random


def create_set_slug(name, user):
    slug = name.lower().replace(' ', '-')
    num = 1
    while slug in models.Set.objects.filter(user=user).values_list('slug', flat=True):
        slug = slugify(name)
        slug += f'-{num}'
        num += 1
    return slug


def create_library_set_slug(name, user):
    slug = name.lower().replace(' ', '-')
    num = 1
    while slug in community_library.models.Set.objects.filter(user=user).values_list('slug', flat=True):
        slug = slugify(name)
        slug += f'-{num}'
        num += 1
    return slug


# def lending_page(request):
#     if request.method == 'GET':
#         return render(request, template_name='lending_page.html')
@login_required
def main_view(request):
    if request.method == 'GET':
        user_id = request.user.id
        sets = models.Set.objects.filter(user=request.user)
        template_name = 'main_app/main.html'
        context = {
            'sets': sets,
            'user_id': user_id
        }
        return render(request, template_name, context)


def set_view(request, set_slug):
    if request.method == 'GET':
        user = request.user
        set = get_object_or_404(models.Set, slug=set_slug, user=user)
        cards_count = set.cards.count()
        template_name = 'main_app/set/set.html'
        context = {
            'set': set,
            'cards_count': cards_count
        }
        return render(request, template_name, context)


def create_set_view(request):
    user = request.user
    if request.method == 'POST':
        form = forms.SetForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not models.Set.objects.filter(user=user, name=name).exists():
                slug = create_set_slug(name, user)
                new_set = models.Set(name=name, slug=slug, user=user)
                new_set.save()
                return redirect('user_library')
            else:
                return redirect('create_new_set')
    else:
        form = forms.SetForm(request.POST, request.FILES)

    template_name = 'main_app/set/set_crud/create_set.html'
    context = {'form': form}
    return render(request,  template_name, context)


def create_new_set_view(request):
    user = request.user
    if request.method == 'POST':
        form = forms.SetExistsForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not models.Set.objects.filter(user=user, name=name).exists():
                slug = create_set_slug(name, user)
                new_set = models.Set(name=name, slug=slug, user=user)
                new_set.save()
                return redirect('your_library')
            else:
                return redirect('create_new_set')
    else:
        form = forms.SetExistsForm(request.POST, request.FILES)

    template_name = 'main_app/set/set_crud/create_new_set.html'
    context = {'form': form}
    return render(request,  template_name, context)


def delete_set_confirm_view(request, set_slug):
    if request.method == 'GET':
        set = get_object_or_404(models.Set, slug=set_slug, user=request.user)
        template_name = 'main_app/set/set_crud/delete_set_confirm.html'
        context = {'set': set}
        return render(request, template_name, context)


def delete_set(request, set_slug):
    if request.method == 'GET':
        set = get_object_or_404(models.Set, slug=set_slug, user=request.user)
        set.delete()
        return redirect('user_library')


def rename_set_view(request, set_slug):
    set = get_object_or_404(models.Set, slug=set_slug, user=request.user)
    if request.method == 'POST':
        form = forms.SetForm(instance=set, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('set', set_slug)
    else:
        form = forms.SetForm(instance=set)

    template_name = 'main_app/set/set_crud/rename_set.html'
    context = {
        'set': set,
        'form': form
    }
    return render(request, template_name, context)


def learn_cards_view(request, set_slug):
    set = get_object_or_404(models.Set, user=request.user, slug=set_slug)
    all_cards = list(models.Card.objects.filter(set=set))
    random.shuffle(all_cards)
    context = {
        'all_cards': all_cards,
    }

    return render(request, 'main_app/card/learn_cards.html', context)


def create_card_view(request, set_slug):
    set = get_object_or_404(models.Set, slug=set_slug, user=request.user)
    if request.method == 'POST':
        form = forms.CardForm(request.POST, request.FILES)
        if form.is_valid():
            front_side = form.cleaned_data['front_side']
            back_side = form.cleaned_data['back_side']
            create_reverse_card = form.cleaned_data['create_reverse_card']
            new_card = models.Card(
                front_side=front_side,
                back_side=back_side,
                create_reverse_card=create_reverse_card,
                set=set
            )
            new_card.save()
            if create_reverse_card:
                reverse_new_card = models.Card(
                    front_side=back_side,
                    back_side=front_side,
                    create_reverse_card=False,
                    set=set
                )
                reverse_new_card.save()
            if new_card:
                return redirect('set', set_slug)
    else:
        form = forms.CardForm(request.POST, request.FILES)

    template_name = 'main_app/card/card_crud/create_card.html'
    context = {
        'form': form,
        'set': set
    }
    return render(request, template_name, context)


def set_cards_view(request, set_slug):
    if request.method == 'GET':
        set = get_object_or_404(models.Set, slug=set_slug, user=request.user)
        cards = set.cards.all()
        template_name = 'main_app/set/set_cards.html'
        context = {
            'set': set,
            'cards': cards
        }
        return render(request, template_name, context)


def edit_card_view(request, set_slug, card_id):
    set = get_object_or_404(models.Set, slug=set_slug, user=request.user)
    card = get_object_or_404(models.Card, id=card_id)
    if request.method == 'GET':
        referring_url = request.META.get('HTTP_REFERER', None)
        print(referring_url)
        form = forms.EditCardForm(instance=card)
    elif request.method == 'POST':
        referring_url = request.META.get('HTTP_REFERER', None)
        referring_url = referring_url[:len(referring_url) - 1]
        referring_url = referring_url[:referring_url.rfind('/') + 1]
        print(referring_url)
        form = forms.EditCardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect(referring_url)

    template_name = 'main_app/card/card_crud/edit_card.html'
    context = {
        'form': form,
        'set': set,
        'referring_url': referring_url
    }
    return render(request, template_name, context)


def delete_card(request, set_slug, card_id):
    if request.method == 'GET':
        card = get_object_or_404(models.Card, id=card_id)
        card.delete()
        return redirect('set_cards', set_slug)


def share_set_view(request, set_slug):
    set = get_object_or_404(models.Set, slug=set_slug, user=request.user)
    if request.method == 'POST':
        form = forms.ShareSetForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            slug = create_library_set_slug(name, request.user)
            new_library_set = community_library.models.Set(
                name=name,
                slug=slug,
                user=request.user,
                cards_count=set.cards.count(),
                is_published=False
            )
            new_library_set.save()
            for card in set.cards.all():
                front_side = card.front_side
                back_side = card.back_side
                new_library_card = community_library.models.Card(
                    front_side=front_side,
                    back_side=back_side,
                    set=new_library_set
                )
                new_library_card.save()
            return redirect('share_set_success', set_slug)
    else:
        form = forms.ShareSetForm(request.POST, request.FILES)

    template_name = 'main_app/set/share_set/share_set.html'
    context = {'form': form, 'set': set}
    return render(request, template_name, context)


def share_set_success_view(request, set_slug):
    template_name = 'main_app/set/share_set/share_set_success.html'
    context = {'set_slug': set_slug}
    return render(request, template_name, context)
