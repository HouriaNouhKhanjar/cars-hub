from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image
from .forms import UserForm, ProfileForm, CarForm
from .models import Category


# Create tests for user form.
class UserFormTest(TestCase):
    def test_valid_user_form(self):
        """Test for all fields are correct"""
        form = UserForm(data={'username': 'testuser',
                              'email': 'user@example.com'})
        self.assertTrue(form.is_valid(),
                        msg="User Form isn't valid.")

    def test_invalid_user_form(self):
        """Test for all fields are incorrect"""
        form = UserForm(data={'username': '', 'email': 'not-an-email'})
        self.assertFalse(form.is_valid(),
                         msg="Profile form fields are incorrect.")


# Create tests for user profile form.
class ProfileFormTest(TestCase):

    def setUp(self):
        """Create default user"""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        image = BytesIO()
        Image.new('RGB', (100, 100)).save(image, 'JPEG')
        image.seek(0)
        self.image = SimpleUploadedFile('test.jpg',
                                        image.read(),
                                        content_type='image/jpeg')

    def test_valid_profile_form(self):
        """Test for all fields are correct"""
        form = ProfileForm(data={
                           'phone': '1234567890',
                           'user': self.user
                           },
                           files={'profile_image': self.image})
        self.assertTrue(form.is_valid(),
                        msg="Profile form isn't valid.")

    def test_invalid_profile_form(self):
        """Test phone field is optional"""
        form = ProfileForm(data={'phone': ''})
        self.assertTrue(form.is_valid(),
                        msg="Profile phone fields is required.")


# test create new car
class CarFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.category = Category.objects.create(name='SUV')
        image = BytesIO()
        Image.new('RGB', (100, 100)).save(image, 'JPEG')
        image.seek(0)
        self.image = SimpleUploadedFile('test.jpg',
                                        image.read(),
                                        content_type='image/jpeg')

    def test_valid_car_form(self):
        """Test for all fields are filled"""
        form_data = {
            'title': 'Test Car',
            'model': 'Model X',
            'brand': 'Tesla',
            'age': 2,
            'description': 'Great electric car',
            'category': self.category.id,
        }
        form = CarForm(data=form_data, files={'images': self.image})
        self.assertTrue(form.is_valid())

    def test_invalid_car_form_missing_fields(self):
        """Test for all fields are not correct"""
        form_data = {
            'title': '',
            'model': '',
            'brand': '',
            'age': '',
            'description': '',
            'category': ''
        }
        form = CarForm(data=form_data)
        self.assertFalse(form.is_valid())
