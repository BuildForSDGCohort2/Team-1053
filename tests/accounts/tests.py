from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.accounts.models import User, Customer
from tests.raw_data import accounts


class AccountTests(APITestCase):
    header_prefix = 'Token '

    def create_user(self):
        new_user = self.client.post(
                reverse('rest_register'), accounts['new_user'], format='json'
            )
        return new_user

    def log_in(self):
        response = self.client.post(
            reverse('rest_login'), accounts['user'], format='json'
        )
        return response

    def test_create_account(self):
        """
            Ensure we can create a new account object.
        """
        response = self.create_user()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')

    def test_get_all_users(self):
        """
            Ensure we can get all users.
        """
        self.create_user()
        url = reverse('user-list')
        response = self.client.get(url, accounts['new_user'], format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_get_user_details(self):
        """
            Ensure we can get user details.
        """
        self.create_user()
        token = self.header_prefix + self.log_in().json()['key']
        self.client.credentials(HTTP_AUTHORIZATION=token)
        response = self.client.get(
            reverse('rest_user_details'), accounts['new_user'],  format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('email', response.json())
        self.assertIn('username', response.json())

    def test_update_user_details(self):
        """
            Ensure we can update user details.
        """
        self.create_user()
        token = self.header_prefix + self.log_in().json()['key']
        self.client.credentials(HTTP_AUTHORIZATION=token)
        response = self.client.put(
            reverse('rest_user_details'), accounts['user'],  format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('email', response.json())
        self.assertIn('username', response.json())

    def test_user_login(self):
        """
            Ensure user can login after creating account.
        """
        self.create_user()
        response = self.log_in()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('key', response.json())

    def test_user_logout(self):
        """
            Ensure user can logout after login.
        """
        self.create_user()
        self.log_in()
        url = reverse('rest_logout')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['detail'], 'Successfully logged out.')

    def test_create_customer_account(self):
        """
            Ensure we can create a new customer account object.
        """
        response = self.create_user()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'test')

    def test_get_customer_accounts(self):
        """
            Ensure we can update customer details.
        """
        self.create_user()
        url = reverse('customer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
