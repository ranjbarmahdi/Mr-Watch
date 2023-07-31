from django.shortcuts import render, get_object_or_404, redirect
from .models import *

from .forms import *
from django.views.decorators.http import require_POST


# =======================================<< Index View >>=======================================
def index(request):
    pass


# =======================================<< Product List View >>=======================================
def product_list(request):
    return render(request, 'product/list.html', {})


# =======================================<< Product Detail View >>=======================================
def product_detail(request, id):
    product = get_object_or_404(Product, status=Product.Status.PUBLISHED, id=id)
    context = {
        'product': product,
    }
    return render(request, 'product/detail.html', context)


# =======================================<< Post Comment View >>=======================================
@require_POST
def product_comment(request, id):
    product = get_object_or_404(Product, satatus=Product.Status.PUBLISHED, id=id)
    comment = None
    form = CommentForm(data=request.POST)
    print(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.save()

    context = {
        'product': product,
        'form': form,
        'comment': comment,
    }
    render(request, 'product/detail.html', context)


# =====================================<< Ticket View >>=====================================
def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Ticket.objects.create(
                name=cd['name'],
                email=cd['email'],
                phone=cd['phone'],
                subject=cd['subject'],
                message=cd['message']
            )
            redirect('product:index')
    else:
        form = TicketForm()
    context = {
        'form': form
    }
    return render(request, 'product/contact-us.html', context)

