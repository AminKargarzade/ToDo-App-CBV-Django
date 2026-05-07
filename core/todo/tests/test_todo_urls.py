from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .. import views

class TestUrl(SimpleTestCase):
    
    def test_todo_task_list_url_resolve(self):
        url = reverse('todo:task_list')
        self.assertEqual(resolve(url).func.view_class, views.TaskList)
        
    def test_todo_task_create_url_resolve(self):
        url = reverse('todo:create_task')
        self.assertEqual(resolve(url).func.view_class, views.TaskCreate)
        
    def test_todo_task_update_url_resolve(self):
        url = reverse('todo:update_task', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, views.TaskUpdate)
        
    def test_todo_task_complete_url_resolve(self):
        url = reverse('todo:complete_task', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, views.TaskComplete)
        
    def test_todo_task_delete_url_resolve(self):
        url = reverse('todo:delete_task', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, views.DeleteView)