from django.shortcuts import render
from product.models import Product

# Create your views here.
def trending_product(request):
    trending_item=Product.objects.all()
    print(trending_item)
    for t in trending_item:
        if t.season==True:
            
            print(t.name)
        else:
            pass
    return render(request,'templates/home/bags.html')