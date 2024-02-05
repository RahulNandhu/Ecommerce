from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import Cart,Account,Order

# Create your views here.
@login_required
def cartview(request):
    u=request.user
    cart=Cart.objects.filter(user=u)
    amount=0
    for i in cart:
        amount +=i.quantity * i.product.price
    return render(request,template_name='cart.html',context={'cart':cart,'total':amount})

@login_required
def addtocart(request,p):
    pr = Product.objects.get(name=p)
    u=request.user
    try:
        cart = Cart.objects.get(product=pr, user=u)
        if (cart.quantity<pr.stock):
            cart.quantity +=1
            cart.save()
            return cartview(request)
    except:
        if (pr.stock >0):
            cart=Cart.objects.create(product=pr,user=u,quantity=1)
            cart.save()
            return cartview(request)
        else:
            return HttpResponse('Currently Not available')
    return cartview(request)

@login_required()
def add_cart(request,p):
    u=request.user
    pr=Product.objects.get(name=p)

    try:
        cart=Cart.objects.get(user=u,product=pr)
        if (cart.quantity<cart.product.stock):
            cart.quantity +=1
            cart.save()
            return cartview(request)
    except:
        HttpResponse('exceeded the stock')
    return cartview(request)

@login_required()
def remove_cart(request,p):
    u=request.user
    pr=Product.objects.get(name=p)
    cart = Cart.objects.get(user=u, product=pr)
    try:
        if cart.quantity >1:
            cart.quantity -=1
            cart.save()
            return cartview(request)
        else:
            cart.delete()
            return cartview(request)
    except:
        return cartview(request)

    
@login_required
def delete_cart(request,p):
    u=request.user
    pr=Product.objects.get(name=p)
    try:
        cart=Cart.objects.get(user=u,product=pr)
        cart.delete()
        return cartview(request)
    except:
        return cartview(request)

@login_required
def order(request):
    if request.method=='POST':
        p=request.POST['ph']
        a=request.POST['ad']
        u=request.user
        acc=request.POST['acc']
        cart=Cart.objects.filter(user=u)
        total=0

        try:
            ac = Account.objects.get(acc_no=acc)
            for i in cart:
                total +=i.quantity * i.product.price
            if ac.amount > total:
                ac.amount -=total
                ac.save()
                for i in cart:
                    pr=Order.objects.create(user=u,product=i.product,amount=i.product.price,no_of_item=i.quantity,address=a,phone=p,order_status='ordered')
                    pr.save()
                    msg='item ordered'
                return render(request,template_name='order_clar.html',context={'msg':msg})

            else:
                print(ac.amount)
                msg='Insufficient Balance'
                return render(request,template_name='order_clar.html',context={'msg':msg})

        except:
            msg='Invalid bank details'
            return render(request, template_name='order_clar.html', context={'msg': msg})
    return render(request,template_name='order.html')

@login_required
def order_view(request):
    u=request.user
    items=Order.objects.filter(user=u)
    return render(request,template_name='order_view.html',context={'j':items})


