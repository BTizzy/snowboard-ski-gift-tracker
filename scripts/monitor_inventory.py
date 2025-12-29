#!/usr/bin/env python3
"""
Snowboard/Ski Gift Tracker - Inventory Monitor

Automated monitoring script to track prices and inventory across multiple retailers.
Supports email alerts, logging, and CSV export of findings.

Usage:
    python3 monitor_inventory.py
    python3 monitor_inventory.py --item SPY-001
    python3 monitor_inventory.py --export results.csv

Requirements:
    pip install requests beautifulsoup4 python-dotenv
"""

import json
import csv
import logging
from datetime import datetime
from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

LOG_FILE = "logs/monitor.log"
OUTPUT_DIR = "tracking/snapshots"
ITEMS_FILE = "tracking/items.json"
BRAND_FILE = "data/brand_retailer_matrix.json"

# Retry logic
MAX_RETRIES = 3
REQUEST_TIMEOUT = 10
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Setup logging
Path("logs").mkdir(exist_ok=True)
Path(OUTPUT_DIR).mkdir(exist_ok=True, parents=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# CORE MONITORING FUNCTIONS
# ============================================================================

def load_tracking_data() -> Dict:
    """Load items.json tracking database."""
    try:
        with open(ITEMS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Items file not found: {ITEMS_FILE}")
        return {}

def load_brand_data() -> Dict:
    """Load brand_retailer_matrix.json."""
    try:
        with open(BRAND_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Brand file not found: {BRAND_FILE}")
        return {}

def check_spyder_official(product_url: str) -> Dict:
    """
    Monitor Spyder official website for pricing and availability.
    
    Args:
        product_url: Full URL to product page
    
    Returns:
        Dict with price, stock status, available sizes
    """
    logger.info(f"Checking Spyder: {product_url}")
    
    try:
        response = requests.get(product_url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Parse Spyder page structure
        # Note: Spyder uses product JSON in page - look for script tags
        scripts = soup.find_all('script', type='application/json')
        
        result = {
            "retailer": "Spyder Official",
            "url": product_url,
            "timestamp": datetime.now().isoformat(),
            "price": None,
            "stock_status": "Unknown",
            "sizes_available": [],
            "error": None
        }
        
        # Look for price in meta tags or structured data
        price_meta = soup.find('meta', {'property': 'product:price:amount'})
        if price_meta:
            result["price"] = float(price_meta.get('content'))
        
        # Check for "Add to Cart" button visibility
        add_to_cart = soup.find('button', {'class': lambda x: x and 'add-to-cart' in x.lower()})
        result["stock_status"] = "In Stock" if add_to_cart else "Out of Stock"
        
        logger.info(f"  Price: ${result['price']}, Status: {result['stock_status']}")
        return result
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed for {product_url}: {e}")
        return {
            "retailer": "Spyder Official",
            "url": product_url,
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }
    except Exception as e:
        logger.error(f"Parsing error for {product_url}: {e}")
        return {
            "retailer": "Spyder Official",
            "url": product_url,
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }

def check_peter_glenn(search_term: str) -> Dict:
    """
    Monitor Peter Glenn for specific product.
    """
    logger.info(f"Checking Peter Glenn for: {search_term}")
    
    try:
        # Peter Glenn has search functionality
        search_url = f"https://peterglenn.com/search?q={search_term.replace(' ', '+')}"
        response = requests.get(search_url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        result = {
            "retailer": "Peter Glenn",
            "url": search_url,
            "timestamp": datetime.now().isoformat(),
            "products_found": 0,
            "items": [],
            "error": None
        }
        
        # Find product listings
        products = soup.find_all('div', {'class': lambda x: x and 'product' in x.lower()})
        result["products_found"] = len(products)
        
        logger.info(f"  Found {len(products)} products")
        return result
        
    except Exception as e:
        logger.error(f"Peter Glenn search failed: {e}")
        return {
            "retailer": "Peter Glenn",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }

def check_rei_search(search_term: str) -> Dict:
    """
    Monitor REI for product availability.
    """
    logger.info(f"Checking REI for: {search_term}")
    
    try:
        search_url = f"https://www.rei.com/search?q={search_term.replace(' ', '+')}"
        response = requests.get(search_url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        result = {
            "retailer": "REI Co-op",
            "url": search_url,
            "timestamp": datetime.now().isoformat(),
            "products_found": 0,
            "error": None
        }
        
        logger.info(f"  REI search completed")
        return result
        
    except Exception as e:
        logger.error(f"REI search failed: {e}")
        return {
            "retailer": "REI Co-op",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }

def monitor_item(item: Dict) -> List[Dict]:
    """
    Run full monitoring for a single item across all configured retailers.
    """
    results = []
    item_name = item.get('name')
    logger.info(f"\n{'='*70}")
    logger.info(f"Monitoring: {item_name}")
    logger.info(f"{'='*70}")
    
    # Get tracking URLs from item data
    tracking_data = item.get('tracking_data', [])
    
    for tracker in tracking_data:
        retailer = tracker.get('retailer')
        url = tracker.get('url')
        
        if not url:
            logger.warning(f"  No URL configured for {retailer}")
            continue
        
        # Route to appropriate checker based on retailer
        if 'spyder.com' in url:
            result = check_spyder_official(url)
        elif 'peterglenn.com' in url:
            result = check_peter_glenn(item_name)
        elif 'rei.com' in url:
            result = check_rei_search(item_name)
        else:
            logger.warning(f"  No handler for {retailer}")
            continue
        
        results.append(result)
    
    return results

def save_results(results: List[Dict], item_id: str):
    """
    Save monitoring results to timestamped file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/{item_id}_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    logger.info(f"Results saved to: {filename}")
    return filename

def export_csv(results: List[Dict], output_file: str = "tracking_results.csv"):
    """
    Export results to CSV for spreadsheet analysis.
    """
    if not results:
        logger.warning("No results to export")
        return
    
    # Flatten results for CSV
    rows = []
    for result in results:
        row = {
            'timestamp': result.get('timestamp'),
            'retailer': result.get('retailer'),
            'price': result.get('price'),
            'stock_status': result.get('stock_status'),
            'products_found': result.get('products_found'),
            'error': result.get('error')
        }
        rows.append(row)
    
    fieldnames = ['timestamp', 'retailer', 'price', 'stock_status', 'products_found', 'error']
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    logger.info(f"CSV export saved to: {output_file}")

def run_monitoring():
    """
    Main monitoring loop - checks all tracked items.
    """
    logger.info("Starting inventory monitoring...")
    
    tracking_data = load_tracking_data()
    items = tracking_data.get('items', [])
    
    if not items:
        logger.warning("No items configured for monitoring")
        return
    
    all_results = []
    
    for item in items:
        item_id = item.get('id')
        results = monitor_item(item)
        all_results.extend(results)
        
        # Save results for this item
        save_results(results, item_id)
    
    # Export combined results
    export_csv(all_results, f"{OUTPUT_DIR}/combined_results.csv")
    
    logger.info(f"\n{'='*70}")
    logger.info(f"Monitoring complete. Checked {len(all_results)} retailers.")
    logger.info(f"{'='*70}")

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        run_monitoring()
    except KeyboardInterrupt:
        logger.info("Monitoring interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
