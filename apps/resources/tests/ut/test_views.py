from django.test import TestCase, Client
from django.urls import reverse
from apps.resources import views
from apps.user.models import User
from apps.resources import models


class TestResourcesView(TestCase, Client):

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='erjose22',
            password='kektus',
            first_name='jose',
            last_name='esca',
            email='email@kektus.com',
            bio='whatreyoutalkinabeet',
            title='sassy seesquatch'
        )

        self.tag = models.Tag(name='Python')
        self.tag.save()

        self.cat = models.Category.objects.create(
            cat='Programming Language'
        )

        expected_res_count = 1

        self.resource = models.Resources.objects.create(
            user_id=self.user,
            cat_id=self.cat,
            title='Python for begs',
            description='yea',
            link="https://link.com",
        )

        self.resource.tags.add(self.tag)
        self.resource.save()

    def test_home_page_return_200_status(self):
        response = self.client.get(
            reverse('home-page'),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        self.assertEqual(response.status_code, 200)

    def test_home_page_user_count(self):

        response = self.client.get(
            reverse('home-page'),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        self.assertEqual(response.context['user_cnt'], 1)

    def test_home_page_view_resource_count(self):

        response = self.client.get(
            reverse('home-page'),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        self.assertEqual(response.context['cnt'], 1)

    def test_resource_detail_redirects_to_login_for_non_auth_user(self):
        response = self.client.get(
            reverse('resource-detail', kwargs={'id': 1}),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        self.assertEqual(response.status_code, 302)

    def test_resource_detail_view_status_code_ok_for_auth_user(self):

        login = self.client.login(username='erjose22', password='kektus')

        response = self.client.get(
            reverse('resource-detail', kwargs={'id': self.resource.id}),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        self.assertEqual(response.status_code, 200)
