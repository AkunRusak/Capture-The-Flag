# ============================================
# BASIC WEB SCRAPER
# ============================================
import requests
from urllib.parse import urljoin, urlparse
import re

def extract_links(url):
    try:
        response = requests.get(url, timeout=5)
        content = response.text
        
        # Extract links using regex
        links = re.findall(r'href=[\'"]?([^\'" >]+)', content)
        
        absolute_links = []
        for link in links:
            absolute_url = urljoin(url, link)
            absolute_links.append(absolute_url)
        
        return list(set(absolute_links))
        
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return []

def extract_forms(url):
    try:
        response = requests.get(url, timeout=5)
        content = response.text
        
        # Basic form extraction
        forms = re.findall(r'<form[^>]*>(.*?)</form>', content, re.DOTALL | re.IGNORECASE)
        
        form_data = []
        for form in forms:
            inputs = re.findall(r'<input[^>]*>', form, re.IGNORECASE)
            form_data.append({
                'form_html': form[:200] + '...' if len(form) > 200 else form,
                'inputs': inputs
            })
        
        return form_data
        
    except Exception as e:
        print(f"Error extracting forms from {url}: {str(e)}")
        return []

# Usage
# links = extract_links("http://example.com")
# print(f"Found {len(links)} links")
# forms = extract_forms("http://example.com")
# print(f"Found {len(forms)} forms")