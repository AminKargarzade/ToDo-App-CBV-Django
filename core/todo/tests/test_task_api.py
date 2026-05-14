from rest_framework.test import APIClient
from django.urls import reverse
import pytest

@pytest.mark.django_db
class TestTaskApi:
    
    def test_get_task_response_200_status(self):
        client = APIClient()
        url = reverse("todo:api-v1:task-list")
        response = client.get(url)
        assert response.status_code == 200 # type: ignore