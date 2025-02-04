from django.shortcuts import render , redirect , get_object_or_404
from django.http import request , response
from django.views import View
from . models import ClothingProduct , Bag
from django.contrib.auth import logout
def home(req):
    return render(req, 'app/home.html')

class thriftView(View):
    def get(self,request):
        products = ClothingProduct.objects.all()  #
        return render(request, "app/thrift.html", {'products': products})
    
def bags_view(request):
    bags = Bag.objects.all()  #
    return render(request, 'app/bags.html', {'bags': bags})


from .models import Accessory  

def accessories_view(request):
    accessories = Accessory.objects.all() 
    return render(request, 'app/accessories.html', {'accessories': accessories})

from .forms import ClothingForm

def sell_clothing(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('clothing_list')  
    else:
        form = ClothingForm()

    return render(request, 'sell_clothing.html', {'form': form})
