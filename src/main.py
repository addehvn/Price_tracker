import bs4 
import requests
import scraper
import price_tracker
link = input("Enter nike product's link: ")

r=requests.get(link)
data=r.text
soup=bs4.BeautifulSoup(data)


# Main menu
loop =True
while loop == True:
    print('----- Main menu -----')
    print()
    print('1. Full detail')
    print('2. Collection name')
    print('3. Product name')
    print('4. Price')
    print('5. Turn on checker')
    print('6. Exit')
    choose=int(input('Choose a number from list: '))
    if choose == 1:
        print(scraper.details(soup))
    if choose == 2: 
        print(scraper.collection(soup))
    if choose == 3:
        print(scraper.product(soup))
    if choose == 4:
        print(scraper.price(soup))
    if choose == 5:
        price_tracker.check(scraper,soup)
    if choose == 6:
        print('Have a nice day')
        loop = False  
    else :
        choose 
    