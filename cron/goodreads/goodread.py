import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

maxPageNumber = 100


try:
    # scrape goodreads data into a sqllite database, then dump into google sheet
    # target lists / urls
    listUrls = ["https://www.goodreads.com/list/show/7",
                "https://www.goodreads.com/list/show/6",
                "https://www.goodreads.com/list/show/16",
                "https://www.goodreads.com/list/show/30",
                "https://www.goodreads.com/list/show/53",
                "https://www.goodreads.com/list/show/52",
                "https://www.goodreads.com/list/show/74",
                "https://www.goodreads.com/list/show/73",
                "https://www.goodreads.com/list/show/1384",
                "https://www.goodreads.com/list/show/71",
                "https://www.goodreads.com/list/show/1414",
                "https://www.goodreads.com/list/show/14",
                "https://www.goodreads.com/list/show/8163",
                "https://www.goodreads.com/list/show/4088",
                "https://www.goodreads.com/list/show/71525",
                "https://www.goodreads.com/list/show/3079",
                "https://www.goodreads.com/list/show/3078",
                "https://www.goodreads.com/list/show/3077"]
    # get loop through each url

    for url in listUrls:
        keepGoing = True
        listName = ""
        currentpage = 1
        while keepGoing and currentpage <= maxPageNumber:
            # load url
            pageRequest = requests.get(url+"?page="+str(currentpage))
            pageSoup = BeautifulSoup(pageRequest.content, 'html.parser')
            listName = pageSoup.h1.text
            
            currentpage += 1
        # wait random interval of time, and go to next page
        break  # while debug, just test with one url
except:
  print("An exception occurred")
# loop through each page and scrape book info
# load into table with timestamp
