# Example Site Configurations

This file provides example configurations for tracking products on popular e-commerce platforms.

## Amazon Configuration Examples

### Electronics
```json
{
  "id": "amazon_laptop_001",
  "name": "Dell XPS 15",
  "url": "https://www.amazon.com/dp/B08L5NRZ3K",
  "price_selector": "#priceblock_dealprice, #priceblock_ourprice, .a-price-whole"
}
```

### Books
```json
{
  "id": "amazon_book_001",
  "name": "Python Crash Course",
  "url": "https://www.amazon.com/dp/1593279280",
  "price_selector": "#priceblock_dealprice, #priceblock_ourprice, .a-price-whole"
}
```

## eBay Configuration Examples

### Fixed Price Items
```json
{
  "id": "ebay_phone_001",
  "name": "Samsung Galaxy S23",
  "url": "https://www.ebay.com/itm/123456789012",
  "price_selector": "#prcIsum, .notranslate, #mm-saleDscPrc"
}
```

### Auction Items (Current Bid)
```json
{
  "id": "ebay_auction_001",
  "name": "Vintage Rolex Watch",
  "url": "https://www.ebay.com/itm/987654321098",
  "price_selector": "#prcIsum, .notranslate"
}
```

## Walmart Configuration Examples

### General Products
```json
{
  "id": "walmart_tv_001",
  "name": "Samsung 65\" 4K TV",
  "url": "https://www.walmart.com/ip/Samsung-65-Class-QLED-Q60A-Series/123456789",
  "price_selector": ".price-current, .price-sales, .price-group"
}
```

## Target Configuration Examples

### Home Goods
```json
{
  "id": "target_blanket_001",
  "name": "Weighted Blanket",
  "url": "https://www.target.com/p/weighted-blanket/-/A-12345678",
  "price_selector": "[data-test='product-price'], .price-display, .price-tag"
}
```

## Best Buy Configuration Examples

### Electronics
```json
{
  "id": "bestbuy_headphones_001",
  "name": "Sony WH-1000XM5",
  "url": "https://www.bestbuy.com/site/sony-wh-1000xm5-noise-canceling-headphones/6503145.p",
  "price_selector": ".price-current, .price-sale, .price-block__price"
}
```

## Generic Configuration Template

For sites not listed above, use this template and adjust the selector:

```json
{
  "id": "unique_product_id",
  "name": "Product Name",
  "url": "https://example.com/product-page",
  "price_selector": "CSS_SELECTOR_FOR_PRICE_ELEMENT"
}
```

## Tips for Finding Selectors

1. **Use browser dev tools**: Right-click price → Inspect → Find unique identifier
2. **Try multiple selectors**: Separate with commas for fallbacks
3. **Test in console**: `document.querySelector('YOUR_SELECTOR')` should return the price element
4. **Check for currency symbols**: Selectors should capture the full price including symbols if needed
5. **Consider parent elements**: Sometimes you need to get text from a parent element

## Handling Different Price Formats

Some sites show prices differently:
- **With tax**: `price_selector` might need to target price before tax
- **Member prices**: Look for selectors that show both regular and member price
- **Sale vs regular**: Some sites have separate elements for sale and regular prices

For complex cases, you might need to:
1. Create multiple selectors and parse the results
2. Use JavaScript execution to compute final price
3. Look for JSON-LD structured data in the page