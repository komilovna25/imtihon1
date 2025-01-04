from django.shortcuts import render
from .models import About,Category,Portfolio,Services,Contact
from django.views.generic.edit import FormView
from .forms import ContactForm
from .bot import send_message
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.views.generic.edit import FormView
from .bot import send_message

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm  
    success_url = '/' 

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        
    
        contact = Contact(name=name, email=email)
        contact.save()

        message_text = f"New Contact Form Submission:\n\nName: {name}\nEmail: {email}"
        send_message(message_text)

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



class AboutListView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'

def home_view(request):
    return render(request=request, template_name='index.html')




class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
    



class ServicesListView(ListView):
    model = Services
    template_name = 'services.html'
    context_object_name = 'services'

