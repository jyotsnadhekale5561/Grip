from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
# model imports
from .models import customers,Transfer
# Create your views here.
def home_veiw(request):
    return render(request,'Banking Home.html')

def transfer(request,pk):
    user = get_object_or_404(customers,pk=pk)
    cont = customers.objects.all()
    if request.method == "POST":
        name = user.name
        amount = int(request.POST.get('amount'))
        reciver_id = request.POST.get('reciver')
        reciver = get_object_or_404(customers,pk=reciver_id)
        if user.balance > amount:
            reciver.balance = reciver.balance+amount
            user.balance = user.balance-amount
        else:
            return HttpResponse("<h3><i>Not enough amount</i></h3>")
        t = Transfer(name=user,revicer=str(reciver.name),send=amount)
        t.revicer = reciver.name
        t.save()
        user.save()
        return HttpResponseRedirect(reverse('bank_site:Home'))
    return render(request,'view_one.html',context={'customers':cont,'user':user})

def view_all(request):
    cont = customers.objects.all()
    return render(request,'view_all.html',context={'customers':cont})

def view_all_transfers(request):
    transfers = Transfer.objects.all()
    return render(request,'transfers.html',context={'transfers':transfers})




