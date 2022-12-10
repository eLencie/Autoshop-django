from django.forms import *
from .models import Good, Invoice, GoodItem


InvoiceFormSet = inlineformset_factory(Invoice, GoodItem, fields=('item', 'quantity', 'invoice'), extra=3,
                                       can_delete=False)


