import requests
from bs4 import BeautifulSoup

class FinTablesScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_fund_data(self, fund_id):
        url = f"{self.base_url}/fund/{fund_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example scraping logic: Modify this according to the website structure
        fund_data = {}
        fund_data['name'] = soup.find('h1', class_='fund-name').text.strip()
        fund_data['performance'] = soup.find('div', class_='fund-performance').text.strip()
        return fund_data

if __name__ == "__main__":
    base_url = 'https://www.fintables.com'
    scraper = FinTablesScraper(base_url)
    fund_info = scraper.fetch_fund_data('12345')  # Sample fund ID
    print(fund_info)