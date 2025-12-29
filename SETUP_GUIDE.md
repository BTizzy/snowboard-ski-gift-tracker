# Setup Guide: Snowboard/Ski Gift Tracker

## Quick Start (5 Minutes)

### Step 1: Clone & Navigate
```bash
git clone https://github.com/BTizzy/snowboard-ski-gift-tracker.git
cd snowboard-ski-gift-tracker
```

### Step 2: Review Core Files
- **README.md** - Project overview & brand universe
- **tracking/items.json** - Current tracked items (Spyder Titania test case)
- **data/brand_retailer_matrix.json** - All brand + retailer intel

### Step 3: Browser Prep (Extensions)

Install these in your preferred browser:

1. **Honey** - https://www.joinhoney.com/
   - Auto-applies coupon codes at checkout
   - Tracks cashback opportunities
   - Instant savings calculation

2. **Rakuten** - https://www.rakuten.com/
   - 2-5% cashback on purchases
   - Watch for seasonal bonus categories

3. **CamelCamelCamel** (Amazon only) - https://camelcamelcamel.com/
   - Historical price tracking
   - Price drop alerts
   - Not needed for Spyder, but useful for other gear

### Step 4: Email Subscriptions (Instant Alerts)

Sign up for these to catch sales within hours:

- [ ] Spyder email list - https://www.spyder.com (footer)
- [ ] Peter Glenn deals - https://peterglenn.com (subscribe)
- [ ] REI Member emails - https://www.rei.com/membership
- [ ] Volcom newsletter - https://www.volcomsnow.com
- [ ] The North Face alerts - https://www.thenorthface.com
- [ ] SlickDeals email - https://www.slickdeals.net (ski category)

### Step 5: Browser Bookmarks

Create a "Ski Gift Hunt" folder with:

```
Ski Gift Hunt/
├── Spyder Titania (Polar White, S)
│   └── https://www.spyder.com/products/womens-titania-jacket-white
├── Peter Glenn
│   └── https://peterglenn.com/womens/jackets/
├── REI Search
│   └── https://www.rei.com/search?q=spyder+titania
├── Sierra
│   └── https://www.sierra.com/s~waterproof-and-insulated/womens-ski-and-snowboard-jackets/
├── Dick's Sporting Goods
│   └── https://www.dickssportinggoods.com/search?q=spyder+titania
├── Deal Trackers
│   ├── SlickDeals: https://www.slickdeals.net
│   └── RetailMeNot: https://www.retailmenot.com
└── Community
    └── r/snowboarding: https://www.reddit.com/r/snowboarding/
```

---

## Workflow: Daily Deal Hunting

### Morning Sweep (5 minutes)
**Time:** 8-9 AM EST (after overnight restocks)

1. **Check email alerts**
   - Spyder: Any new drops?
   - Peter Glenn: Sale updates?
   - REI: Member-only deals?

2. **Visit primary retailers**
   - Spyder official: https://www.spyder.com/products/womens-titania-jacket-white
   - Peter Glenn: https://peterglenn.com/womens/jackets/
   - REI: https://www.rei.com/search?q=spyder+titania

3. **Document in tracking/items.json**
   - Update price field
   - Update stock_status
   - Add timestamp

### Evening Sweep (5 minutes)
**Time:** 8-9 PM EST (before daily reset)

1. **Check r/snowboarding** - Sort by new
   - Any flash sale announcements?
   - Volcom codes posted?

2. **Revisit top retailers**
   - Check for price drops
   - Look for new promotional codes

3. **Compare prices**
   - Build simple spreadsheet:
     ```
     Retailer | Spyder Titania S | Price | Discount % | Stock S | Notes
     Spyder   | MSRP            | $595  | 0%        | Yes    | Baseline
     Peter    | Yes             | TBD   | TBD       | Check  | 
     REI      | Yes             | TBD   | TBD       | Check  |
     Sierra   | TBD             | TBD   | TBD       | Check  |
     Dick's   | TBD             | TBD   | TBD       | Check  |
     ```

### Weekly Deep Dive (15 minutes)
**Time:** Sunday 6 PM EST

1. **Screenshot all active retailers**
   - Create folder: `tracking/screenshots/week_of_DEC29/`
   - Screenshot each retailer
   - Include URL and timestamp

2. **Calculate deal metrics**
   - Best current price: ?
   - Best discount %: ?
   - Best combo (price + shipping + returns): ?

3. **Update decision log** in tracking/items.json
   ```json
   "decision_log": [
     {
       "date": "2025-12-29",
       "action": "Weekly review",
       "findings": "...",
       "next_steps": "..."
     }
   ]
   ```

---

## How to Avoid False Positives

### Problem: "In Stock" that's Actually Out

**Detection Methods:**

1. **Try to Add to Cart**
   - ✅ Works → Real stock
   - ❌ Error → Fake stock (common false positive)

2. **Check Size Availability Matrix**
   - Look at ALL available sizes
   - If only L/XL show as "In Stock" but S is grayed out → Out of stock

3. **Call the Retailer**
   - Spyder: +1-800-SPYDER-1 (8 AM-5 PM PT)
   - Peter Glenn: Check website for phone
   - REI: Member services line
   - **Tip:** Call 11:30 AM EST when staff are less busy

4. **Check Product Page Carefully**
   - "More colors available" ≠ Your color available
   - "More sizes available" ≠ Size S available
   - Always verify exact SKU combination

