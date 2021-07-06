import requests
import sqlite3
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import date

import goodreadModules as grm

try:
    # target lists / urls
    listUrls = grm.getTargetLists()
    # get loop through each url
    webRequestMadeThisExecution = 0
    maxPageNumber = 100
    maxNumberOfWebRequests = 100
    targetListIndex = 0
    conn = sqlite3.connect('goodreads.db')
    # get last polled list item and page number
    while webRequestMadeThisExecution < maxNumberOfWebRequests:
        targetPage = 1
        targetListIndex += 1
        areThereMorePagesToPullForThisList = True
        listName = ""
        while (areThereMorePagesToPullForThisList):
            # load url

            parsedBooks = []
            pageRequest = (requests.get(listUrls[targetListIndex]
                                        + "?page="+str(targetPage)))
            pageSoup = BeautifulSoup(pageRequest.content, 'html.parser')
            listName = pageSoup.h1.text
            # loop through books on page
            booksOnPage = pageSoup.table.find_all("tr")
            for book in booksOnPage:
                # get id from url,
                bookurl = book.find("a", href=True)["href"]
                name = book.find('a', attrs={'class': 'bookTitle'}).text
                author = book.find('a', attrs={'class': 'authorName'}).text
                ratingText = book.find(
                    'span', attrs={'class': 'minirating'}).text
                thisBook = grm.bookModel(bookurl, name, author, ratingText,
                                         date.today(), listName)
                parsedBooks.append(thisBook)
            print(f"Finished Page {str(targetPage)} for List {listName}")

            targetPage += 1
            webRequestMadeThisExecution += 1
            if (len(booksOnPage) != 100
                    or targetPage <= maxPageNumber
                    or webRequestMadeThisExecution <= maxNumberOfWebRequests):
                areThereMorePagesToPullForThisList = False
            sleep(randint(2, 10))
            # save results to sqllite
            # update sqllite table to indicate list id and page number

        # wait random interval of time, and go to next page
    conn.close()
except Exception as ex:
    print("An exception occurred => " + ex.__str__)
# https://github.com/maddieannette/mycity-restaurants/blob/main/data-retrieve-app/main.py for sqllite
