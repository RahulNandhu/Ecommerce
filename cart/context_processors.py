from .models import Cart

def total_item(request):
    t = 0
    if request.user.is_authenticated:
        u=request.user
        try:
            cart=Cart.objects.filter(user=u)
            for i in cart:
                t += i.quantity
        except:
            t=0
    return {'count':t}