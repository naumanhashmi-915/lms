from django.test import TestCase
from django.urls import reverse


class HomepageTests(TestCase):
    def test_homepage_renders(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student LMS')

    def test_courses_page_renders(self):
        response = self.client.get(reverse('courses'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Courses')

    def test_contact_page_renders(self):
        response = self.client.get(reverse('contact'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact Us')

    def test_html_page_request_renders(self):
        response = self.client.get('/courses.html')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Courses')

    def test_student_portal_page_renders(self):
        response = self.client.get('/student-portal.html')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Portal')
