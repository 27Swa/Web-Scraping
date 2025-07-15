# Web-Scraping
## 📚 Book Store Web Scraper

This project is a **Python-based web scraper** built using Selenium that extracts detailed information about books from [books.toscrape.com](http://books.toscrape.com). It automatically navigates through the site to gather:

- ✅ Book Title  
- 💰 Price  
- 📦 Availability (number of copies in stock)  
- 🏷️ Category

---

### 🚀 Technologies Used

- Python 3.x
- Selenium WebDriver
- ChromeDriver
- Standard libraries: `time`, `pandas`

---

### 🔍 What the Script Does

- Accesses the main page of the bookstore.
- Iterates over all book categories.
- For each category:
  - Navigates to the category page.
  - Traverses all pages within the category if multiple pages exist.
  - Extracts details for each book:
    - Title
    - Price
    - Availability
    - Category
- Saves the collected data into a CSV file for further analysis.

---
