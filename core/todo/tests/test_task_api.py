from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create(email="admin@admin.com", password="a/@1234567")  # type: ignore
    return user


@pytest.mark.django_db
class TestTaskApi:
    client = APIClient()

    def test_get_task_response_200_status(self, api_client):
        url = reverse("todo:api-v1:task-list")
        response = api_client.get(url)
        assert response.status_code == 200  # type: ignore

    def test_create_task_response_401_status(self, api_client):
        url = reverse("todo:api-v1:task-list")
        data = {"title": "test", "complete": True, "created_date": datetime.now()}
        response = api_client.post(url, data)
        assert response.status_code == 401  # type: ignore

    def test_create_task_response_201_status(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        data = {"title": "test", "complete": True, "created_date": datetime.now()}
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201  # type: ignore

    def test_create_task_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("todo:api-v1:task-list")
        data = {}
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400  # type: ignore
