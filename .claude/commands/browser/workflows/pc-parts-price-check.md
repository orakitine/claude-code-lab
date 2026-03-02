---
mode: headless
---

# PC Parts Price Checker

Compare prices for a PC component across multiple Canadian retailers.

## Steps

1. Search for "{PROMPT}" on each of these sites (open each in a separate tab or session):
   - amazon.ca
   - bestbuy.ca
   - newegg.ca
   - canadacomputers.com
2. For each site:
   - Navigate to the site and search for the product
   - Find the top 2-3 relevant results (matching the product closely)
   - Capture: product name, price, availability (in stock / out of stock / ships in X days), and product page URL
   - Take a screenshot of the search results
3. Compile a comparison table sorted by price (lowest first):

   | # | Product | Store | Price | Availability | URL |
   |---|---------|-------|-------|-------------|-----|

4. Add a "Best Deal" recommendation at the bottom considering price, availability, and shipping
5. Save all screenshots to the output directory
