import requests
from typing import Dict, Any


def scrape_with_brightdata(url: str, zone_name: str, password: str) -> Dict[str, Any]:
    """Scrape URL using Bright Data proxy"""
    proxy_host = "brd.superproxy.io"
    proxy_port = 33335
    customer_id = "hl_b044aca4"
    
    proxy_user = f"brd-customer-{customer_id}-zone-{zone_name}"
    proxies = {
        "http": f"http://{proxy_user}:{password}@{proxy_host}:{proxy_port}",
        "https": f"http://{proxy_user}:{password}@{proxy_host}:{proxy_port}",
    }
    
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        return {
            "success": True,
            "status_code": response.status_code,
            "content": response.text,
            "url": url
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "url": url
        }
