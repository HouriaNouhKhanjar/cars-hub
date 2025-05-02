from django.test import TestCase
from .forms import InquiryForm


# Create tests for inquiry form.
class TestInquiryForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = InquiryForm(
            {'name': 'test', 'email': 'test@test.com', 'message': 'Hi!'})
        self.assertTrue(form.is_valid(), msg="Inquiry form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = InquiryForm(
            {'name': '', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided in inquiry, but the form is valid"
            )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = InquiryForm(
            {'name': 'Matt', 'email': '', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided in inquiry, but the form is valid"
            )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = InquiryForm(
            {'name': 'Matt', 'email': 'test@test.com', 'message': ''})
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided in inquiry, but the form is valid"
            )
