```
---
name: price-tracker
description: Track product prices on specified websites and detect significant price drops (greater than 25%) or site-wide promotions (greater than 30% discount). Use when you want to monitor prices for products across multiple e-commerce sites and get notified via email when deals are found. The skill includes scripts for web scraping, price comparison, and email notifications.
---

# Price Tracker

## Overview

This skill enables tracking of product prices across multiple e-commerce websites. It provides tools to scrape product prices, compare them against historical prices, detect significant price drops or promotions, and send email notifications when deals are found.

## Workflow

The price tracking workflow consists of these steps:
1. **Configure targets** - Define which products and websites to monitor
2. **Scrape current prices** - Extract current prices from target websites
3. **Compare prices** - Check for price drops >25% or site-wide promotions >30%
4. **Send notifications** - Email alerts when significant deals are detected

## Configuration

To use this skill, you need to create a configuration file that specifies:
- List of products to track (name, URL, CSS selectors for price elements)
- Historical price data (can be stored and updated)
- Email settings for notifications
- Thresholds for price drop (25%) and promotion detection (30%)

## Key Features

- **Web scraping** - Extract price data from e-commerce sites using configurable selectors
- **Price comparison** - Compare current prices against historical data
- **Deal detection** - Identify price drops >25% and site-wide promotions >30%
- **Email notifications** - Send alerts when deals are found
- **Historical tracking** - Maintain price history for trend analysis

## Usage Examples

You might ask:
- "Track the price of this laptop on Amazon and Best Buy"
- "Monitor these 5 products for price drops over 25%"
- "Check if any of these websites have site-wide sales over 30% off"
- "Email me when this product's price drops significantly"

## Resources

### scripts/
Contains executable scripts for price tracking operations:
- `scrape_prices.py` - Scrapes current prices from configured websites
- `compare_prices.py` - Compares current vs historical prices and detects deals
- `send_notifications.py` - Sends email alerts when deals are found
- `price_tracker.py` - Main orchestrator script that runs the full workflow

### references/
Reference materials for effective price tracking:
- `selectors_guide.md` - Guide to finding correct CSS selectors for price elements on various sites
- `sites_config.md` - Example configurations for popular e-commerce platforms
- `email_templates.md` - Templates for deal notification emails

### assets/
(Not currently used - no template files or boilerplate needed for this skill)
sandbox@my-assistant:~$ vim ---
sandbox@my-assistant:~$ cat /sandbox/.openclaw-data/workspace/skills/price-tracker/SKILL.md 
sandbox@my-assistant:~$ cat /sandbox/.openclaw-data/workspace/skills/price-tracker/SKILL.md 
---
name: price-tracker
description: Track product prices on specified websites and detect significant price drops (greater than 25%) or site-wide promotions (greater than 30% discount). Use when you want to monitor prices for products across multiple e-commerce sites and get notified via email when deals are found. The skill includes scripts for web scraping, price comparison, and email notifications.
---

# Price Tracker

## Overview

This skill enables tracking of product prices across multiple e-commerce websites. It provides tools to scrape product prices, compare them against historical prices, detect significant price drops or promotions, and send email notifications when deals are found.

## Workflow

The price tracking workflow consists of these steps:
1. **Configure targets** - Define which products and websites to monitor
2. **Scrape current prices** - Extract current prices from target websites
3. **Compare prices** - Check for price drops >25% or site-wide promotions >30%
4. **Send notifications** - Email alerts when significant deals are detected

## Configuration

To use this skill, you need to create a configuration file that specifies:
- List of products to track (name, URL, CSS selectors for price elements)
- Historical price data (can be stored and updated)
- Email settings for notifications
- Thresholds for price drop (25%) and promotion detection (30%)

## Key Features

- **Web scraping** - Extract price data from e-commerce sites using configurable selectors
- **Price comparison** - Compare current prices against historical data
- **Deal detection** - Identify price drops >25% and site-wide promotions >30%
- **Email notifications** - Send alerts when deals are found
- **Historical tracking** - Maintain price history for trend analysis

## Usage Examples

You might ask:
- "Track the price of this laptop on Amazon and Best Buy"
- "Monitor these 5 products for price drops over 25%"
- "Check if any of these websites have site-wide sales over 30% off"
- "Email me when this product's price drops significantly"

## Resources

### scripts/
Contains executable scripts for price tracking operations:
- `scrape_prices.py` - Scrapes current prices from configured websites
- `compare_prices.py` - Compares current vs historical prices and detects deals
- `send_notifications.py` - Sends email alerts when deals are found
- `price_tracker.py` - Main orchestrator script that runs the full workflow

### references/
Reference materials for effective price tracking:
- `selectors_guide.md` - Guide to finding correct CSS selectors for price elements on various sites
- `sites_config.md` - Example configurations for popular e-commerce platforms
- `email_templates.md` - Templates for deal notification emails

### assets/
(Not currently used - no template files or boilerplate needed for this skill)
``` 