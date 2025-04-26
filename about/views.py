from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib import messages
from .models import About
from .forms import InquiryForm


class AboutDetailView(DetailView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about'

    def get_object(self):
        return About.objects.first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InquiryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                    self.request, messages.SUCCESS,
                    'Inquiry sent successfuly.'
            )
            return redirect('about') 
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)