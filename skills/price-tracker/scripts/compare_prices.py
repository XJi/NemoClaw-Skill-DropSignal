#!/usr/bin/env python3
"""
Compare current prices with historical data to detect deals
"""

import json
import logging
import os

logger = logging.getLogger(__name__)

def compare_prices(current_prices, price_history, config):
    """
    Compare current prices with historical data to detect significant deals
    
    Args:
        current_prices (dict): Current scraped prices
        price_history (dict): Historical price data
        config (dict): Configuration with thresholds and settings
        
    Returns:
        list: List of deals found
    """
    deals = []
    
    # Get thresholds from config
    price_drop_threshold = config.get('price_drop_threshold', 0.25)  # 25%
    promotion_threshold = config.get('promotion_threshold', 0.30)   # 30%
    
    for product_id, current_data in current_prices.items():
        try:
            current_price = current_data['price']
            product_name = current_data['name']
            url = current_data['url']
            
            # Check for price drop compared to historical data
            if product_id in price_history:
                historical_price = price_history[product_id].get('price', current_price)
                if historical_price > 0:  # Avoid division by zero
                    price_drop_ratio = (historical_price - current_price) / historical_price
                    
                    if price_drop_ratio >= price_drop_threshold:
                        deals.append({
                            'type': 'price_drop',
                            'product_id': product_id,
                            'product_name': product_name,
                            'url': url,
                            'current_price': current_price,
                            'historical_price': historical_price,
                            'drop_percentage': price_drop_ratio * 100,
                            'timestamp': current_data['timestamp']
                        })
                        logger.info(f"Price drop detected for {product_name}: {price_drop_ratio*100:.1f}%")
            
            # Check for site-wide promotions (this would require additional scraping)
            # For now, we'll implement a simple check - in practice, this would need
            # to scrape for banner text or promotion indicators
            promotion_data = check_for_promotions(current_data, config)
            if promotion_data:
                deals.append(promotion_data)
                
        except Exception as e:
            logger.error(f"Error comparing prices for product {product_id}: {e}")
            continue
    
    return deals

def check_for_promotions(product_data, config):
    """
    Check for site-wide promotions (placeholder implementation)
    In a real implementation, this would scrape for promotion banners, sale tags, etc.
    """
    # This is a simplified version - real implementation would need to:
    # 1. Scrape the homepage or category pages for promotion indicators
    # 2. Look for text like "Site-wide Sale", "30% off everything", etc.
    # 3. Extract the discount percentage
    
    # For now, we'll return None to indicate no promotion detected
    # Users would need to enhance this based on the specific sites they're tracking
    return None

if __name__ == "__main__":
    # For testing
    logging.basicConfig(level=logging.INFO)
    
    # Load config and history for testing
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    history_path = os.path.join(os.path.dirname(__file__), '..', 'price_history.json')
    
    config = {}
    price_history = {}
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
    
    if os.path.exists(history_path):
        with open(history_path, 'r') as f:
            price_history = json.load(f)
    
    # Mock current prices for testing
    current_prices = {
        'test1': {
            'price': 75.0,
            'name': 'Test Product',
            'url': 'https://example.com/product',
            'timestamp': 1234567890
        }
    }
    
    # Mock historical price
    price_history['test1'] = {
        'price': 100.0,
        'timestamp': 1234567800
    }
    
    deals = compare_prices(current_prices, price_history, config)
    print(json.dumps(deals, indent=2))