5. **Recent Reviews**
   - If reviews show "sold out in hours," product is popular
   - Set alerts earlier than you think necessary

### Problem: Price Shown ≠ Price at Checkout

**Prevention:**

1. **Screenshot the price**
   - Full page screenshot with URL visible
   - Include timestamp (browser dev tools show this)

2. **Incognito Mode**
   - Retailers show lower prices in incognito
   - They raise prices based on tracking cookies
   - Ctrl+Shift+N (Windows) or Cmd+Shift+N (Mac)

3. **Check Honey Dashboard**
   - Before adding to cart, check Honey price history
   - It shows if site has raised prices recently

4. **Verify Free Shipping**
   - Spyder: States "FREE over $150" prominently
   - But verify in cart - sometimes changes for:
     - Large items (skis)
     - Multiple items that exceed weight limits
     - International addresses

---

## Alert Automation (Optional)

### Email Alerts

**Create Gmail filter for deal notifications:**

1. Go to Gmail → Settings → Filters and Blocked Addresses
2. Create filter for:
   - From: `retailer@spyder.com OR newsletter@peterglenn.com`
   - Label as: "Ski Deals"
   - Star the email

### Browser Notifications

**Using Honey/Rakuten:**
- Both have browser notification options
- Enable for price drops and cashback opportunities

### Reddit Alerts

**Subscribe to r/snowboarding deal posts:**

1. Visit https://www.reddit.com/r/snowboarding/
2. "Sort by New" (top right)
3. Check 1x daily
4. Search for: `Volcom`, `Spyder`, `deal`, `sale`

---

## Price Comparison Formula

Don't just look at final price - calculate total value:

```
TRUE_COST = (Price) + (Shipping) - (Cashback) - (Tax Savings)

Example:
Spyder Official: $595 + Free shipping - $0 cashback = $595 (baseline)
Peter Glenn:    $465 + Free shipping - $10 (Rakuten) = $455 ✅ BEST
REI:            $535 + Free 2-day - $25 (member) = $510
Dick's:         $520 + Free (>$99) - $15 (coupon) = $505
```

---

## When to Pull the Trigger

### BUY IF:
- Price is 25%+ below MSRP ($595 → $446 or less)
- Stock confirmed in your size (call retailer)
- Free or cheap shipping
- 60+ day return window
- Email confirmation arrives instantly

### WAIT IF:
- Still in normal price range (MSRP $595)
- Size availability uncertain
- Shipping costs >$15
- Return window <30 days
- Stock status "Coming Soon"

### RED FLAGS (Don't Buy):
- "In stock" but add-to-cart fails
- "Final sale" or "No returns"
- Shipping to non-contiguous US takes 2+ weeks
- Third-party seller on marketplace (use official only)
- Price seems "too good" (verify authenticity)

---

## Documentation

### What to Screenshot

When you find a good deal:

1. **Product page** (full page, scrolled down to see all options)
2. **Price/Stock** (highlight the specific detail)
3. **Shipping info** (confirm free shipping qualifies)
4. **Return policy** (screenshot policy)
5. **URL** (visible in address bar)

Save as: `tracking/deal_screenshots/YYYY-MM-DD_RETAILER_itemname.png`

### Update items.json

When you find a new price point:

```json
{
  "date": "2025-12-31",
  "retailer": "Peter Glenn",
  "price": 465,
  "discount_percent": 22,
  "stock_status": "In Stock",
  "sizes_available": ["XS", "S", "M", "L"],
  "verified": true,
  "notes": "Honey showed no additional coupons available. Free shipping over $150 threshold met."
}
```

---

## Success Checklist: Before Purchasing

- [ ] Price is confirmed in incognito mode
- [ ] Stock confirmed by calling retailer (not just website)
- [ ] Size S Polar White specifically available
- [ ] Shipping is free or <$20
- [ ] Return policy is 60+ days
- [ ] No hidden fees (tax calculated)
- [ ] Price comparison done across 3+ retailers
- [ ] Screenshots taken and saved
- [ ] Best deal identified and documented
- [ ] Coupon codes checked (Honey, RetailMeNot)
- [ ] Cashback option verified (Rakuten, Honey)

---

## Ongoing Maintenance

### Weekly
- Update items.json with new tracking data
- Clean up old deal screenshots (keep last 2 weeks)
- Review decision_log to see if patterns emerge

### Monthly
- Update brand_retailer_matrix.json with new deal patterns
- Archive old tracking snapshots
- Review total savings vs. MSRP

### After Purchase
1. Screenshot receipt
2. Save to `tracking/purchases/`
3. Document final price paid in items.json
4. Update metadata with savings calculation
5. Note any lessons learned for next item

---

## Troubleshooting

### "Item shows 'In Stock' but add-to-cart fails"
→ This is the #1 false positive. Call retailer to confirm.

### "Price dropped $50 but I missed it"
→ Set email alerts. Next item will have push notifications enabled.

### "Free shipping threshold calculation is confusing"
→ Add $1-5 filler items (socks, stickers) to hit free shipping threshold.

### "Different prices for different devices"
→ Use incognito mode across all devices. Clear cookies.

### "Size S not available, only XS/M"
→ Check if other colors available in S. Women's sizing varies between colors.

---

## Questions?

Check the main README.md for:
- Complete retailer universe
- Brand-specific deal patterns
- Pro tips from mountain community
- Future items list

---

**Good luck on the hunt!** 🎿❄️
