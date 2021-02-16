from django.shortcuts import render, redirect
from .Assetsforms import AssetForm
from .Assetcatforms import Assetcatform
from .RegisterForm import RegisterForms
from .models import Asset, AssetCat, Registration


def home(request):
    return render(request, 'asset/home.html')

# -----------------Asset-----------------------------

def viewasset(request):
    assets = Asset.objects.all()
    return render(request, "asset/viewasset.html", {'assets': assets})

def inventory(request):
    assets = Asset.objects.all()
    return render(request, "asset/inventory.html", {'assets': assets})

def deleteasset(request, ids):
    assets = Asset.objects.get(id=ids)
    assets.delete()
    return redirect('/login/viewasset')

def addasset(request):
    assetscat = AssetCat.objects.all()
    if request.method == "POST":
        addassetform = AssetForm(request.POST)
        if addassetform.is_valid():
            try:
                addassetform.save()
                return redirect('/login/viewasset')
            except:
                pass
    else:
        addassetform = AssetForm()
    return render(request, 'asset/addasset.html', {'addassetform': addassetform, 'assetscat': assetscat})

def editasset(request, ids):
    editassetform = Asset.objects.get(id=ids)
    assetscat = AssetCat.objects.all()
    return render(request, 'asset/editasset.html', {'editassetform': editassetform, 'assetscat': assetscat})

def updateasset(request, ids):
    editassetform = Asset.objects.get(id=ids)
    editasset = AssetForm(request.POST, instance=editassetform)
    if editasset.is_valid():
        editasset.save()
        return redirect('/login/viewasset')
    return render(request, 'asset/editasset.html', {'editassetform': editassetform})
# -----------------------------------category--------------------------------------

def viewcat(request):
    assetscat = AssetCat.objects.all()
    return render(request, "asset/viewcat.html", {'assetscat': assetscat})

def deletecat(request, ids):
    assetscat = AssetCat.objects.get(id=ids)
    assetscat.delete()
    return redirect('/login/viewcat')

def addcat(request):
    category = AssetCat.objects.all()
    category_record = []
    for elements in category:
        x = elements.cat_name
        category_record.append(x)
    if request.method == "POST":
        addcatform = Assetcatform(request.POST)
        cat_name = request.POST.get('cat_name')
        if cat_name not in category_record:
            if addcatform.is_valid():
                try:
                    addcatform.save()
                    return redirect('/login/viewcat')
                except:
                    pass
        else:
            note = "Category already exists!!"
            return render(request, 'asset/addcat.html', {'addcatform': addcatform, 'note': note})
    else:
        addcatform = Assetcatform()
    return render(request, 'asset/addcat.html', {'addcatform': addcatform})

def editcat(request, ids):
    editcatform = AssetCat.objects.get(id=ids)
    return render(request, 'asset/editcat.html', {'editcatform': editcatform})

def updatecat(request, ids):
    editcatform = AssetCat.objects.get(id=ids)
    editcat = Assetcatform(request.POST, instance=editcatform)
    if editcat.is_valid():
        editcat.save()
        return redirect('/login/viewcat')
    return render(request, 'asset/editcat.html', {'editcatform': editcatform})

def register(request):
    if request.method == "POST":
        registerform = RegisterForms(request.POST)
        if registerform.is_valid():
            try:
                registerform.save()
                return redirect('/login/')
            except:
                pass
    else:
        registerform = RegisterForms()
    return render(request, "asset/login.html", {'registerform': registerform})

def login(request):
    return render(request, "asset/login.html")

def check(request):
    uname = request.POST.get('username')
    pwd = request.POST.get('password')
    user = Registration.objects.all()
    usersrecord = {}
    for elements in user:
        x = elements.uname
        y = elements.pwd
        usersrecord.update({x: y})
    note = "Username or password does not exists."
    alpha = usersrecord.get(uname, "Not Found ! ")
    if alpha == pwd:
        return render(request, "asset/home.html", {'uname': uname})
    else:
        return render(request, "asset/login.html", {'note': note})