from bs4 import BeautifulSoup
import requests, openpyxl 


excel = openpyxl.Workbook() #parsing into csv excel file
print(excel.sheetnames)
sheet = excel.active            #load data into active sheet
sheet.title = 'Best Animes rated by IMDB'
print(excel.sheetnames)
sheet.append(['Anime Rank', 'Anime Name', 'Release Year', 'Rating (IMDB)']) #EXCEL COLOUMS


try:                                                                          
    source = requests.get('https://www.imdb.com/list/ls033398199/')             #access the link 
    source.raise_for_status()                                                 #throws error if there is a problem with a link.# if we dont use this, invalid url would still run in the terminal

    soup = BeautifulSoup(source.text, 'html.parser')                                         #returns the html content of the webpage
    
    
    animes = soup.find('div', class_="lister-list").find_all('div', class_="lister-item mode-detail")                 #tbody is extracted and finding all tr
    # print(len(animes)) #60

    for anime in animes:                         #iterate throught the one by one in the 50 list
        
        name =  anime.find('h3', class_="lister-item-header").a.text                     #only in the tag a to find the title name and text
        # print(name)  #Bleach: Sennen Kessen-hen



        rank = anime.find('span', class_="lister-item-index unbold text-primary").get_text(strip=True).split('.')[0] #strips all new characters or spaces
        # print(rank) 

        year = anime.find('span', class_="lister-item-year text-muted unbold").text.strip('()')
        # print(year)
        

        rating = anime.find('span', class_="ipl-rating-star__rating").text
        # print(rating)
        
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating]) #load value into escel
        
except Exception as e:
    print(e)

excel.save('IMDB Anime Ratings SHEET.xlsx') #saving the file