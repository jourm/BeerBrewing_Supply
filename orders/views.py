from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def orders(request):
    return render(request, 'orders/orders.html')


@csrf_exempt
def register_order(request):
    print('RECEIVED REQUEST =)')
    print(request.method)
    print('\n*HEADERS')
    print(request.headers)
    print('\n*BODY')
    print(request.body)
    if request.POST:
        print(request.POST, request.headers)

    return render(request, 'orders/orders.html')
