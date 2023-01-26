this is more of a framework than a package

will need to 
```bash
pip3 install scrapy
```

then in the dir you want to work

```bash
scrapy startproject neuralcrawling
```

will make dir structure similar to 
```bash
ProjectName/
    spiders/
        __init__.py
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
scrapy.cfg
```

can interact with scrapy in realtime in the terminal
find what you need to get what you want then build it into the prog
```
scrapy shell http://books.toscrape.com/index.html
```

it crawls the page

response object
```
response
```

can filter on things like css
```
response.css("h1")
response.css("h3")
```

to get the actuall html you could
```
response.css("h3").get()
```

could get the text too
```
response.css("h1::text").get()
response.css("a::text").get()
```

prob is it only gets 1 element
```
response.css("a::text").getall()

response.css(".page-header").get()

# give all links, and from the links text
response.xpath("//a/text()").extract()
```

run by
```
scrapy crawl mycrawler
scrapy crawl mycrawler -o output.json
```
