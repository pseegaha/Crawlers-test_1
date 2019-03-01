# Crawlers-test_1
# Overview
Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

For more information including a list of features check the Scrapy homepage at: https://scrapy.org

## Installation
### Create a virtual environment
```pip install virtualenv```
```mkvirtualenv project```

### Install Scrapy and dependencies
```pip install scrapy service_identity ipython pillow```

Can check whether we have successfully installed Scrapy by typing command

```pip freeze```

## Development Setup
### Create the first Spider
To create a Spider project, simply type

```scrapy startproject project```
This will create a project directory samsung and all the neccessary files for the crawler. Now I access the project directory

```cd project```
Display all available Scrapy command by

```scrapy -h```
Create the first Spider named samsung_Spider followed with the link of the news website that I want to scrape data from.

```scrapy genspider project_Spider www.reuter.com```

## Storing Data
Scrapy provides a convenient way to store the yielded item into a separate file using -o option by:

```scrapy crawl project -o extracted_data_files/links_JSON.json```

extracted_data_files is a folder and .json is the file format. Scrapy also supports .csv and .xml formats as well.

