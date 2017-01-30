import os
import unittest

from views import app, db
from _config import basedir
from models import User

TEST_DB = 'test.db'

class AllTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
                os.path.join(basedir,TEST_DB))
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def login(self,name,password):
        return self.app.post('/',
                data=dict(name=name, password=password),
                follow_redirects=True)
    def register(self,name,email, password,confirm):
        return self.app.post('register',
                data=dict(name=name,
                    email=email,
                    password=password,
                    confirm=confirm
                    ),
                follow_redirects=True
                )

    def create_user(self,name,email,password):
        new_user = User(name=name, email=email,password=password)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post('add/', data=dict(
            name='Go to the Bank',
            due_date='10/08/2016',
            priority='1',
            posted_date='10/08/2016',
            status='1'
            ),follows_redirects=True)
    def test_user_setup(self):
        new_user = User("test_user8188","test@xyz.com","abcd1234")
        db.session.add(new_user)
        db.session.commit()

    def test_form_is_present(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Please sign in to access your task list', response.data)


    def test_user_can_login(self):
        self.register('Micheal', 'micheal@realpython.com','python','python')
        response = self.login('Micheal','python')
        self.assertIn(b'Welcome', response.data)

    def test_invalid_form_data(self):
        self.register('Micheal', 'micheal@realpython.com','python','python')
        response = self.login('alert("alert box");','foo')
        self.assertIn(b'Invalid username and password', response.data)

    def test_is_present_on_register_page(self):
        response = self.app.get('register/')
        self.assertEqual(response.response_code,200)
        self.assertIn(b'Please register to access this task list', response.data)

    def test_user_registration(self):
        self.app.get('register/', follow_redirects=True)
        response = self.register(
                'Michael', 'michael@realpython.com', 'python', 'python')
        self.assertIn(b'Thanks for registering, please login', response.data)

    def test_user_registration_error(self):
        self.app.get('register/', follows_redirect=True)
        self.register('Micheal', 'micheal@realpython.com','python','python')
        self.app.get('register/', follows_redirect=True)
        response = self.register('Micheal', 'micheal@realpython.com','python','python')
        self.assertIn(b'That username and/or email already exists.',
                response.data
            )

    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo','bar')
        self.assertIn(b'Invalid username and password', response.data)

    def test_logged_in_user_can_access_task_page(self):
        self.register('test', 'test@realpython.com','python','python')
        self.login('test','python')
        response = self.app.get('tasks/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Add new task:', response.data)

    def test_not_logged_in_users_cannot_access_tasks_page(self):
        response = self.app.get('tasks/', follow_redirect = True)
        self.assertIn(b'You need to login first.', response.data)

    def test_users_can_add_tasks(self):
        self.create_user('test1', 'test1@gmail.com','meh')
        self.login('test1','meh')
        self.app.get('tasks/', follow_redirects=True)
        response = self.create_tasks()
        self.assertIn(b'New entry was successfully posted. Thanks.', response.data)

    def test_users_cannot_add_tasks_when_error(self):
        self.create_user('test1', 'test1@gmail.com','meh')
        self.login('test1','meh')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.post('add/', data =dict(
            name = 'Go to the bank',
            due_date = '',
            priority = '1',
            posted_date = '02/05/2014',
            status='1'
            ), follows_redirect=True)
        self.assertEqual(b'This field is required', response.data)

    def test_users_can_delete_tasks(self):
        self.create_user('test1', 'test1@gmail.com','meh')
        self.login('test1','meh')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('delete/1/', follow_redirect=True)
        self.assertIn(b'The task was deleted.',response.data)

    def test_users_cannot_complete_tasks_that_are_not_created_bu_them(self):
        self.create_user('Micheal','m@yahoo.com','python')
        self.login('tasks/',follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_user('anshu','anshu8188@yahoo.com','meh')
        self.login('anshu','meh')
        self.app.get('tasks/',follow_redirects=True)
        response= self.app.get('complete/1/',follow_redirects=True)
        self.assertNotIn(b'The task is complete. Nice', response.data)

if __name__ == "__main__":
    unittest.main()

