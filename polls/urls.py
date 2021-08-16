from django.urls import path
from django.urls.resolvers import RoutePattern
from . import views


# the path function takes four argments.
# 1) route 2) view -> when dhango finds the regular expression, it calls the specified view function.
# in the case, call the value caputured from route with the HttpRewuest object
#  as the first argument and as the keyword arguments.
#  3) name -> if you give the URL a name, cleary refer to it from anywhere in django.
# especially useful in templates
app_name="polls"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("<int:question_id>/", views.detail, name="detail"),
#     path("<int:question_id>/results/", views.results, name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote")
# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]
