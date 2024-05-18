import time
from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_create_task(self):
        
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            is_completed=False
        )

        
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.title, 'Test Task')
        self.assertFalse(task.is_completed)
        self.assertIsNotNone(task.time_create)

    def test_task_str(self):
        
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            is_completed=False
        )

        
        self.assertEqual(str(task), f'User: {self.user} | Task: {task.title}')

    def test_task_ordering(self):
        
        task1 = Task.objects.create(
            user=self.user,
            title='Test Task 1',
            is_completed=False
        )
        time.sleep(0.01)  # Затримка, щоб завдання створювалися в разний час
        task2 = Task.objects.create(
            user=self.user,
            title='Test Task 2',
            is_completed=False
        )

        
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)
        self.assertEqual(tasks[1], task1)

    def test_task_index(self):
        
        index_fields = [index.fields for index in Task._meta.indexes]
        self.assertIn(['-time_create'], index_fields)
