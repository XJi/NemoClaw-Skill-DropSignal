#!/usr/bin/env python3
"""
Scrape prices from e-commerce websites
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import json
import os
import logging

logger = logging.getLogger(__name__)

def scrape_prices(config):
    """
    Scrape current prices from configured websites
    
    Args:
        config (dict): Configuration containing products to track
        
    Returns:
        dict: Current prices keyed by product ID
    """
    current_prices = {}
    
    # Get products to track from config
    products = config.get('products', [])
    
    for product in products:
        try:
            product_id = product.get('id')
            url = product.get('url')
            price_selector = product.get('price_selector')
            name = product.get('name', f'Product {product_id}')
            
            if not all([product_id, url, price_selector]):
                logger.warning(f"Missing required fields for product {product_id}")
                continue
            
            # Add headers to appear more like a real browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
            }
            
            # Add delay to be respectful to servers
            time.sleep(random.uniform(1, 3))
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            price_element = soup.select_one(price_selector)
            
            if price_element:
                price_text = price_element.get_text().strip()
                # Extract numeric price from text (remove currency symbols, commas, etc.)
                import re
                price_match = re.search(r'[\d,]+\.?\d*', price_text.replace(',', ''))
                if price_match:
                    price = float(price_match.group())
                    current_prices[product_id] = {
                        'price': price,
                        'name': name,
                        'url': url,
                        'timestamp': time.time(),
                        'raw_text': price_text
                    }
                    logger.info(f"Scraped price for {name}: ${price}")
                else:
                    logger.warning(f"Could not extract price from text: {price_text}")
            else:
                logger.warning(f"Price selector '{price_selector}' not found on {url}")
                
        except Exception as e:
            logger.error(f"Error scraping {product.get('name', 'unknown product')}: {e}")
            continue
    
    return current_prices

if __name__ == "__main__":
    # For testing - load config and run
    logging.basicConfig(level=logging.INFO)
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
        prices = scrape_prices(config)
        print(json.dumps(prices, indent=2))
    else:
        print("Config file not found for testing")