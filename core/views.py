from django.shortcuts import render, HttpResponse
from .forms import *

# Create your views here.



def info(request):
    return render(request,
                  'info.html',
                  {'info': Product.objects.all()})


def product_update(request, id):
    context = {}
    client_object = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=client_object)

        if form.is_valid():
            client_object = form.save()
        else:
            return HttpResponse('не валидно')

    context["form"] = ProductForm(instance=client_object)
    return render(request, 'product_update.html', context)




def product_delete(request, id):
    global product
    context = {}
    order_object = Product.objects.get(id=id)
    if request.method == 'POST':
        order_object.delete()
        product = ProductDeleteForm(request.POST, instance=order_object)

    context['product'] = ProductDeleteForm(instance=product)
    return render(request, 'product_delete.html', context)


def productViews(request):
    if request.method == "POST":
        data = request.POST
        product = Product()
        product.name = data["name"]
        product.pirce = data["price"]
        product.photo = data["photo"]
        product.save()
        return HttpResponse("Форма обработана")
    return render(request, 'client.html')