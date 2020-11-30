import django_filters
from django_filters import DateRangeFilter, DateFilter
from .models import Tracking
from django import forms

class TrackingFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name='workDate', lookup_expr=('gt'),
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker_start',
                'type': 'text'}))
    end_date = DateFilter(
        field_name='workDate', lookup_expr=('lt'),
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker_end',
                'type': 'text'}))
    date_range = DateRangeFilter(field_name='workDate')

    class Meta:
        model = Tracking
        fields = ('mood', 'date_range')
