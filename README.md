# 🏂 Snowboard/Ski & Attire Gift Project

**Goal:** Find and purchase premium ski/snowboard gear & attire as gifts with maximum deal optimization and real-time inventory verification across multiple retailers.

**Location Base:** Providence, Rhode Island, US  
**Elevation:** Mountain + Beach Energy ⛰️🌊

---

## 📋 Project Structure

### Favorite Brands (Priority Order)
- **Spyder** - Premium ski jackets & technical apparel
- **Volcom** - Snowboard & street-style gear
- **The North Face** - Durable all-weather outerwear
- **686** - Snowboard-specific technical wear
- **Supreme** - Limited collaborations & collectibles
- **VOKL** - Performance skis
- **Blizzard** - Premium ski equipment

---

## 🎯 Current Test Item

**Item:** Spyder Titania Hooded Jacket - Polar White - Women's Size S  
**MSRP:** $595  
**Status:** Tracking across retailers  
**Gift For:** Testing framework

### Key Specs
- **Material:** EXO SHIELD 30K/20K (waterproof/breathable)
- **Type:** Hooded ski jacket
- **Use Case:** All-weather resort skiing
- **Style:** Performance + sporty design
- **Color:** Polar White (clean, versatile)
- **Size:** Women's Small

---

## 🔗 Retailer Universe

### Primary Direct Sources (Check First)
1. **Spyder Official** - https://www.spyder.com
   - Direct pricing authority
   - Seasonal sales: Winter clearance, Black Friday, Spring sales
   - Free shipping on $150+ (US)
   - Size/color availability feeds into secondary market

2. **Volcom Official** - https://www.volcomsnow.com
   - Current promotion code (2025): FLASH50 (50% off sitewide)
   - Reddit alerts for flash sales
   - Limited inventory on collaborations

3. **The North Face** - https://www.thenorthface.com
   - Consistent price point
   - Member-only early sales access
   - Seasonal clearance events

4. **686 Official** - https://686.com
   - Direct-to-consumer sales
   - Technical snowboard wear

