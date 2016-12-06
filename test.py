from app import app
import unittest 

class FlaskTestCase(unittest.TestCase):

    # Checking that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # Checking that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        self.assertIn(b'Please login', response.data)
    
    # Checking that login behaves correctly with correct credentials
    def test_correct_login(self):
        tester = app.test_client()
        response = test.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'You were logged in', response.data)

    # Checking login behaves correctly when fed incorrect credentials 
    def test_incorrect_login(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="wrong", password="bruh"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid login. Please try again.', response.data)
    
    # Testing the logout func
    def test_logout(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True 
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b"You logged out.", response.data)

    # Checking that the main page requires user login 
    def test_main_route_requires_login(self):
        tester = app.test_client()
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'You need to loggin first', response.data)

    # Ensure that logout page requires user to be already logged in 
    def test_logout_route_requires_login(self):
        tester = app.test_client()
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to loggin first', response.data)

    # Ensure that posts appear on the main page 
    def test_posts_show_up_on_main_page(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'Hello from the shell', response.data)


if __name__ == '__main__':
    unittest.main()