# Directory Structure & File Guide

## Complete File Map

```
snowboard-ski-gift-tracker/
├── README.md                          ⚔️ MAIN PROJECT OVERVIEW
├── PROJECT_SUMMARY.md                  🏂 START HERE - What you're getting
├── QUICK_REFERENCE.md                  🔏 ONE-PAGE CHEAT SHEET
├── SETUP_GUIDE.md                      📄 DETAILED WORKFLOW GUIDE
├── DIRECTORY_STRUCTURE.md              📁 THIS FILE
├── requirements.txt                    🐍 Python dependencies
├── .gitignore                          🔐 Safe local file handling
├── LICENSE                             (Optional) MIT recommended
├──
├── data/
│   └── brand_retailer_matrix.json         🤯 Brand profiles & retailer intel
├── tracking/
│   ├── items.json                          👍 MAIN TRACKING DATABASE
│   ├── snapshots/                          📸 (auto-created) Price snapshots
│   ├── screenshots/                        📾 (manual) Your retailer screenshots
│   └── purchases/                          ✅ (manual) Completed buys
├── scripts/
│   └── monitor_inventory.py                🐭 Python monitoring script
├── templates/
│   └── new_item_template.json              📋 Template for adding items
├── logs/
│   └── monitor.log                         (auto-created) Script logs
└── .git/                               (auto-created) Git history
```

---

## File Purpose Quick Reference

### 📄 Documentation Files (Read These First)

| File | Purpose | Read When |
|------|---------|----------|
| **PROJECT_SUMMARY.md** | Complete overview of what you're getting | First - 10 min read |
| **QUICK_REFERENCE.md** | One-page cheat sheet for daily use | Before each hunt |
| **SETUP_GUIDE.md** | Detailed step-by-step workflow | Once per week |
| **README.md** | Full project details + brand universe | Research phase |
| **DIRECTORY_STRUCTURE.md** | This file - where everything is | Navigation |

### 📅 Data Files (Update These)

| File | Purpose | Update Frequency |
|------|---------|------------------|
| **tracking/items.json** | Active tracked items + prices | Daily (with new prices) |
| **data/brand_retailer_matrix.json** | Brand & retailer intelligence | Monthly (new deals/patterns) |
| **templates/new_item_template.json** | Template for new items | Never (reference only) |

### 📀 Local Folders (Create as Needed)

