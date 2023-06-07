from django.test import TestCase
from restaurant.models import MenuItem

from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer

from django.contrib.auth.models import User
from rest_framework.test import force_authenticate
from django.urls import reverse

class MenuItemTest(TestCase):
	def test_get_item(self):
		item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
		itemstr = item.get_item()

		self.assertEqual(itemstr, "IceCream : 80")

class MenuItemsViewTest(TestCase):
	def setUp(self):

		self.menu_item1 = MenuItem.objects.create(title="Bizza", price=10.0,inventory=20)
		self.menu_item2 = MenuItem.objects.create(title="Purger", price=8.0,inventory= 30)
		self.menu_item3 = MenuItem.objects.create(title="Xalad", price=6.0,inventory=40)
		self.user = User.objects.create_user(username="testuser", password="testpass")
		self.client = APIClient()

	def test_getall(self):
		user = User.objects.get(username="testuser")
		url = reverse("menuitems-list")
		self.client.force_authenticate(user=user)

		response = self.client.get(url)


		self.assertEqual(response.status_code, 200)

		expected_data = MenuItemSerializer(MenuItem.objects.all(), many=True).data
		self.assertEqual(response.data, expected_data)
	
	

	






	