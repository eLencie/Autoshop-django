from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer

from .serializers import *
from shop.models import *
from rest_framework import viewsets, generics


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.prefetch_related('gooditem_set__item').select_related('author')
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, ]


