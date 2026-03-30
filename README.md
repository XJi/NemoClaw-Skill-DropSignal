# NemoClaw-Skill-DropSignal
A beta price tracker skill for NemoClaw 

 - The skill is complete and ready for use. You'll need to customize the configuration in skills/price-tracker/config.json with your specific tracking targets and      
 email settings before it can run automatically. The cron job is already set up to execute the skill daily at 4PM PT.  

 ## Next Steps
To activate the skill, you'll need to:
- 1. Edit skills/price-tracker/config.json with: Your actual products to track (name, URL, CSS selector for price element), Your email SMTP settings (server, port, credentials), Any threshold adjustments if needed
- 2. Test it manually (optional): 
```
bash python3 skills/price-tracker/scripts/price_tracker.py
```