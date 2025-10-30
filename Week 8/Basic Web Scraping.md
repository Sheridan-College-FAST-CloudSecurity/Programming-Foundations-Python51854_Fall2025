Basic Web Scraping Techniques

Web scraping is the process of extracting data from websites. It allows you to collect information that is displayed on web pages but not available as structured data (like JSON or CSV).

1. Why Web Scraping?

Data Collection: Gather information for analysis, research, or personal projects.

Automation: Automatically fetch and process data without manual copy-paste.

APIs Not Available: When a website does not provide an API, scraping is a useful alternative.

Examples of use cases:

Collecting product prices from e-commerce websites.

Extracting news headlines from online newspapers.

Scraping real estate listings for analysis.

2. Basic Tools in Python

The most common Python libraries for web scraping are:

requests – To send HTTP requests and fetch webpage content.
requests.get(url) → sends a GET request to fetch HTML.

BeautifulSoup(html_content, "html.parser") → parses HTML so it can be queried.

Selecting Elements

You can use:

Tag names: soup.find_all("p") → all paragraphs.
What is a User-Agent?

A User-Agent is a string that a browser or client sends to a web server to identify itself. It tells the server:

Which browser or client is making the request (Chrome, Firefox, Safari, etc.)

Which operating system is being used (Windows, macOS, Linux, Android, etc.)

Version information of the browser or client

It’s part of the HTTP request headers when you visit a website.
Why User-Agent Matters in Web Scraping

Some websites block requests from unknown clients (like scripts or bots) to prevent automated scraping.

Adding a User-Agent makes your request look like it’s coming from a real browser, increasing the chance the server will respond normally.

Without it, some websites might:

Return an error page

Return empty content

Redirect you to a login or CAPTCHA page

Example of a User-Agent String

Here’s an example for Chrome on Windows:

Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/114.0.0.0 Safari/537.36


Mozilla/5.0 → Historical convention; most browsers include it.

Windows NT 10.0; Win64; x64 → Operating system info.

AppleWebKit/537.36 → Rendering engine.

Chrome/114.0.0.0 → Browser version.

Safari/537.36 → Compatibility information.

How to Use It in Python Requests
import requests

url = "https://www.python.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(response.status_code)  # Should return 200 if successful


 Now the server thinks the request is coming from a real browser, not a bot.
 What is Rate Limiting?

Rate limiting is the practice of slowing down your requests to a website so that you don’t overload its server.

Websites have limited resources; too many rapid requests can crash the server or get your IP banned.

It’s considered good scraping etiquette and is part of ethical web scraping.

How to Implement Rate Limiting in Python

You can use the time.sleep() function to pause your scraper between requests.
What is robots.txt?

robots.txt is a text file placed by websites to tell web crawlers (like Googlebot or your scraper) which pages can or cannot be accessed.

It’s usually located at the root of a website, e.g.: https://www.python.org/robots.txt
Why Respect robots.txt?

Ethical scraping – Avoid accessing restricted content.

Avoid legal issues – Some sites may block IPs or take action if rules are ignored.

Prevent server overload – Following rules helps servers handle traffic efficiently.
Tip for Scrapers

Always read robots.txt before scraping a website.

Only scrape pages that are allowed.

Combine with rate limiting and User-Agent headers for safe, ethical scraping.

Best Practices for Web Scraping
Start Small:
Test on simple websites before moving to complex targets.
Use Caching:
Avoid redundant requests by caching scraped data.
Monitor Changes:
Websites may change their structure; write adaptable code.
Store Data Efficiently:
Save data in formats like JSON or CSV for easy access.

BeautifulSoup (from bs4) – To parse HTML and extract specific data.

pandas – Optional, for storing and processing scraped data in tables. What is Pandas?

Pandas is an open-source Python library used for data analysis and manipulation.

It provides data structures like:

Series → one-dimensional labeled array (like a column)

DataFrame → two-dimensional labeled table (like an Excel sheet or SQL table)

It’s widely used for:

Reading/writing CSV, Excel, JSON, SQL, etc.

Cleaning and transforming data

Performing calculations and aggregations

Preparing data for visualization or machine learning



