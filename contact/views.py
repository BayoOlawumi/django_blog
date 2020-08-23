from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.clean_data['topic']
            message = form.clean_data['message']
            sender = form.clean_data['sender']
            send_mail(
                "Feedback from your website eBayo %s"
                 % topic, message, sender,['olawumiebayo@gmail.com'])
            return HttpResponseRedirect('/contact/thanks/')

    else:
        form = ContactForm()
    return render(request,'contact.html', {'form': form})
