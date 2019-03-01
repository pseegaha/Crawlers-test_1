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

## Storing Data
Scrapy provides a convenient way to store the yielded item into a separate file using -o option by:

```scrapy crawl GithubTrendingRepoCrawler -o extracted_data_files/links_JSON.json```

extracted_data_files is a folder and .json is the file format. Scrapy also supports .csv and .xml formats as well.

## Running the Test
I write a script link_generator.py to generate all the URL links of Reuters news of 22 companies from January 1, 2011 to December 31, 2017. Each company would have 365 days x 6 years = 2190 links, and I end up with 2190 x 22 = 48180 links stored in url_list.txt
Then, I construct my Spider in samsung_Spider.py.
After specifying the crawling rule, I let the Spider crawl the website

```scrapy crawl samsung_Spider```
If I want to write the scraped content to csv file and don't display the content in the terminal, I use the command

```scrapy crawl --nolog --output=export.csv samsung_Spider```
The source code doesn't contain the date in a clear structure, so I obtained the date from the URL links and then, I write a script convert_file.py to extract the date from the URL and re-format them to MM/DD/YY
The sample scraped data is stored in News folder.
