# filters.py
import django_filters
from .models import *

class SubmitJobFilter(django_filters.FilterSet):
    work_mode = django_filters.ChoiceFilter(
        choices=SubmitJob.WORK_MODE_CHOICES,  
        label="Work Mode"
    )
    industry = django_filters.CharFilter(
        field_name='industry__industry',  
        lookup_expr='icontains',
        label="Industry"
    )
    city = django_filters.CharFilter(
        field_name='city__name',  
        lookup_expr='icontains',
        label="city"
    )
    job_title = django_filters.CharFilter(
        lookup_expr='icontains',  # Allows for partial matches
        label="Job Title"
    )

    class Meta:
        model = SubmitJob
        fields = ['work_mode', 'industry', 'city','job_title']