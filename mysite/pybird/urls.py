from django.urls import path

from . import views

urlpatterns = [
    # ex: /pybird/
    path("", views.index, name="index"),
    # ex: /pybird/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /pybird/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /pybird/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]