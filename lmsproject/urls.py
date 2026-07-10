"""
URL configuration for lmsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from lmsapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('courses.html', views.courses, name='courses_html'),
    path('course-detail/', views.course_detail, name='course-detail'),
    path('course-detail.html', views.course_detail, name='course_detail_html'),
    path('contact/', views.contact, name='contact'),
    path('contact.html', views.contact, name='contact_html'),
    path('login.html', views.login_page, name='login_html'),
    path('signup.html', views.signup_page, name='signup_html'),
    path('admin-login.html', views.admin_login_page, name='admin_login_html'),
    path('student-login.html', views.student_login_page, name='student_login_html'),
    path('student-portal/', views.student_portal_page, name='student_portal'),
    path('student-portal.html', views.student_portal_page, name='student_portal_html'),
    path('student-courses.html', views.student_courses_page, name='student_courses_html'),
    path('student-timetable.html', views.student_timetable_page, name='student_timetable_html'),
    path('student-assignments.html', views.student_assignments_page, name='student_assignments_html'),
    path('student-grades.html', views.student_grades_page, name='student_grades_html'),
    path('student-discussions.html', views.student_discussions_page, name='student_discussions_html'),
    path('student-settings.html', views.student_settings_page, name='student_settings_html'),
    path('admin-portal.html', views.admin_portal_page, name='admin_portal_html'),
    path('index.html', views.home, name='index_html'),
    path('admin/', admin.site.urls),
]
