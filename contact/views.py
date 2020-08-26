from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render(request,'contact.html', {'form': form})
