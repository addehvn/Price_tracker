  
def collection(soup):
    collection_name=soup.select_one('#pdp_product_title')
    print(f'Collection: {collection_name.get_text()}')


def product(soup):
    product_name=soup.select_one('#pdp_product_subtitle')
    print(f'Product: {product_name.get_text()}')


def price(soup):
    price=soup.select_one('#price-container > span')
    print(f'Price:{price.get_text()}')

def details(soup):
 collection(soup)
 product(soup)
 price(soup)