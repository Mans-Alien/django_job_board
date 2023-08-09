import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    discription = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job 
        fields = ['category', 'title', 'job_type', 'salary', 'ex_years', 'discription']