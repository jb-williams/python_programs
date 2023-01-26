import time
import asyncio
import httpx

async def fetch():
    urls = [
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html",
    ]

    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)

    print(results)

start = time.perf_counter()
asyncio.runt(fetch())
end = time.perf_counter()

print(end - start)