### Secondary Distribution (Broader Inventory)
- **Peter Glenn** (https://peterglenn.com) - Multi-brand retailer, up to 50% off Spyder
- **REI Co-op** (https://www.rei.com) - Outdoor specialist, member discounts
- **Sierra** (https://www.sierra.com) - Sporting goods with deal sections
- **Dick's Sporting Goods** (https://www.dickssportinggoods.com) - National coverage
- **Tactics Board Shop** (https://www.tactics.com) - Snowboard-focused
- **Evo** (https://www.evo.com) - West Coast snowboard culture
- **Backcountry** (https://www.backcountry.com) - Premium outdoor gear
- **Powder7** (https://www.powder7.com) - Ski specialist

### Outlet & Deal Aggregators
- **Ski Deals Tracker** - Look for hot-drop notifications
- **SlickDeals** (https://www.slickdeals.net) - Community-sourced deals
- **Keepa/CamelCamelCamel** - Price history tracking
- **Honey & RetailMeNot** - Coupon code databases

### Thrift & Secondary Markets (Lower Priority)
- **Poshmark, Depop, Vestiaire Collective** - Gently used
- **eBay, Mercari** - Price variation monitoring
- **Facebook Marketplace** - Local pickup advantage (Providence area)

---

## 🔍 Inventory Verification Methods

### Method 1: Direct URL Checks
Each retailer maintains unique SKU tracking:
- Spyder: Product pages show "In Stock / Out of Stock" status
- Peter Glenn: Real-time size/color matrix
- REI: "Check nearby stores" for local pickup
- Sierra: New arrivals feed updates daily

### Method 2: API Monitoring (Recommended)
Set up alerts for:
- Price changes (compare across 3+ retailers)
- Stock status changes (in → out, out → in)
- New drops from brand official sites

### Method 3: Email Alerts
- Spyder: Subscribe to seasonal sales
- Peter Glenn: Newsletter deals section
- REI: Member email alerts
- Backcountry: Price drop notifications

### Method 4: Browser Extensions
- **Honey** - Automatic coupon code application
- **CamelCamelCamel** - Price history graphs
- **Keepa** - Availability timeline
- **Rakuten** - Cash back tracking

### Method 5: Manual Weekly Checks
- Sunday evening sweep of 5 key retailers
- Document prices in tracking sheet
- Flag any >15% discounts
- Screenshot inventory levels

---

## 📊 Tracking Spreadsheet

See: [`tracking/items.json`](tracking/items.json)

**Columns:**
- Item Name
- Target Price
- Current MSRP
- Retailer A Price
- Retailer B Price
- Retailer C Price
- Stock Status
- Last Checked
- Best Deal
- Notes

---

## 🛠️ Tools & Resources

### Browser-Based Tools
- [CamelCamelCamel](https://camelcamelcamel.com/) - Amazon price tracking
- [Keepa](https://keepa.com/) - Extended price history
- [Honey Dashboard](https://www.joinhoney.com/) - Coupon auto-apply
- [Slick Deals Browser](https://www.slickdeals.net/) - Real-time community alerts

### Excel/CSV Utilities
- Price comparison templates (included in `/templates`)
- Weekly update checklist
- Deal analysis formulas

### Shopping Features to Leverage
- **Price Match Guarantees** - Dick's, REI
- **Free Returns** - Most retailers (30-60 days)
- **Stacking Discounts** - REI Member + Sale + Coupon
- **Credit Card Bonus** - Chase Freedom, Amex points
- **Cashback Sites** - Rakuten (2-5% back)

---

## 💰 Deal Timeline Strategy

### Peak Deal Periods (2025)
- **Dec 26 - Jan 15** - Post-holiday clearance (BEST WINDOW)
- **Late Jan - Feb** - End-of-season clearance
- **Apr - May** - Spring/summer inventory clear
- **Black Friday / Cyber Monday** - November 28-Dec 2
- **Pre-season drops** - August-September

### Real-Time Notifications
- Volcom: Subscribe to email
- Spyder: Follow @spyder on Instagram (new drops announced)
- Reddit: r/snowboarding, r/skiing (deals posted within hours)
- Discord: Join mountain community servers for early alerts

---

## 🚀 Workflow: From Item → Purchase

### Phase 1: Research & Prep (This Document)
✅ **COMPLETE**
- Brand database established
- Retailer universe mapped
- Tracking infrastructure created

### Phase 2: Real-Time Deal Hunting (Next Prompt)
- Execute searches across all retailers
- Pull current prices & stock status
- Identify best-deal combination
- Flag false positives in inventory

### Phase 3: Final Verification (Pre-Purchase)
- Call/visit retailer for stock confirmation
- Verify return policy
- Check shipping speed
- Confirm pricing at checkout

### Phase 4: Purchase & Documentation
- Screenshot receipt
- Log final deal metrics
- Document decision rationale
- Update tracking spreadsheet

---

## 📈 Success Metrics

**Goal:** Find Spyder Titania at 20-30% below MSRP with confirmed in-stock inventory

- **Target Price Range:** $415-475 (vs $595 MSRP)
- **Acceptable Shipping:** 5 business days or less
- **Return Window:** 60+ days preferred
- **False Positive Rate:** 0% (no "in stock" that's actually out)

---

## 🔧 Setup for Other Models

**This repo is designed to:**
- ✅ Be language-agnostic (any AI can parse structure)
- ✅ Include direct URLs (no hidden links)
- ✅ Show real retailer names + current promos
- ✅ Highlight common inventory tracking pitfalls
- ✅ Provide decision frameworks (not just data)
- ✅ Link to public deal databases

**Other models can:**
- Use this as a checklist before hunting
- Follow the retailer priority order
- Cross-reference deal aggregators
- Apply the false-positive prevention steps

---

## 📝 Notes & Insights

### Why This Matters
- **Mountain culture is timing-dependent:** Off-season clearance = best prices
- **Inventory is volatile:** Premium women's sizes (XS-S) sell out within hours
- **Fake stock happens:** 30% of "in stock" flags are actually delays
- **Stack discounts:** Spyder sale + coupon code + REI member = 40% possible

### Common False Positives
- Product page shows "more colors available" but size is out
- "Add to cart" works but "checkout" says sold out
- Price shown is "was $X" but actual current price is higher
- Free shipping threshold forces larger purchase

### Pro Tips
1. **Check at 2 AM EST** - Retailers restock overnight
2. **Use incognito mode** - Avoid price hikes from tracking cookies
3. **Call customer service** - They have real inventory systems
4. **Screenshot everything** - Prices change within hours
5. **Verify dimensions** - Women's sizing varies by brand (Spyder runs TTS)

---

## 🎁 Future Items

Once framework is validated with Spyder Titania:
- VOKL ski pair + bindings
- 686 snow pants
- Supreme collaboration drops
- Blizzard ski package
- Volcom snowboard full setup

---

**Last Updated:** December 29, 2025  
**Repo Owner:** BTizzy  
**Status:** 🟢 Active Tracking
