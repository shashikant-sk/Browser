from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from deep_translator import GoogleTranslator
import requests
import os
import re
import time
from collections import Counter

# Setup Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Go to El País - Opinion Section
driver.get('https://elpais.com/opinion/')
time.sleep(3)

# Extract and parse the HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
articles = soup.select('article')[:5]

# Prepare main output folder
base_dir = "articles_data"
os.makedirs(base_dir, exist_ok=True)

# Track all titles
original_titles = []
translated_titles = []

print("\n📄 Scraping Articles...\n")

for idx, article in enumerate(articles, start=1):
    # Extract title
    title_tag = article.find('h1') or article.find('h2')
    if not title_tag:
        continue

    title = title_tag.get_text().strip()
    original_titles.append(title)
    print(f"📌 Article {idx} Title (Spanish): {title}")

    # Make a folder for each article
    article_dir = os.path.join(base_dir, f"article_{idx}")
    os.makedirs(article_dir, exist_ok=True)

    # Save title to a text file
    with open(os.path.join(article_dir, "title_es.txt"), "w", encoding="utf-8") as f:
        f.write(title)

    # Get article URL
    link_tag = article.find('a')
    if not link_tag or not link_tag.get('href'):
        continue

    article_url = link_tag['href']
    if not article_url.startswith("http"):
        article_url = "https://elpais.com" + article_url

    try:
        driver.get(article_url)
        time.sleep(3)
        article_page = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract content
        content_paragraphs = article_page.select(
            'div.a_c div.a_m-p > p, div.a_c article > p, div#fusion-app p, p.c_d'
        )
        content = "\n".join(p.get_text().strip() for p in content_paragraphs if p.get_text().strip())

        if content:
            print(f"📝 Content Snippet:\n{content[:300]}...\n")
        else:
            print("⚠️ No content found.\n")

        # Save content to file
        with open(os.path.join(article_dir, "content_es.txt"), "w", encoding="utf-8") as f:
            f.write(content)

    except Exception as e:
        print(f"❌ Error fetching content: {e}")

    # Download cover image if available
    try:
        # Try multiple selectors for images in El País articles
        img_selectors = [
            'figure.a_m-media img',  # Main article image
            'div.a_m-media img',     # Alternative media container
            'img.a_m-media__img',    # Direct image class
            'figure img',            # Generic figure image
            'div.c_m img',           # Content module image
            'img[src*="elpais"]'     # Any El País hosted image
        ]
        
        img_tag = None
        for selector in img_selectors:
            img_tag = article_page.select_one(selector)
            if img_tag and img_tag.get("src"):
                break
        
        if img_tag and img_tag.get("src"):
            img_url = img_tag["src"]
            
            # Handle relative URLs
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            elif img_url.startswith("/"):
                img_url = "https://elpais.com" + img_url
            
            # Add headers to mimic a real browser request
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Referer': article_url,
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
            }
            
            print(f"🖼️ Attempting to download image from: {img_url}")
            
            img_response = requests.get(img_url, headers=headers, timeout=15)
            img_response.raise_for_status()  # Raise an exception for bad status codes
            
            # Determine file extension from URL or content type
            if img_url.lower().endswith(('.jpg', '.jpeg')):
                ext = '.jpg'
            elif img_url.lower().endswith('.png'):
                ext = '.png'
            elif img_url.lower().endswith('.webp'):
                ext = '.webp'
            else:
                # Try to get from content type
                content_type = img_response.headers.get('content-type', '')
                if 'jpeg' in content_type or 'jpg' in content_type:
                    ext = '.jpg'
                elif 'png' in content_type:
                    ext = '.png'
                elif 'webp' in content_type:
                    ext = '.webp'
                else:
                    ext = '.jpg'  # Default fallback
            
            image_path = os.path.join(article_dir, f"cover{ext}")
            
            with open(image_path, 'wb') as f:
                f.write(img_response.content)
            
            print(f"✅ Image saved successfully: {image_path}")
            
        else:
            print("⚠️ No suitable image found for this article")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error downloading image: {e}")
    except Exception as e:
        print(f"❌ Error saving image: {e}")
    
    print("─" * 50)  # Separator between articles

# Hold browser open until user presses Enter
input("\n✅ Done scraping. Press Enter to close the browser...")
driver.quit()

# Save all Spanish titles
with open(os.path.join(base_dir, "original_titles.txt"), "w", encoding="utf-8") as f:
    for title in original_titles:
        f.write(title + "\n")

# Translate titles
print("\n🌐 Translating Titles...\n")

for idx, title in enumerate(original_titles, start=1):
    try:
        translated = GoogleTranslator(source='es', target='en').translate(title)
        translated_titles.append(translated)
        print(f"📝 Title {idx} Translated: {translated}")

        # Save translated title to corresponding article folder
        article_dir = os.path.join(base_dir, f"article_{idx}")
        with open(os.path.join(article_dir, "title_en.txt"), "w", encoding="utf-8") as f:
            f.write(translated)
    except Exception as e:
        print(f"❌ Error translating title {idx}: {e}")

# Save all translated titles
with open(os.path.join(base_dir, "translated_titles.txt"), "w", encoding="utf-8") as f:
    for title in translated_titles:
        f.write(title + "\n")

# Repeated word analysis
print("\n🔎 Analyzing Repeated Words...\n")
all_words = []

for title in translated_titles:
    words = re.findall(r'\b\w+\b', title.lower())
    all_words.extend(words)

word_counts = Counter(all_words)

# Show words that appear more than two
repeated_words = {word: count for word, count in word_counts.items() if count > 2}

if repeated_words:
    print("🔁 Words appearing more than once:")
    for word, count in sorted(repeated_words.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{word}' appears {count} times")
else:
    print("📝 No repeated words found in titles")

print(f"\n📊 Total words analyzed: {len(all_words)}")
print(f"📊 Unique words: {len(word_counts)}")
print(f"📊 Articles processed: {len(original_titles)}")

print("\n🎉 Script completed successfully!")
