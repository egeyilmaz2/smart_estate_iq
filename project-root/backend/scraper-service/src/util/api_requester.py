import requests
from bs4 import BeautifulSoup
import logger


def api_request(url, method='GET', headers=None, params=None, data=None):
    """
    Sends a synchronous HTTP request to the specified URL and parses the response using BeautifulSoup.

    Parameters:
        url (str): The URL to request.
        method (str): HTTP method (default 'GET').
        headers (dict): Optional headers.
        params (dict): URL parameters.
        data (dict): Data for POST requests.

    Returns:
        BeautifulSoup: Parsed HTML content if successful, None otherwise.
    """
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data, timeout=10)
        response.raise_for_status()  # Raise for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.RequestException as e:
        logger.scapper_service_logger.error(f"API request error for {url}: {e}")
        return None
    except Exception as e:
        logger.scapper_service_logger.error(f"Unexpected error in API requester for {url}: {e}")
        return None


if __name__ == "__main__":
    test_url = "https://www.example.com"
    result = api_request(test_url)
    if result:
        print("Page title:", result)
    else:
        print("Failed to retrieve data.")
