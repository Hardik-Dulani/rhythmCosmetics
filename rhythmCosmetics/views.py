from django.shortcuts import render,redirect
from .models import Product,Contact,Order
from math import ceil
# Create your views here.
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from Paytm import Checksum
from django.contrib.auth.models import User
from django.contrib.auth  import logout
from django.contrib import messages
import requests



def get_user_email(access_token):
    r = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            params={'access_token': 'https://oauth2.googleapis.com/token'})
    return r.json()



def index(request):
    print(User)
    allProds = Product.objects.values()
    params = {'allProds':allProds}
    return render(request, 'index.html', params)




def about(request):
    return render(request, 'about.html')




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        query = request.POST.get('query','')
        contact=Contact(name=name,email=email,phone=phone,query=query)
        contact.save()
        thank=True
        return render(request, 'contact.html', {'thank':thank})
    return render(request, 'contact.html')



def orders(request):

    this_user =0
    try:
        this_user = request.user.email
        Orders = Order.objects.filter(email = this_user)
        allOrders= [order for order in Orders]
        allOrders=allOrders[::-1]


    except:
        allOrders = ""
    count = len(allOrders)
    params = {'allOrders':allOrders,'count':count}
    return render(request, 'orders.html', params)





def searchMatch(query, item):
    if query.lower() in item['product_name'].lower() or query.lower() in item['category'].lower()  or query.lower() in item['subcategory'].lower():
        return True
    else:
        return False



def search(request):
    query= request.GET.get('search')
    allProds = Product.objects.values()
    prod=[item for item in allProds if searchMatch(query, item)]
    params = {'allProds':prod,'number_results':len(prod),'search_query':query}
    return render(request, 'search.html', params)





def productview(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'prodview.html',{'product':product[0],'id':myid})

def orderview(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'prodview.html',{'product':product[0],'id':myid})



def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        email = request.POST.get('email','')
        address = request.POST.get('address','') + "  "+request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        payment_ref = request.POST.get('utr','')
        primary_prod = request.POST.get('primary_prod','')
        order=Order(items_json=itemsJson,
                     name=name,
                     email=email,
                     phone=phone,
                     address=address,
                     city=city,
                     state=state,
                     zip_code=zip_code,
                     amount=amount,
                     payment_conf = 0,
                     payment_ref=payment_ref,
                     dispatched = 0,
                     link = "0",
                     primary_prod="0")
        order.save()

        thank=True
        id=order.order_id

        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    return render(request,'checkout.html')




def cart_view(request):
    return render(request, 'cart.html')



def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

# @csrf_exempt
def get_user_email(access_token):
    r = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            params={'access_token': 'https://oauth2.googleapis.com/token'})
    return r.json()
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     # verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'paymentstatus.html', {'response': response_dict})

