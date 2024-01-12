import requests
from parsel import Selector

def parse_ads(url):
    response = requests.get(url)
    selector = Selector(response.text)

    ads = []

    for ad_elem in selector.css('.listing-item'):
        title = ad_elem.css('.listing-title::text').get()
        price = ad_elem.css('.listing-price::text').get()
        address = ad_elem.css('.listing-address::text').get()
        description = ad_elem.css('.listing-description::text').get()

        ad_data = {
            'title': title.strip() if title else None,
            'price': price.strip() if price else None,
            'address': address.strip() if address else None,
            'description': description.strip() if description else None,
        }

        ads.append(ad_data)

    return ads
