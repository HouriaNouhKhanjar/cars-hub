from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import InquiryForm


# Test about views
class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", description="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_inquiry_form(self):
        """Verifies get request for about me containing an inquiry form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['inquiry_form'], InquiryForm)

    def test_successful_inquiry_request_submission(self):
        """Test for a user requesting an inquiry"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Inquiry sent successfuly." in str(m) for m in messages
            ))
