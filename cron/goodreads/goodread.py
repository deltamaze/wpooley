import requests
import sqlite3
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import date

maxPageNumber = 100


class bookModel:
    def __init__(self, bookurl, name, author, ratingText, timestamp, listName):
        self.bookurl = bookurl
        self.name = name
        self.author = author
        self.ratingText = ratingText
        self.timestamp = timestamp
        self.listName = listName


try:
    # target lists / urls
    listUrls = ["https://www.goodreads.com/list/show/3077",
                "https://www.goodreads.com/list/show/7",
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
    webRequestMadeThisExecution = 0
    targetListIndex = 0
    targetPage = 1
    conn = sqlite3.connect('sqlite.db')
    # get last polled list item and page number
    while webRequestMadeThisExecution < 100:
        targetListIndex += 1
        areThereMorePagesToPullForThisList = True
        listName = ""
        while (areThereMorePagesToPullForThisList
                and targetPage <= maxPageNumber
                and webRequestMadeThisExecution <= 100):
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
                thisBook = bookModel(bookurl, name, author, ratingText,
                                     date.today(), listName)
                parsedBooks.append(thisBook)
            print(f"Finished Page {str(targetPage)} for List {listName}")

            if len(booksOnPage) != 100:
                areThereMorePagesToPullForThisList = False
            sleep(randint(2, 10))
            targetPage += 1
            # save results to sqllite
            # update sqllite table to indicate list id and page number

        # wait random interval of time, and go to next page
    conn.close()
except Exception as ex:
    print("An exception occurred => " + ex.__str__)
# https://github.com/maddieannette/mycity-restaurants/blob/main/data-retrieve-app/main.py for sqllite
