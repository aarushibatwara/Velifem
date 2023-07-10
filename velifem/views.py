from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . forms import SOS, Adoption, Donation
from django.contrib import messages
#from django.contrib.auth import authenticate, login
#from .forms import Registration, Login


# Create your views here.

def home(request):
  template = loader.get_template('NGO1stpage.html')
  return HttpResponse(template.render({},request))

def about(request):
  template = loader.get_template('NGOAboutus.html')
  return HttpResponse(template.render({},request))

def adopt(request):
  template = loader.get_template('NGOAdoptpage.html')
  return HttpResponse(template.render({},request))

def adoptreq(request):
  template = loader.get_template('NGOAdoptreqpage.html')
  return HttpResponse(template.render({},request))

def career(request):
  template = loader.get_template('NGOCareers.html')
  return HttpResponse(template.render({},request))

def contactus(request):
  template = loader.get_template('NGOContactus.html')
  return HttpResponse(template.render({},request))

def fund(request):
  template = loader.get_template('NGOFund.html')
  return HttpResponse(template.render({},request))

def issues(request):
  template = loader.get_template('NGOissuespage.html')
  return HttpResponse(template.render({},request))

def thankyou(request):
  template = loader.get_template('NGOThankyoupage.html')
  return HttpResponse(template.render({},request))

def volunteer(request):
  template = loader.get_template('NGOVolunteer.html')
  return HttpResponse(template.render({},request))


def sos_submit(request):
    if request.method == 'POST':
        form = SOS(request.POST, request.FILES)
        if form.is_valid():
            print("Valid Saved")
            form.save()
            # form.clean()
        else:
           print("Invalid")
           print(form.errors)
    else:
        print("Submit button issue")
        form = SOS()
    return render(request, 'SOS.html', {'form': form})


def adoption(request):
    if request.method == 'POST':
        form = Adoption(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for submitting the adoption form!')
            print("Im SOrry")
            return redirect('/templates/NGOAdoptreqpage/')
        else:
           print(form.errors)
    else:
        print("ffffffffffffffffffff")
        form = Adoption()
    return render(request, 'NGOAdoptform.html', {'form': form})

# def donation(request):
#     if request.method == 'POST':
#         form = Donation(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = Donation()  # clear the form
#             message = 'Thank you for your donation!'
#             print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
#         else:
#            print("ggggggggggggggggggggggggggggggggggccccccccccccccc")
#     else:
        
#         form = Donation()
        
#         message = ''
#     return render(request, 'NGODonatepage.html', {'form': form, 'message': message})



def donate(request):
    if request.method == 'POST':
        form = Donation(request.POST)
        if form.is_valid():
            form.save()
            print("valid")
            return redirect('/templates/NGOThankyoupage/')  # replace with your actual thank you page URL
        else:
           print(form.errors)
           print("ggggggggggggggggggggggggggggg")
    else:
      print("ffddddddddddddddddddddddddddd")
      form = Donation()
    return render(request, 'NGODonatepage.html', {'form': form})





"""def register(request):
     if request.method == 'POST':
         form = Registration(request.POST)
         if form.is_valid():
             print("Valid Saved")
             user = form.save()
             
             # Log the user in.
             login(request, user)
             return redirect('templates/NGO1stpage/')
         else:
            print("Invalid")
     else:
      
        print("Submit button issue")
        form = Registration()
     return render(request, 'loginregisterform.html', {'form': form})

def login(request):
     if request.method == 'POST':
         form = Login(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             user = authenticate(request, user_id=cd['user_id'], password=cd['password'])
             if user is not None:
                 login(request, user)
                 return redirect('templates/NGO1stpage/')
             else:
                 return render(request, 'loginregisterform.html', {'form': form, 'invalid_creds': True})
     else:
         form = Login()
     return render(request, 'loginregisterform.html', {'form': form})"""