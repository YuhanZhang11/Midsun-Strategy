import requests
import sys
import os.path

sys.path.append(os.path.dirname(__file__))

from config import BASE_URL 

# common getter for all files
def get_API_data(query: str):
    """
    @param query: formatted query to be requested from API
    #return: a JSON response from API
    """
    url = BASE_URL + query
     # get and return response
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print("An error occured:", err, "\nMessage:", err.response.text)
        sys.exit()
    return response.json()

# TODO: build a common SQLite connection/insert function