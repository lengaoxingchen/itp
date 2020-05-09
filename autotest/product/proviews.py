from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def product_manage(request):
    username = request.session.get('user', '')
    product_list = Product.objects.all()
    product_count = Product.objects.all().count()  # 统计产品数
    paginator = Paginator(product_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        product_list = paginator.page(currentPage)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    return render(request, 'product_manage.html',
                  {'user': username, 'products': product_list, 'product_count': product_count})


@login_required
def product_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('product_name', '')
    product_list = Product.objects.filter(product_name__icontains=search_name)
    return render(request, 'product_manage.html', {'user': username, 'products': product_list})
