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
   
## Scrapy Project Setup
Execute the below command to create a Scrapy project:

```scrapy startproject github_trending_bot```

Startproject command will create a directory in the current directory. Use the cd command to change directory and pwd or  cd(alone) to check the name of the current directory.

## Spider arguments
Spiders can receive arguments that modify their behaviour. Some common uses for spider arguments are to define the start URLs or to restrict the crawl to certain sections of the site, but they can be used to configure any functionality of the spider.

Spider arguments are passed through the :command:`crawl` command using the -a option. For example:

```scrapy crawl myspider -a category=electronics```

## Storing Data
Scrapy provides a convenient way to store the yielded item into a separate file using -o option by:

```scrapy crawl GithubTrendingRepoCrawler -o extracted_data_files/links_JSON.json```

extracted_data_files is a folder and .json is the file format. Scrapy also supports .csv and .xml formats as well.

## Installation
### Create a virtual environment
```pip install virtualenv```
```mkvirtualenv samsung```
### Install Scrapy and dependencies
```pip install scrapy service_identity ipython pillow```
Can check whether we have successfully installed Scrapy by typing command

```pip freeze```

## Development Setup
### Create the first Spider
To create a Spider project, simply type

```scrapy startproject samsung```
This will create a project directory samsung and all the neccessary files for the crawler. Now I access the project directory

```cd samsung```
Display all available Scrapy command by

```scrapy -h```
Create the first Spider named samsung_Spider followed with the link of the news website that I want to scrape data from.

```scrapy genspider samsung_Spider www.reuter.com```

## Running the Test
I write a script link_generator.py to generate all the URL links of Reuters news of 22 companies from January 1, 2011 to December 31, 2017. Each company would have 365 days x 6 years = 2190 links, and I end up with 2190 x 22 = 48180 links stored in url_list.txt
Then, I construct my Spider in samsung_Spider.py.
After specifying the crawling rule, I let the Spider crawl the website

```scrapy crawl samsung_Spider```
If I want to write the scraped content to csv file and don't display the content in the terminal, I use the command

```scrapy crawl --nolog --output=export.csv samsung_Spider```
The source code doesn't contain the date in a clear structure, so I obtained the date from the URL links and then, I write a script convert_file.py to extract the date from the URL and re-format them to MM/DD/YY
The sample scraped data is stored in News folder.
