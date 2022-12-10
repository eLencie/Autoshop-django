import django_filters
from .models import Good


class GoodsFilter(django_filters.FilterSet):
    class Meta:
        model = Good
        fields = ['group', 'name', 'countries__name']

    class Meta:
        model = Good
        fields = {
            'group': ['in'],
            'name': ['icontains'],
            'countries__name': ['in'],
        }