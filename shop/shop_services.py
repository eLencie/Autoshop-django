from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Good, Invoice
from .forms import InvoiceFormSet


@login_required(login_url='login')
def invoice_create_new(request):
	""" Creating new invoice instance, saving it and then associating gooditems with it through F-keys """

	if request.method == 'GET':
		formset = InvoiceFormSet(queryset=Invoice.objects.none())
	elif request.method == 'POST':
		new_invoice = Invoice()
		formset = InvoiceFormSet(request.POST, instance=new_invoice)
		instances = formset.save(commit=False)
		if instances:  # Проверка на наличие хоть одной заполненной формы. Переопределять правила валидации
			# inline-объектов (gooditem) не вариант из-за особенностей устройства formset'ов (из-за extra полностью
			# пустые формы игнорируются при валидации)
			for instance in instances:
				price = instance.item.retail_price
				instance.price = price
			new_invoice.author = request.user
			new_invoice.save()
			formset.save()
			return redirect(new_invoice.get_absolute_url())
		else:
			messages.error(request, 'Add at least one item!')
	return render(request, 'shop/invoice_create.html', {'formset': formset})


