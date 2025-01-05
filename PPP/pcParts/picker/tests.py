from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Case, CpuCooler, Cpu, InternalHardDrive, Memory, Motherboard, PowerSupply, SavedSelections

class AppTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = Client()
        self.api_client = APIClient()
        self.api_client.force_authenticate(user=self.user)
        
        # Create test data
        self.case = Case.objects.create(name="Test Case")
        self.cpu = Cpu.objects.create(name="Test CPU")
        self.saved_selection = SavedSelections.objects.create(
            user=self.user,
            case_id=self.case.case_id,
            cpu_id=self.cpu.cpu_id,
        )

    # Test login functionality
    def test_login_successful(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  # Redirect on successful login

    # Test signup functionality
    def test_signup_successful(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_passwords_do_not_match(self):
        # Submit form with mismatched passwords
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password321',  # Mismatched passwords
        })

        # Assert that the response is a redirect (302)
        self.assertEqual(response.status_code, 302)

        # Assert that the redirect is back to the signup page
        self.assertRedirects(response, reverse('signup'))

        # Check that the appropriate error message is set
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)  # One message should be added
        self.assertEqual(str(messages[0]), "Passwords do not match.")

    # Test Save Customizations API
    def test_save_customizations_success(self):
        data = {
            "Case": self.case.case_id,
            "CPU": self.cpu.cpu_id,
        }
        response = self.api_client.post(reverse('saveCustomizations'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Customizations saved successfully!", response.data["message"])

    def test_save_customizations_invalid_data(self):
        data = {
            "Case": "invalid_id",
        }
        response = self.api_client.post(reverse('saveCustomizations'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test Retrieve Customizations API
    def test_get_customizations(self):
        response = self.api_client.get(reverse('saveCustomizations'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Test Delete Customizations API
    def test_delete_customization_success(self):
        response = self.api_client.delete(reverse('delete-customization', args=[self.saved_selection.saved_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Customization deleted successfully!")

    def test_delete_customization_not_found(self):
        response = self.api_client.delete(reverse('delete-customization', args=[999]))  # Non-existent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test part detail view
    def test_part_detail_view(self):
        response = self.client.get(reverse('partDet', args=["Case", self.case.case_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.case.name)

    # Test PC Assembly view
    def test_pc_assembly_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('pcAssembly'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Case")