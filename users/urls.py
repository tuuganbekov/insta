from django.urls import path

from users.views import search, users_profile, model_form_create, new_search

urlpatterns = [
    path("profile/<int:id>/", users_profile, name='profile'),
    path("search/", search, name='search'),
    path("new-search/", new_search, name='new_search'),
    path("model-form/", model_form_create, name='model'),
]