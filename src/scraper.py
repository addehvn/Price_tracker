  
def collection(soup):
    collection_name=soup.select_one('#pdp_product_title')
    return f'Collection: {collection_name.get_text()}'


def product(soup):
    product_name=soup.select_one('#pdp_product_subtitle')
    return f'Product: {product_name.get_text()}'


def price(soup):
    price=soup.select_one('#price-container > span')
    return f'Price:{price.get_text()}'

def details(soup):
 print(collection(soup))
 print(product(soup))
 print(price(soup))