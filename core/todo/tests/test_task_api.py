from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime

@pytest.mark.django_db
class TestTaskApi:
    client = APIClient()
    
    def test_get_task_response_200_status(self):
        url = reverse("todo:api-v1:task-list")
        response = self.client.get(url)
        assert response.status_code == 200 # type: ignore
        
    def test_create_task_response_401_status(self):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title" : "test",
            "complete" : True,
            "created_date" : datetime.now()
        }
        response = self.client.post(url, data)
        assert response.status_code == 401  # type: ignore