# filters.py
import django_filters
from .models import *
from django.db.models import Q
class SubmitJobFilter(django_filters.FilterSet):
    work_mode = django_filters.ChoiceFilter(
        choices=SubmitJob.WORK_MODE_CHOICES,  
        label="Work Mode"
    )
      # Industry filter (support multiple values)
    industry = django_filters.CharFilter(
        field_name='industry__industry',  # Assumes `industry` is a related model       
        method='filter_industry',         # Custom filter method
        label="Industry"
    )
    job_location = django_filters.CharFilter(
        field_name='job_location__name',  
        method='filter_job_location',     # Custom filter method
        label="Job Location"
    )

    job_title = django_filters.CharFilter(
        lookup_expr='icontains',  # Allows for partial matches
        label="Job Title"
    )
    experience = django_filters.CharFilter(
        lookup_expr='icontains',  # Allows for partial matches
        label="experience"
    )
    def filter_industry(self, queryset, name, value):
        if value:
            industries = value.split(',')
            # Build a Q object for each industry with icontains, then combine with OR
            industry_query = Q()
            for industry in industries:
                industry_query |= Q(industry__industry__icontains=industry)
            queryset = queryset.filter(industry_query)
        return queryset

    
    def filter_job_location(self, queryset, name, value):
        if value:
            # Split job locations by comma
            locations = value.split(',')
            # Filter the queryset to include any of the specified locations
            queryset = queryset.filter(job_location__name__in=locations)
        return queryset

    class Meta:
        model = SubmitJob
        fields = ['work_mode', 'industry', 'job_location','job_title','experience']
