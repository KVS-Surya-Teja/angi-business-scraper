import requests
from bs4 import BeautifulSoup
import new_options  # This will handle the URL generation process
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Debugging: Print the value of final_file
print(f"Value of final_file from new_options: {new_options.final_file}")

# Assuming the `final_file` (URL) is generated correctly by the `new_options.py` script
url = str(new_options.final_file)  # This now contains the generated URL

# Debugging: Print the URL before making the request
print(f"Fetching URL: {url}")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Create a session object to handle retries
session = requests.Session()
retry = Retry(
    total=5,  # Number of retries
    backoff_factor=1,  # Exponential backoff factor
    status_forcelist=[500, 502, 503, 504],  # Retry for these status codes
    raise_on_status=False
)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Additional check to ensure url is valid
if url:
    try:
        response = session.get(url, headers=headers, timeout=30)  # Increased timeout to 30 seconds
        response.raise_for_status()  # Check if the request was successful
        # Use lxml parser for BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')

        # Extract the business name
        business_name = soup.select_one('div.BusinessProfileCard_business-name-mobile___hvyR div[data-testid="business-name-mobile"]')
        if business_name:
            print(f"Business Name: {business_name.text.strip()}")

        # Extract the business address
        business_address = soup.select_one('div.BusinessProfileCard_serviceAddress-mobile__txqq6')
        if business_address:
            print(f"Business Address: {business_address.text.strip()}")

        # Extract the rating
        rating = soup.select_one('div.BaseRatingDisplay_root__lhJSZ[aria-label]')
        if rating:
            rating_value = rating['aria-label']
            print(f"Rating: {rating_value}")

        # Extract the number of reviews
        reviews = soup.select_one('span.RatingsLockup_reviewCount__nwosb div')
        if reviews:
            print(f"Number of Reviews: {reviews.text.strip()}")

        # Extract certification status
        certification = soup.select_one('div[data-testid="angi-certified"] span')
        if certification:
            print(f"Certification Status: {certification.text.strip()}")

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
else:
    print("The URL is empty. Please check the value of new_options.final_file.")
