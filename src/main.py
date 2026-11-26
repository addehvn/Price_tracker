import bs4 
import requests
import scraper
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
    print('3. product name')
    print('4. price')
    print('5. Exit')
    choose=int(input('Choose a number from list: '))
    if choose == 1:
        scraper.details(soup)
    if choose == 2: 
        scraper.collection(soup)
    if choose == 3:
        scraper.product(soup)
    if choose == 4:
        scraper.price(soup)
    if choose == 5:
        print('Have a nice day')
        loop = False  
    else :
        choose 
