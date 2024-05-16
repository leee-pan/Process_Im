from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request,list_id):
    list_user = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_user)
    return render(request, 'list.html', {'list': list_user})

def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')

def test_redirects_after_POST(self):
    response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
    new_list = List.objects.first()
    self.assertRedirects(response, f'/lists/{new_list.ed}/')

def add_item(request,list_id):
    list_user = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')