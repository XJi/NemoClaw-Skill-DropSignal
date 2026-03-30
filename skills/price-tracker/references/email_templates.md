# Email Templates for Price Tracker Notifications

This file contains template designs for deal notification emails sent by the price tracker skill.

## Default HTML Template

The default template used in `send_notifications.py` includes:
- Clean, responsive design
- Clear deal categorization (price drops vs promotions)
- Visual distinction between deal types
- Product images (if available)
- Clear call-to-action buttons

## Alternative Template Options

### Simple Text Template
For environments where HTML email isn't preferred or supported:

```
Price Tracker Alert: {{deal_count}} Deal{{deal_count_plural}} Found!

{% for deal in deals %}
====================
{{deal.product_name}}
{% if deal.type == 'price_drop' -->
Price Drop Alert! 
Previous Price: ${{deal.historical_price}}
Current Price:   ${{deal.current_price}}
Savings:         ${{deal.historical_price - deal.current_price}} ({{deal.drop_percentage}}%)
{% else %}
Site-wide Promotion!
Discount: {{deal.discount_percentage}}% off
{% endif %}
Product URL: {{deal.url}}
Detected: {{deal.timestamp|date}}
====================

{% endfor %}
This is an automated message from your Price Tracker skill.
```

### Minimal HTML Template
A lighter-weight HTML option:

```html
<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
  <h2>Price Tracker Alert</h2>
  <p>{{deal_count}} new deal{{deal_count_plural}} found:</p>
  
  {% for deal in deals %}
  <div style="border: 1px solid #eee; margin: 15px 0; padding: 15px; border-radius: 5px;">
    <h3 style="margin-top: 0;">{{deal.product_name}}</h3>
    <p><strong>Price:</strong> ${{deal.current_price}}</p>
    {% if deal.type == 'price_drop' %}
    <p style="color: #d32f2f;"><strong>Drop:</strong> {{deal.drop_percentage}}% from ${{deal.historical_price}}</p>
    {% else %}
    <p style="color: #388e3c;"><strong>Promotion:</strong> {{deal.discount_percentage}}% off</p>
    {% endif %}
    <p><a href="{{deal.url}}" style="background: #1976d2; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px;">View Product</a></p>
    <p style="font-size: 0.9em; color: #666;">Detected: {{deal.timestamp}}</p>
  </div>
  {% endfor %}
  
  <p style="font-size: 0.9em; color: #999; margin-top: 30px;">
    This is an automated message from your Price Tracker skill.
  </p>
</div>
```

## Template Customization Guide

### Variables Available
All templates receive a context with:
- `deals`: List of deal dictionaries
- `deal_count`: Number of deals found
- `deal_count_plural`: "s" if deal_count != 1, otherwise empty string
- Each deal dictionary contains:
  - `product_name`: Name of the product
  - `url`: Product URL
  - `current_price`: Current price
  - `historical_price`: Previous price (for price drops)
  - `drop_percentage`: Percentage drop (for price drops)
  - `discount_percentage`: Discount percentage (for promotions)
  - `timestamp`: Unix timestamp of detection
  - `type`: Either "price_drop" or "promotion"

### Adding Product Images
To include product images in emails:
1. Modify the scraper to also extract image URLs
2. Add `image_url` field to deal data
3. Update templates to include `<img src="{{deal.image_url}}" alt="{{deal.product_name}}">`

### Localization
For non-English emails:
1. Extract text strings to variables
2. Create language-specific template versions
3. Add language selection to config

## Testing Templates

To test email templates without sending actual emails:
1. Use the `__main__` block in `send_notifications.py`
2. Modify to print HTML instead of sending
3. Or use a local SMTP testing tool like MailHog or Papercut

## Best Practices

1. **Keep it simple**: Clear, scannable layouts work best for deal alerts
2. **Brand consistency**: Use colors and fonts that match your preferences
3. **Mobile-friendly**: Ensure templates render well on mobile devices
4. **Clear CTAs**: Make "View Product" buttons prominent
5. **Unsubscribe option**: Consider adding an unsubscribe link for regular alerts
6. **Legal compliance**: Include your physical address if required by anti-spam laws