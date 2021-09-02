from django.shortcuts import render, redirect

from insta.forms import MyForm
from insta.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'insta/index.html', locals())


def get_detail(request, id):
    detail = Post.objects.get(pk=id)
    print(detail)
    return render(request, 'insta/detail.html', locals())


def app_form(request):
    # request

    if request.method == "POST":
        title = request.POST.get("title")
        descr = request.POST.get("desc")
        class_ = Post
        if title and descr:
            class_.objects.create(
                title=title,
                descr=descr,
            )
            return redirect("index")

    return render(request, 'insta/app_form.html', locals())

def new_form(request):
    form = MyForm
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data['title']
            desc = form.cleaned_data['descr']
            # print(title, desc)
            Post.objects.create(title=title, descr=desc)
            return redirect('index')
    return render(request, 'insta/new_form.html', locals())