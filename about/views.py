from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import InquiryForm
from .models import About


class AboutDetailView(DetailView):
    """
    Renders About information on the website
    and allows user to send thier inquiries.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent updated instance of :model:`about.About`.
    ``inquiry_form``
        An instance of :form:`about.InquiryForm`.

    **Template**
    :template:`about/about.html`
    """
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about'

    def get_object(self):
        return About.objects.all().order_by('-updated_on').first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inquiry_form'] = InquiryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        inquiry_form = InquiryForm(request.POST)
        if inquiry_form.is_valid():
            inquiry_form.save()
            messages.add_message(
                    self.request, messages.SUCCESS,
                    'Inquiry sent successfuly.'
            )
            return redirect('about')
        context = self.get_context_data()
        context['inquiry_form'] = inquiry_form
        return self.render_to_response(context)
