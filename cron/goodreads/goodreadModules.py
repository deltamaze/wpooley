import sqlite3


class bookModel:
    def __init__(self, bookurl, name, author, ratingText, timestamp, listName):
        self.bookurl = bookurl
        self.name = name
        self.author = author
        self.ratingText = ratingText
        self.timestamp = timestamp
        self.listName = listName


def parseRatings(book):
    return 'TODO'


def insertBookArrayIntoDb(books):
    return 'TODO'


def getTargetLists():
    return ["https://www.goodreads.com/list/show/3077",
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
