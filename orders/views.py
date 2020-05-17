from django.shortcuts import render

# Create your views here.


def orders(request):
    return render(request, 'orders/orders.html')


def register_order(request):
    if request.POST:
        print(request.POST)

    return render(request, 'orders/orders.html')

