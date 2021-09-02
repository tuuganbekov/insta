from django.shortcuts import render, redirect

from insta.models import User
from users.forms import SearchForm, ProfileModelForm
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