from django.contrib.auth import logout
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .filters import GoodsFilter
from .shop_services import invoice_create_new
from .models import Good, Invoice


class UserRegisterView(CreateView):
	form_class = UserCreationForm
	template_name = 'shop/auth/register.html'
	success_url = reverse_lazy('login')


class UserLoginView(LoginView):
	form_class = AuthenticationForm
	template_name = 'shop/auth/login.html'

	def get_success_url(self):
		next_page = self.request.GET.get('next')
		if next_page:
			return next_page
		return reverse_lazy('home')


def user_logout(request):
	logout(request)
	return redirect('login')


class InvoiceListView(ListView):
	model = Invoice
	template_name = 'shop/invoice_list.html'
	paginate_by = 8


class InvoiceDetailView(DetailView):
	model = Invoice
	template_name = 'shop/invoice_detail.html'
	pk_url_kwarg = 'invoice_id'


def invoice_create(request):
	return invoice_create_new(request)


def goods_list(request):
	"""
	Table of goods with filtering
	"""
	good_filter = GoodsFilter(request.GET, queryset=Good.objects.all())
	return render(request, 'shop/goods_list.html', {'filter': good_filter})
