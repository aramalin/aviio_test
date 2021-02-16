import unittest
import requests
from requests.exceptions import HTTPError

URL = 'https://atlas.pretio.in/atlas/coding_quiz'
HEAD = {"Authorization": "Bearer LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF"}

class testHttpStatusCodes(unittest.TestCase):

    def testHttpStatusCodes429(self):
        # Ensures Raises HTTPError 429 Status Code
        self.assertRaises((requests.get(URL,headers=HEAD)).status_code,429)
    
    def testHttpStatusCodes500(self):
        # Ensures Raises HTTPError 500 Status Code
        self.assertRaises((requests.get(URL,headers=HEAD)).status_code,500)