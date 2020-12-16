import django_filters
from .models import Practice, Category


class PracticeFilter(django_filters.FilterSet):

    class Meta:
        model = Practice
        fields = {'title': ['icontains'],
                  'category': ['exact']}
