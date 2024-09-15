# Angi Business Scraper

This project is a web scraper designed to extract business information from the **Angi (formerly Angie’s List)** website. The scraper retrieves details such as business name, address, contact information, reviews, and more.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech_stack)
- [Message](#message)
  
## Features
- Scrapes detailed business information, including:
  - Business Name
  - Address
  - Rating
  - No. of Reviews
  - Angi Certification
  - Experience
  - Description
  - Reviews
  - Customer Recommendation
- Handles pagination to scrape multiple results.
- The `Category: ` pane contains a search bar with a dynamic dropdown, the `State: ` pane also contains a search bar with a dynamic dropdown, and the `City: ` pane contains a search bar to take the input.
- Contains a loader, to inform the user about the status of the scraping.
- Saves scraped data into CSV format.

## Tech Stack
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![webbrowser](https://img.shields.io/badge/webbrowser-library-blue)
- ![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-darkgreen?style=for-the-badge)
- ![urllib3](https://img.shields.io/badge/urllib3-library-green)
- ![Requests](https://img.shields.io/badge/Requests-005A9C?style=for-the-badge&logo=python&logoColor=white)
- ![Flask](https://img.shields.io/badge/Flask-framework-red)
  
Make sure you have Python 3.8+ installed on your system.

## Message
When the `ui.py` is run, the user's input is taken from the HTML UI deployed by Flask, which retrieves it and stores it as variables. You can see it in `app.py` (Currently Incomplete). These inputs are used to create the most suitable URL from the Angi's site which matches with the user's input. You can see it in `new_options.py` (Done as a python demo, couldn't integrate it with Flask yet). The `options.py` contains the lists of all categories, states and cities within those states (Completed). 

I tried my best to deploy the `app.py` and scrape using bs4 and requests in `main.py` but currently I faced some issues like warning that it is a development server and runtime error respectively.

This project is done with the best of my efforts and my novice programming experience sir. 

Thank you for giving me my first webscraping project sir,
KVS Surya Teja
