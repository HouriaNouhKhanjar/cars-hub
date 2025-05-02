from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.contrib.auth.models import User
from .models import Car, Category, UserProfile, Comment


def get_test_image():
    """Create default image"""
    image = BytesIO()
    Image.new('RGB', (100, 100)).save(image, 'JPEG')
    image.seek(0)
    return SimpleUploadedFile('test.jpg',
                              image.read(),
                              content_type='image/jpeg')


class BaseTestCase(TestCase):
    """Base class contains the basic data to test car view"""
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.category = Category.objects.create(name='Sedan')
        self.car = Car.objects.create(
            title='Test Car',
            model='Model S',
            brand='Tesla',
            age=1,
            description='Electric car',
            category=self.category,
            owner=self.user,
            approved=1,
        )
        self.profile = UserProfile.objects.create(user=self.user,
                                                  phone='123456')
        self.second_user = User.objects.create_user(
            username="secondUser",
            password="secondPassword",
            email="test2@test.com"
        )


class CommentAndLikeTests(BaseTestCase):
    """extend data from basetest to add comment"""
    def setUp(self):
        super().setUp()
        self.client.login(username='myUsername', password='myPassword')
        self.comment = Comment.objects.create(
            user=self.user,
            car=self.car,
            content="Initial comment"
        )


class CarListViewTests(BaseTestCase):
    """Test cars list homepage"""
    def test_car_list_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/index.html')
        self.assertContains(response, self.car.title)


class UserCarListViewTests(BaseTestCase):
    """Test user cars list"""
    def test_car_list_view_status_code(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/cars-list.html')
        self.assertContains(response, self.car.title)


class CarDetailViewTests(BaseTestCase):
    """Test detail car view"""
    def test_car_detail_view(self):
        response = self.client.get(reverse('car_detail', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.title)


class CarCreateViewTests(BaseTestCase):
    def test_create_car_view_redirect_if_not_logged_in(self):
        """Test car add view not authorized"""
        response = self.client.get(reverse('car_add'))
        self.assertEqual(response.status_code, 302)

    def test_create_car_success(self):
        """Test car add view authorized"""
        self.client.login(username="myUsername", password="myPassword")
        url = reverse('car_add')
        image = get_test_image()
        data = {
            'title': 'New Car',
            'model': 'Y',
            'brand': 'Tesla',
            'age': 2,
            'description': 'A fast car',
            'category': self.category.id
        }
        response = self.client.post(url, data=data, files={'images': image})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Car.objects.filter(title='New Car').exists())


class CarUpdateViewTests(BaseTestCase):
    def test_update_car_redirect_if_not_owner(self):
        """Test car add view not authorized"""
        self.client.login(username='secondUser', password='secondPassword')
        url = reverse('car_edit', args=[self.car.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_update_car_success(self):
        """Test car add view authorized"""
        self.client.login(username="myUsername", password="myPassword")
        url = reverse('car_edit', args=[self.car.id])
        response = self.client.post(url, {
            'title': 'Updated Title',
            'model': self.car.model,
            'brand': self.car.brand,
            'age': self.car.age,
            'description': 'Updated desc',
            'category': self.category.id,
        })
        self.assertEqual(response.status_code, 302)
        self.car.refresh_from_db()
        self.assertEqual(self.car.title, 'Updated Title')


class DeleteCarViewTests(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username="myUsername", password="myPassword")
        self.delete_url = reverse('car_delete', args=[self.car.id])

    def test_delete_car_success(self):
        """Test successful deletion by owner"""
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())

    def test_delete_car_forbidden_for_non_owner(self):
        """Test forbidden access by non-owner"""
        self.client.login(username="secondUser", password="secondPassword")
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 403)
        self.assertIn('Forbidden', response.json()['error'])

    def test_delete_car_method_not_allowed(self):
        """Test not allowed"""
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 405)
        self.assertIn('Method not allowed', response.json()['error'])


class ToggleLikeTests(CommentAndLikeTests):
    def test_like_car(self):
        """Test like a car"""
        url = reverse('toggle_like', args=[self.car.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.car.likes.filter(id=self.user.id).exists())
        self.assertTrue(response.json()['liked'])

    def test_unlike_car(self):
        """Test dislike a car"""
        self.car.likes.add(self.user)
        url = reverse('toggle_like', args=[self.car.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.car.likes.filter(id=self.user.id).exists())
        self.assertFalse(response.json()['liked'])

    def test_toggle_like_method_not_allowed(self):
        url = reverse('toggle_like', args=[self.car.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)


class ProfileViewTests(BaseTestCase):
    def test_profile_view_redirect_if_not_logged_in(self):
        """Test profile view not loggedin"""
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_profile_view_logged_in(self):
        """Test profile view loggedin"""
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/index.html')


class CommentTests(CommentAndLikeTests):
    def test_add_comment(self):
        """Test add comment loggedin"""
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(reverse('add_comment'), {
            'car_id': self.car.id,
            'content': 'Nice car!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Nice car!', response.json().get('content'))

    def test_add_comment_not_loggedin(self):
        """Test add comment not loggedin"""
        self.client.logout()
        response = self.client.post(reverse('add_comment'), {
            'car_id': self.car.id,
            'content': 'Nice car!'
        })
        self.assertEqual(response.status_code, 302)

    def test_add_comment_not_empty_content(self):
        """Test add comment empty content"""
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(reverse('add_comment'), {
            'car_id': self.car.id,
            'content': ''
        })
        self.assertEqual(response.status_code, 400)

    def test_edit_comment_success(self):
        """Test edit comment from authorized user"""
        url = reverse('edit_comment', args=[self.comment.id])
        response = self.client.post(url, {
                                     'car_id': self.car.id,
                                     'content': 'test'
                                    })
        self.assertEqual(response.status_code, 200)

    def test_edit_comment_forbidden(self):
        """Test edit comment from not authorized user"""
        self.client.login(username='secondUser', password='secondPassword')
        url = reverse('edit_comment', args=[self.comment.id])
        response = self.client.post(url, {
                                     'car_id': self.car.id,
                                     'content': 'test'
                                    })
        self.assertEqual(response.status_code, 404)

    def test_edit_comment_method_not_allowed(self):
        """Test edit comment from not allowed"""
        url = reverse('edit_comment', args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_delete_comment_success(self):
        """Test delete comment from authorized user"""
        url = reverse('delete_comment', args=[self.comment.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

    def test_delete_comment_forbidden(self):
        """Test delete comment from not authorized user"""
        self.client.login(username='secondUser', password='secondPassword')
        url = reverse('delete_comment', args=[self.comment.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

    def test_delete_comment_method_not_allowed(self):
        """Test delete comment from not allowed"""
        url = reverse('delete_comment', args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)
