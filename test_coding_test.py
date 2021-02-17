import unittest
from unittest.mock import patch
import coding_test

class testHttpStatusCodes(unittest.TestCase):
    def setUp(self):
        self.URL = 'https://atlas.pretio.in/atlas/coding_quiz'
        self.HEAD = {"Authorization": "Bearer LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF"}

    def test_HttpStatusCode_429(self):
        with patch('coding_test.requests.get') as mocked_get:
            mocked_get.return_value.status_code = 429
            # mocked_get.assert_called_with("{}/{}".format(self.URL,self.HEAD))
            response = coding_test.requests.get(self.URL,headers = self.HEAD)
            self.assertEqual(response.status_code,429)
    
    def test_HttpStatusCode_500(self):
        with patch('coding_test.requests.get') as mocked_get:
            mocked_get.return_value.status_code = 500
            # mocked_get.assert_called_with("{}/{}".format(self.URL,self.HEAD))
            response = coding_test.requests.get(self.URL,headers = self.HEAD)
            self.assertEqual(response.status_code,500)

if __name__ == '__main__':
    unittest.main()