from django.urls import path


from .views import index, get_detail, app_form, new_form

urlpatterns = [
    path("", index, name="index"),
    path("post/add/", app_form, name="apps"),
    path("post/new-form/", new_form, name="new-form"),
    path("post/<int:id>/", get_detail, name="detail"),
]