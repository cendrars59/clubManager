from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import PracticeCreateView, PracticeDetailView, PracticesListView

urlpatterns = [
    path("", views.sessions, name="sessions"),
    path("practices/", PracticesListView.as_view(), name="pratices"),
    path("practices/practice/<int:pk>/", PracticeDetailView.as_view(), name="practice-details"),
    path("practices/practice/new/", PracticeCreateView.as_view(), name="practice-new"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
