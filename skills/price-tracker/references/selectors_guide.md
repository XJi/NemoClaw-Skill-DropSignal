```
Selector: `.price-current`

## Tips for Reliable Selectors

1. **Prefer ID selectors** when available (`#element-id`)
2. **Use attribute selectors** for data attributes (`[data-price]`, `[itemprop="price"]`)
3. **Avoid overly specific selectors** that might break with site updates
4. **Test on multiple pages** if tracking similar products
5. **Consider fallback selectors** in case primary selector fails

## Troubleshooting

If your selector isn't working:
- Check if the element is inside an iframe
- Verify the site isn't blocking requests (you might need headers/delay)
- Ensure the price isn't loaded dynamically after initial HTML load
- Look for price elements that might be hidden by CSS (display: none, visibility: hidden)

## Site-Specific Notes

Some sites have particular challenges:
- **Sites with heavy JavaScript**: May require tools like Selenium instead of simple requests+BeautifulSoup
- **Sites with anti-bot measures**: May require rotating user agents, proxies, or delays
- **International sites**: Price formats may vary (comma vs period for decimals, different currency symbols)

For difficult sites, consider:
1. Looking for JSON data in page source (often in `<script>` tags)
2. Checking if the site has a public API
3. Using browser automation tools for complex interactions
```