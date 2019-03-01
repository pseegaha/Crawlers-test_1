# Crawlers-test_1
# Overview
Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

For more information including a list of features check the Scrapy homepage at: https://scrapy.org

## Requirements
Python 2.7 or Python 3.4+
Works on Linux, Windows, Mac OSX, BSD

## Install
The quick way:

```pip install scrapy```
For more details see the install section in the documentation: https://docs.scrapy.org/en/latest/intro/install.html

Basic executable crawl spidy code for a specified site....if you are using it for different weblinks, have to change the xpath and link
....
Effective can pull all the comments from a single page

## Spiders
Spiders are classes which define how a certain site (or a group of sites) will be scraped, including how to perform the crawl (i.e. follow links) and how to extract structured data from their pages (i.e. scraping items). In other words, Spiders are the place where you define the custom behaviour for crawling and parsing pages for a particular site (or, in some cases, a group of sites).

For spiders, the scraping cycle goes through something like this:

1) You start by generating the initial Requests to crawl the first URLs, and specify a callback function to be called with the response downloaded from those requests.

 The first requests to perform are obtained by calling the :meth:`~scrapy.spiders.Spider.start_requests` method which (by default) generates :class:`~scrapy.http.Request` for the URLs specified in the :attr:`~scrapy.spiders.Spider.start_urls` and the :attr:`~scrapy.spiders.Spider.parse` method as callback function for the Requests.

2) In the callback function, you parse the response (web page) and return either dicts with extracted data, :class:`~scrapy.item.Item` objects, :class:`~scrapy.http.Request` objects, or an iterable of these objects. Those Requests will also contain a callback (maybe the same) and will then be downloaded by Scrapy and then their response handled by the specified callback.

3) In callback functions, you parse the page contents, typically using :ref:`topics-selectors` (but you can also use BeautifulSoup, lxml or whatever mechanism you prefer) and generate items with the parsed data.

4) Finally, the items returned from the spider will be typically persisted to a database (in some :ref:`Item Pipeline <topics-item-pipeline>`) or written to a file using :ref:`topics-feed-exports`.

Even though this cycle applies (more or less) to any kind of spider, there are different kinds of default spiders bundled into Scrapy for different purposes. We will talk about those types here.

.. module:: scrapy.spiders
   :synopsis: Spiders base class, spider manager and spider middleware

## Spider arguments
Spiders can receive arguments that modify their behaviour. Some common uses for spider arguments are to define the start URLs or to restrict the crawl to certain sections of the site, but they can be used to configure any functionality of the spider.

Spider arguments are passed through the :command:`crawl` command using the -a option. For example:

```scrapy crawl myspider -a category=electronics```

## Storing Data
Scrapy provides a convenient way to store the yielded item into a separate file using -o option by:

```scrapy crawl GithubTrendingRepoCrawler -o extracted_data_files/links_JSON.json```

extracted_data_files is a folder and .json is the file format. Scrapy also supports .csv and .xml formats as well.
