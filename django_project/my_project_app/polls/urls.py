
from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('detail/test/<int:pk>', views.DetailsView.as_view(), name="detail"),
    path('vote/<int:question_id>', views.vote, name="vote"),
    path('result/<int:pk>', views.ResultView.as_view(), name="result"),
]
