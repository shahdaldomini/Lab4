from django.shortcuts import render
from .models import Product
from django.db.models import Q

def home(request):

    watches = Product.objects.filter(category="Watches")
    rings = Product.objects.filter(category="Rings")
    scarves = Product.objects.filter(category="Scarves")

    all_products = Product.objects.all()


    search = request.GET.get('search')


    if search:

        search = search.lower()


        if "ساعة" in search or "ساعات" in search or "watch" in search:

            all_products = Product.objects.filter(
                category="Watches"
            )


        elif "سكارف" in search or "شال" in search or "scarves" in search:

            all_products = Product.objects.filter(
                category="Scarves"
            )


        elif "خاتم" in search or "خواتم" in search or "ring" in search:

            all_products = Product.objects.filter(
                category="Rings"
            )


        else:

            all_products = Product.objects.filter(
                Q(name__icontains=search) |
                Q(brand__icontains=search) |
                Q(description__icontains=search)
            )

    print("SEARCH:", search)
    print("COUNT:", all_products.count())

    return render(request,'home.html',{
        'all_products': all_products,
        'watches': watches,
        'rings': rings,
        'scarves': scarves,
    })

def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(request, 'product_detail.html', {

        'product': product

    })