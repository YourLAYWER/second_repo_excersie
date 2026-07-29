#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def scrape_local_info():
    # Target URL for local Gqeberha information
    url = "https://en.wikipedia.org/wiki/Gqeberha"
    
    # It's good practice to include a User-Agent header so the website doesn't block the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    
    try:
        # Fetch the web page
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # The main text content on Wikipedia is usually inside the 'mw-content-text' div
        content_div = soup.find(id="mw-content-text")
        
        if not content_div:
            print("Could not find the main content on the page.")
            return

        # Find all paragraph tags
        paragraphs = content_div.find_all('p')
        
        print("🌍 **Extracting Local Info: Gqeberha** 🌍\n")
        
        # Extract and print the first two non-empty paragraphs
        extracted_count = 0
        for p in paragraphs:
            text = p.get_text().strip()
            
            # Skip empty paragraphs or short coordinate data
            if len(text) > 50: 
                print(text)
                print("\n" + "-"*60 + "\n")
                extracted_count += 1
                
            # Stop after grabbing 2 substantial paragraphs
            if extracted_count >= 2:
                break
                
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")

if __name__ == "__main__":
    scrape_local_info()