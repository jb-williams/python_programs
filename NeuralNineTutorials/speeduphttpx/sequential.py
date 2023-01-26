import time
import requests

def fetch():
    urls = [
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html",
    ]

    results = [requests.get(url) for url in urls]

    print(results)

start = time.perf_counter()
fetch()
end = time.perf_counter()

print(end - start)