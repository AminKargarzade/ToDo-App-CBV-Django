from django.test import TestCase, SimpleTestCase
from datetime import datetime

from ..forms import TaskUpdateForm
from ..models import Task
from django.contrib.auth import get_user_model

class TestTaskForm(TestCase):
    
    def test_task_update_form_with_valid_data(self):
        user_obj = get_user_model()
        form = TaskUpdateForm(data={
            "user": user_obj,
            "title":"test",
            "complete":True,
            "created_date": datetime.now(),
        })
        self.assertTrue(form.is_valid())
        
    def test_task_update_form_with_no_data(self):
        form = TaskUpdateForm(data={})
        self.assertFalse(form.is_valid())