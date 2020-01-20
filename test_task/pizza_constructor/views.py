from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from .forms import ProductForm, ProductFormset, RegisterForm
from .models import Category, Product
from test_task import settings


def home(request):
    products_list = Product.objects.order_by('id')
    formset = ProductFormset(initial=products_list.values())
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        formset = ProductFormset(request.POST, initial=products_list.values())
        if formset.is_valid():
            request.session['total_price'] = float(formset.get_total_price())
            request.session['pastry'] = request.POST.get('pastry')

            request.session['prod_name'] = formset.get_prod_list()
            return redirect(reverse('registration'))

    context = {
        'formset': formset,
    }

    return render(request, 'pizza_constructor/home.html', context)


def register(request):
    if 'total_price' not in request.session:
        return redirect(reverse('home'))
    form = RegisterForm(initial={'total_price': request.session['total_price'],
                                 'pastry': request.session['pastry'],
                                 'prod_name': request.session['prod_name']
                                 })

    context = {
        'form': form
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        total_price = request.POST.get('total_price')
        pastry = request.POST.get('pastry')
        products = request.POST.get('prod_name')

        # SENDING EMAIL
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = f'Добрый день, {name}.\nВаш заказ будет отправлен в ближайшее время.\n' \
                  f'Подробности заказа:\nТесто: {pastry}\nИнгридиенты: {products}\nСумма заказа: {total_price}$.'
        email = EmailMessage(subject=name, body=message, to=recipient_list, from_email=email_from, )
        email.send()
        return render(request, 'pizza_constructor/successful_order.html')
    return render(request, 'pizza_constructor/registration.html', context)
