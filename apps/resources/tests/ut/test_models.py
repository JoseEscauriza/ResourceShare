from django.test import TestCase
from apps.resources import models


class TestTagModel(TestCase):

    def setUp(self):
        self.tag_name = 'Python'
        self.tag = models.Tag(name=self.tag_name)

    def test_tag_object_creation(self):
        self.assertIsInstance(self.tag, models.Tag)

    def test_tag_str_method(self):
        self.assertEquals(self.tag.__str__(), self.tag_name)


class TestCategoryModel(TestCase):

    def setUp(self):
        self.cat_name = 'TestCategory'
        self.category = models.Category(cat=self.cat_name)

    def test_category_object_creation(self):
        self.assertIsInstance(self.category, models.Category)

    def test_category_str_method(self):
        self.assertEqual(self.category.__str__(), self.cat_name)

    def test_category_plural(self):
        self.assertEqual(
            self.category._meta.verbose_name_plural, 'Categories')
