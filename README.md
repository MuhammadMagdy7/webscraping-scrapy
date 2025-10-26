# webscraping-scrapy

A simple Scrapy project that demonstrates scraping the “toscrape” demo site and exporting data to CSV/JSON. This repo is a practical, beginner-friendly example for learning Scrapy the right way.

Why this project matters
- Teaches solid scraping patterns with Scrapy (spiders, items, pipelines, settings).
- Produces structured, reusable data (CSV/JSON) you can analyze or share.
- Reproducible runs and clear commands for fast experimentation and teaching.

Key value points
- Uses Scrapy’s robust engine: fast, asynchronous requests and built-in throttling.
- Clear run commands to export data in the format you need (-O CSV/JSON).
- Easy to extend with items, pipelines, and middlewares as your needs grow.

Project structure (typical Scrapy layout)
- <project_name>/
  - scrapy.cfg (root config for the project)
  - <project_name>/
    - __init__.py
    - items.py        (define extracted data fields)
    - pipelines.py    (post-processing, cleaning, persistence)
    - settings.py     (project settings: user-agent, delays, pipelines, etc.)
    - spiders/        (your spiders live here)

Quick start
1) Clone and enter the repo:
   git clone https://github.com/MuhammadMagdy7/webscraping-scrapy.git
   cd webscraping-scrapy

2) (Optional) Create a virtual environment and install dependencies:
   python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -U pip scrapy

3) Discover available spiders:
   scrapy list

4) Run a spider and export results (replace <spider_name>):
   # Export to CSV
   scrapy crawl <spider_name> -O output.csv

   # Export to JSON
   scrapy crawl <spider_name> -O output.json

Tips for reliable scraping
- Be polite: set DOWNLOAD_DELAY and enable AutoThrottle to avoid hammering servers.
  In settings.py (example):
  AUTOTHROTTLE_ENABLED = True
  DOWNLOAD_DELAY = 0.5

- Keep selectors robust: prefer semantic attributes over volatile class names.
- Handle pagination: loop over next-page links until you reach the end.
- Validate and clean data in pipelines.py before export.

Common troubleshooting
- Command not found: ensure Scrapy is installed in your active environment (pip show scrapy). Use python -m scrapy if PATH issues persist.
- Empty output: check CSS/XPath selectors against the current site HTML; sites change over time.
- Blocked requests: add delays, randomize user-agents, and retry logic; respect robots.txt and site terms.

Suggested improvements
- Add requirements.txt with exact versions for reproducible installs.
- Add an examples/ folder with sample outputs and screenshots.
- Provide a data dictionary (what each field means) in README.
- Add tests for parsing functions (parsel selectors) and pipelines.

License
- MIT (see LICENSE)

Maintainer
- MuhammadMagdy7 — https://github.com/MuhammadMagdy7