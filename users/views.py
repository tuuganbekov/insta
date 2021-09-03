from django import forms
from django.db.models import Q
from django.shortcuts import render, redirect

from insta.models import User
from users.forms import SearchForm, ProfileModelForm, NewSearch
from users.models import Profile


def search(request):

    name = request.GET.get("name", None)
    print(name)
    users = None

    if name:
        users = User.objects.filter(username__icontains=name)

    if not users:
        users = User.objects.all()

    form = SearchForm
    return render(request, 'users/search.html', locals())


def users_profile(request, id):
    file = Profile.objects.get(pk=id)
    return render(request, "users/profile.html", locals())


def model_form_create(request):
    form = ProfileModelForm
    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            new_profile = form.save()
            return redirect('model')
    return render(request, 'users/model_form.html', locals())


def new_search(request):
    form = NewSearch
    print(form)
    search = request.GET.get('text', None)
    # users = User.objects.none()
    if search:
        first_name = Q(first_name__icontains=search)
        last_name = Q(last_name__icontains=search)
        seart = None
        search_by = request.GET.getlist('search_by')
        print(search_by)
        if 'first_name' in search_by and 'last_name' in search_by:
            seart = first_name | last_name
        elif 'first_name' in search_by:
            seart = first_name
        elif 'last_name' in search_by:
            seart = last_name
        else:
            raise forms.ValidationError("Чекбоксы не должны быть пустыми")
        users = User.objects.filter(seart)
    return render(request, "users/new.html", locals())