| Folder | Purpose | Created By |
|--------|---------|------------|
| **tracking/snapshots/** | Auto-generated price tracking data | Python script |
| **tracking/screenshots/** | Your manual retailer screenshots | You |
| **tracking/purchases/** | Receipts for completed purchases | You |
| **logs/** | Python script execution logs | Python script |

### 🐭 Code Files (Run These)

| File | Purpose | How to Use |
|------|---------|----------|
| **scripts/monitor_inventory.py** | Automated price/stock checker | `python3 monitor_inventory.py` |

### ⚙️ Configuration Files

| File | Purpose |
|------|----------|
| **requirements.txt** | Python package dependencies |
| **.gitignore** | Files to exclude from Git |

---

## Where to Find What

### 🔏 "How do I...?"

**...start using this?**
→ Read PROJECT_SUMMARY.md (5 min) then QUICK_REFERENCE.md (2 min)

**...add a new item to track?**
→ Copy templates/new_item_template.json and add to tracking/items.json

**...understand each brand's deal patterns?**
→ See data/brand_retailer_matrix.json (JSON structure)

**...set up automated monitoring?**
→ Read scripts/monitor_inventory.py and run: `python3 monitor_inventory.py`

**...find a specific retailer's policies?**
→ data/brand_retailer_matrix.json → retailers section

**...record a deal I found?**
→ Update tracking/items.json → tracking_data array

**...log a completed purchase?**
→ Update tracking/items.json → decision_log + move status to "purchased"

**...troubleshoot an issue?**
→ SETUP_GUIDE.md → "Troubleshooting" section

**...understand the whole project?**
→ README.md (15 min comprehensive read)

---

## Daily Workflow File Map

### Morning Check (8-9 AM EST)

1. **Open:** QUICK_REFERENCE.md (daily checklist section)
2. **Update:** tracking/items.json (add new prices)
3. **Use:** Browser bookmarks (visit 5 retailers)

### Evening Check (8-9 PM EST)

1. **Open:** QUICK_REFERENCE.md (spreadsheet comparison table)
2. **Check:** r/snowboarding (sort by new)
3. **Update:** tracking/items.json (decision_log if prices moved)

### Weekly Review (Sunday 6 PM)

1. **Read:** PROJECT_SUMMARY.md (success criteria section)
2. **Update:** tracking/items.json (add weekly summary)
3. **Screenshot:** Save to tracking/screenshots/week_of_DATE/
4. **Analyze:** data/brand_retailer_matrix.json (any new patterns?)

### When Ready to Buy

1. **Verify:** QUICK_REFERENCE.md (success checklist)
2. **Execute:** Purchase + screenshot receipt
3. **Document:** tracking/items.json (final price + notes)
4. **Archive:** Move receipt to tracking/purchases/

---

## GitHub Navigation

### For Other Models/Humans Reviewing This

**Start here:**
1. README.md (comprehensive overview)
2. PROJECT_SUMMARY.md (what's included + next steps)
3. QUICK_REFERENCE.md (if quick decision needed)

**Then explore:**
- tracking/items.json (see test case setup)
- data/brand_retailer_matrix.json (understand framework)
- scripts/monitor_inventory.py (see automation approach)
- templates/new_item_template.json (understand extensibility)

**For improvements:**
- Suggest updates to brand_retailer_matrix.json (new deals/patterns)
- Extend scripts/monitor_inventory.py (new retailers)
- Add new items to tracking/items.json (test on more products)

---

## File Size Reference

| File | Size | Type |
|------|------|------|
| README.md | 8 KB | Documentation |
| PROJECT_SUMMARY.md | 10 KB | Documentation |
| QUICK_REFERENCE.md | 6 KB | Documentation |
| SETUP_GUIDE.md | 10 KB | Documentation |
| tracking/items.json | 4 KB | Data (grows with items) |
| data/brand_retailer_matrix.json | 13 KB | Data |
| scripts/monitor_inventory.py | 10 KB | Code |
| templates/new_item_template.json | 4 KB | Template |

**Total:** ~60 KB of pure value

---

## Backup & Maintenance

### What to Backup

- ✅ tracking/items.json (your price history)
- ✅ tracking/screenshots/ (your deal screenshots)
- ✅ tracking/purchases/ (your receipts)

### What's Auto-Recoverable

- ❌ logs/ (regenerate by running script)
- ❌ tracking/snapshots/ (regenerate by running script)
- ❌ Everything else (clone from GitHub)

### Git Workflow

```bash
# Push updates to GitHub
git add .
git commit -m "Update: Prices as of DATE, found deal on RETAILER"
git push origin main

# Pull latest from others
git pull origin main
```

---

## File Relationships

```
QUICK_REFERENCE.md (Your Daily Guide)
↑
└─── tracking/items.json (Your Data)
        ↑
        └─── Templates/new_item_template.json (How to add items)
        └─── data/brand_retailer_matrix.json (Where to buy)
                    ↑
                    └─── Browser bookmarks + email alerts

SETUP_GUIDE.md (Your Workflow)
↑
└─── scripts/monitor_inventory.py (Automation)
        ↑
        └─── Python requirements.txt (Dependencies)

README.md (Your Reference)
↑
└─── PROJECT_SUMMARY.md (Your Context)
```

---

## Next Action

**Right now:**

1. Read PROJECT_SUMMARY.md
2. Read QUICK_REFERENCE.md
3. Bookmark tracking/items.json in your editor (you'll update daily)

**Today:**

4. Follow SETUP_GUIDE.md section 1 (30 min setup)
5. Run first daily check (15 min)
6. Update tracking/items.json with prices

---

**All set! The framework is ready to hunt deals.** 🐍❄️
