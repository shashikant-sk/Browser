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
    title_tag = article.find('h2') or article.find('h1')
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
        img_tag = article_page.find('img')
        if img_tag and img_tag.get("src"):
            img_url = img_tag["src"]
            img_data = requests.get(img_url, timeout=10).content
            image_path = os.path.join(article_dir, "cover.jpg")
            with open(image_path, 'wb') as f:
                f.write(img_data)
            print(f"🖼️ Image saved: {image_path}\n")
    except Exception as e:
        print(f"❌ Error saving image: {e}")

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

# Repeated word analysis
print("\n🔎 Analyzing Repeated Words...\n")
all_words = []

for title in translated_titles:
    words = re.findall(r'\b\w+\b', title.lower())
    all_words.extend(words)

word_counts = Counter(all_words)


for word, count in word_counts.items():
    if count > 2:
        print(f"🔁 '{word}' appears {count} times")




# ==========================================================================================================
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from bs4 import BeautifulSoup
# # from webdriver_manager.chrome import ChromeDriverManager

# # # Use Service object as required by latest Selenium
# # service = Service(ChromeDriverManager().install())
# # driver = webdriver.Chrome(service=service)

# # driver.get('https://elpais.com/opinion/')

# # # Sanity check
# # print(driver.title)

# --------------------------------------------------------------------------------------------


# # driver.quit()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# import requests
# import os
# import time

# # Setup Selenium
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# # Go to El País - Opinion Section
# driver.get('https://elpais.com/opinion/')
# time.sleep(3)  # Let page load

# # Extract HTML and parse with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # Select first 5 articles
# articles = soup.select('article')[:5]

# # Prepare folder for images
# os.makedirs("images", exist_ok=True)

# # Store original titles
# original_titles = []

# for idx, article in enumerate(articles, start=1):
#     # Get article title
#     title_tag = article.find('h2') or article.find('h1')
#     if not title_tag:
#         continue

#     title = title_tag.get_text().strip()
#     original_titles.append(title)
#     print(f"\n📌 Article {idx} Title (Spanish): {title}")

#     # Get article URL
#     link_tag = article.find('a')
#     if not link_tag or not link_tag.get('href'):
#         continue

#     article_url = link_tag['href']
#     if not article_url.startswith("http"):
#         article_url = "https://elpais.com" + article_url

#     # Scrape full article content
#     article_res = requests.get(article_url)
#     article_soup = BeautifulSoup(article_res.text, 'html.parser')
#     paragraphs = article_soup.select('p')

#     content = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())
#     print(f"📝 Content Snippet:\n{content[:300]}...\n")

#     # Download image if available
#     img_tag = article_soup.find('img')
#     if img_tag and img_tag.get("src"):
#         img_url = img_tag["src"]
#         try:
#             img_data = requests.get(img_url).content
#             with open(f"images/cover_image_{idx}.jpg", 'wb') as f:
#                 f.write(img_data)
#             print(f"🖼️ Cover Image saved: images/cover_image_{idx}.jpg")
#         except Exception as e:
#             print(f"❌ Error downloading image: {e}")

# driver.quit()

# # Save titles for next step (translation)
# with open("original_titles.txt", "w", encoding="utf-8") as f:
#     for title in original_titles:
#         f.write(title + "\n")
