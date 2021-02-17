# Code must be written in Python 3.

# Consume an API endpoint (located at https://atlas.pretio.in/atlas/coding_quiz) which returns a list of offers. Order the offers by the payout and 
# print them into a csv.

# 10% of the time the endpoint will spit out a 429. Your code should gracefully handle this error, sleep for 60 seconds and then retry the request. 
# 10% of the time the endpoint will spit out a 500. Your code should handle the error, print it and exit.

# Authorization to the endpoint is done via Bearer token: LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF
# The endpoint will return a 401 if it's unauthorized. 

# Please include two unit tests: one to simulate the case where the endpoint returns a 429 and one to simulate the case where the endpoint returns a 500.

# Please submit the offers.csv via email and upload your code to a public repository (bitbucket, github, gitlab, etc...) and provide the url.

import requests
from requests.exceptions import HTTPError
import json
import time
import csv

CONST_URL = 'https://atlas.pretio.in/atlas/coding_quiz'
CONST_HEAD = {"Authorization": "Bearer LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF"}

def main():
    '''
    Requests Response from URL
    '''
    try:
        response = requests.get(CONST_URL,headers=CONST_HEAD)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()

    except HTTPError as http_err:
        if response.status_code == 429:
            time.sleep(60)
            main()
            
        elif response.status_code == 500:
            print('HTTP {} error occurred:{}'.format(response.status_code,{http_err}))
            raise SystemExit

    except Exception as err:
        print('HTTP error occurred:{}'.format({err}))
    
    else:
        offers = response.json()['rows']
        sorted_offers = sorted(offers, key= lambda x: (float(x['payout']),x['name']))

        with open("output.csv",'w', newline = '') as file:
            writer = csv.DictWriter(file, fieldnames = sorted_offers[0].keys())
            writer.writeheader()
            
            # Loop through each offer and write to csv file
            for i in range(len(sorted_offers)):
                writer.writerow(sorted_offers[i])
            file.close()

if __name__ == "__main__":
    main()