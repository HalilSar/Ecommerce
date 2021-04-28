from django.shortcuts import render,HttpResponseRedirect
from .models import Setting,ContactForm,ContactFormMessage
from product.models import Product 
def Index(request):
    settings=Setting.objects.get(id=1)
    sliderdata = Product.objects.all()[:4]
    context = {
        'settings':settings, 'sliderdata':sliderdata, 'page': 'home'
    }
    return render(request,'home/home.html',context)
def aboutus(request):
    settings=Setting.objects.get(id=1)
    context = {
        'settings':settings,
    }
    return render(request,'home/aboutus.html',context)
  
def reference(request):
    settings=Setting.objects.get(id=1)
    context = {
        'settings':settings,
    }
    return render(request,'home/reference.html',context)

def contact(request):
   if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()  #save data to table
            # messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')
   else:      
        form = ContactForm
        settings=Setting.objects.get(id=1)
        context={'settings':settings,'form':form  }
        return render(request, 'home/contact.html', context)        