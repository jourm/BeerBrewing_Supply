from django.shortcuts import render

# Create your views here.


def checkout(request):
    print('checkout')
    return render(request, 'checkout/checkout.html')


def terms(request):
    print('terms')
    return render(request, 'checkout/terms.html')


def completed(request):
    print('checkout_success')
    return render(request, 'checkout/completed.html')
