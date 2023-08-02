from django.shortcuts import render, get_object_or_404, redirect
from .models import *

from .forms import *
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity

# =======================================<< Index View >>=======================================
def index(request):
    pass


# =======================================<< Product List View >>=======================================
def product_list(request):
    products = Product.published.all()
    context = {
        'products': products
    }
    return render(request, 'product/list.html', context)


# =======================================<< Product Detail View >>=======================================
def product_detail(request, id):
    product = get_object_or_404(Product, status=Product.Status.PUBLISHED, id=id)
    comments = product.comments.filter(active=True).order_by('-create')
    context = {
        'product': product,
        'comments': comments,
    }
    print(comments)
    return render(request, 'product/detail.html', context)


# =======================================<< Post Comment View >>=======================================
def product_search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            # search_vector = SearchVector('brand', 'engine_type')
            # search_query = SearchQuery(query)
            # search_rank = SearchRank(search_vector, search_query)
            # results = Product.published.annotate(search=search_vector, rank=search_rank)\
            #     .filter(search=search_query).order_by('-rank')

            results_1 = Product.published.annotate(similarity=TrigramSimilarity('engine_type', query))\
                .filter(similarity__gt=0.2)
            results_2 = Product.published.annotate(similarity=TrigramSimilarity('dial_type', query))\
                .filter(similarity__gt=0.2)
            # results_3 = Product.objects.annotate(similarity=TrigramSimilarity('brand', query))\
            #     .filter(similarity__gt=0.2, status=Product.Status.PUBLISHED)
            results_4 = Product.published.annotate(similarity=TrigramSimilarity('sex', query))\
                .filter(similarity__gt=0.2)

            results = (results_1 | results_2 | results_4).order_by('-similarity')

            print(results)

        context = {
            'query': query,
            'products': results
        }

        return render(request, 'product/list.html', context)


# =======================================<< Post Comment View >>=======================================
@require_POST
def product_comment(request, id):
    product = get_object_or_404(Product, id=id)
    comment = None
    form = CommentForm(data=request.POST)
    print(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.save()
        return redirect('product:product_detail', product.id)

    context = {
        'product': product,
        'form': form,
        'comment': comment,
    }
    return render(request, 'forms/comment.html', context)


# =====================================<< Ticket View >>=====================================
def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Ticket.objects.create(
                name=cd['name'],
                email=cd['email'],
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

