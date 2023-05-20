from django.test import TestCase
from .models import Catalogue
from django.urls import reverse


class CatalogueViewTests(TestCase):
    def test_book_list_view(self):
        Book_1 = Catalogue.objects.create(
            title="Django for Beginners (2018)",
            ISBN="978-1-60309-0",
            author="John Doe",
            price=9.99,
            availability="true",
        )

        Book_2 = Catalogue.objects.create(
            title="Django for Professionals (2020)",
            ISBN="978-1-60309-3",
            author="Mary Doe",
            price=11.99,
            availability="false",
        )

        response = self.client.get(reverse("home"))

        self.assertIn("Django for Professionals (2020)", response.content.decode())
        self.assertIn("John Doe", response.content.decode())
        self.assertIn("978-1-60309-3", response.content.decode())
