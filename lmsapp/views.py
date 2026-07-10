from django.shortcuts import render


def home(request):
    return render(request, 'webpages/index.html')


def courses(request):
    return render(request, 'webpages/courses.html')


def course_detail(request):
    return render(request, 'webpages/course-detail.html')


def contact(request):
    return render(request, 'webpages/contact.html')


def login_page(request):
    return render(request, 'webpages/login.html')


def signup_page(request):
    return render(request, 'webpages/signup.html')


def admin_login_page(request):
    return render(request, 'webpages/admin-login.html')


def student_login_page(request):
    return render(request, 'webpages/student-login.html')


def student_portal_page(request):
    return render(request, 'webpages/student-login.html')


def student_courses_page(request):
    return render(request, 'webpages/student-courses.html')


def student_timetable_page(request):
    return render(request, 'webpages/student-timetable.html')


def student_assignments_page(request):
    return render(request, 'webpages/student-assignments.html')


def student_grades_page(request):
    return render(request, 'webpages/student-grades.html')


def student_discussions_page(request):
    return render(request, 'webpages/student-discussions.html')


def student_settings_page(request):
    return render(request, 'webpages/student-settings.html')


def admin_portal_page(request):
    return render(request, 'webpages/admin-portal.html')
