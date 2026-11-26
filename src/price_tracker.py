import time

def check(scraper,soup):
    old_price=scraper.price(soup)
    timer=int(input('Enter time with seconds: '))
    while  True :
        second = timer 
        time.sleep(second)
        new_price=scraper.price(soup)
        if old_price!=new_price:
            print('price has changed')
            print(f'price is: {new_price}')
            old_price=new_price


        

