import pytest
from students.models import Course, Student
from rest_framework.test import APIClient
from model_bakery import baker

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_fabric():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_fabric():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_retrieve_courses(client, course_fabric):
    course = course_fabric()

    response = client.get(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 200
    assert response.data['name'] == course.name

@pytest.mark.django_db
def test_list_courses(client, course_fabric):
    courses = course_fabric(_quantity=10)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)

    for i, c in enumerate(data):
        assert c['name'] == courses[i].name

@pytest.mark.django_db
def test_id_filtering(client, course_fabric):
    course1 = course_fabric()
    course2 = course_fabric()
    course3 = course_fabric()

    response = client.get(f'/api/v1/courses/', {'id': course1.id})
    data = response.json()[0]

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert course1.name == data['name']
    assert course2.name or course3.name != data['name']

@pytest.mark.django_db
def test_name_filtering(client, course_fabric):
    course1 = course_fabric(name='orange')
    course2 = course_fabric(name='course2')
    course3 = course_fabric(name='course3')

    response = client.get(f'/api/v1/courses/', {'name': course1.name})
    data = response.json()[0]

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert course1.name == data['name']
    assert course2.name or course3.name != data['name']

@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    data = {
        'id': 1,
        'name': 'Python from scratch'
    }

    response = client.post('/api/v1/courses/', data=data, format='json')

    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client, course_fabric):
    course = course_fabric()
    count = Course.objects.count()
    data = {
        'id': course.id,
        'name': 'Python from scratch'
    }

    response = client.put(f'/api/v1/courses/{course.id}/', data=data, format='json')

    assert response.status_code == 200
    assert Course.objects.count() == count
    assert Course.objects.get(id=course.id).name == data['name']

@pytest.mark.django_db
def test_delete_course(client, course_fabric):
    course = course_fabric()
    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1