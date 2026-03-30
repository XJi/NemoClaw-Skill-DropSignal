#!/usr/bin/env python3
"""
Price Tracker - Main orchestrator script
Tracks product prices and sends notifications for significant deals
"""

import os
import json
import logging
from datetime import datetime
from scrape_prices import scrape_prices
from compare_prices import compare_prices
from send_notifications import send_notifications

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_config():
    """Load configuration from config.json"""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("Configuration file not found. Please create config.json")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing config.json: {e}")
        return None

def load_price_history():
    """Load historical price data"""
    history_path = os.path.join(os.path.dirname(__file__), '..', 'price_history.json')
    try:
        with open(history_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.info("No price history found. Starting fresh.")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing price_history.json: {e}")
        return {}

def save_price_history(history):
    """Save price history to file"""
    history_path = os.path.join(os.path.dirname(__file__), '..', 'price_history.json')
    try:
        with open(history_path, 'w') as f:
            json.dump(history, f, indent=2)
        logger.info("Price history saved")
    except Exception as e:
        logger.error(f"Error saving price history: {e}")

def main():
    """Main price tracking workflow"""
    logger.info("Starting price tracker...")
    
    # Load configuration
    config = load_config()
    if not config:
        return
    
    # Load historical prices
    price_history = load_price_history()
    
    # Scrape current prices
    logger.info("Scraping current prices...")
    current_prices = scrape_prices(config)
    
    if not current_prices:
        logger.warning("No prices scraped. Exiting.")
        return
    
    # Compare prices and detect deals
    logger.info("Comparing prices and detecting deals...")
    deals = compare_prices(current_prices, price_history, config)
    
    # Send notifications for deals found
    if deals:
        logger.info(f"Found {len(deals)} deals. Sending notifications...")
        send_notifications(deals, config)
    else:
        logger.info("No significant deals found.")
    
    # Update price history
    price_history.update(current_prices)
    save_price_history(price_history)
    
    logger.info("Price tracking completed.")

if __name__ == "__main__":
    main()