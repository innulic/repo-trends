import unittest
import sys # added!
sys.path.append("..") # added!
import app as tested_app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_repos_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.status_code, 200)

    def test_post_repos_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)


if __name__ == '__main__':
    unittest.main()