# Angi Business Scraper

This project is a web scraper designed to extract business information from the **Angi (formerly Angie’s List)** website. The scraper retrieves details such as business name, address, contact information, reviews, and more.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)

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
- Saves scraped data into CSV format.

## Requirements
The scraper uses the following Python libraries:
- `requests`
- `bs4`
- `lxml`
- `pandas` (optional, for saving to CSV)
- `selenium` (optional, for dynamic pages)

Make sure you have Python 3.8+ installed on your system.
