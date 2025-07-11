import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_locally():
    """Test the functionality locally before running on BrowserStack"""
    print("=" * 60)
    print("LOCAL VALIDATION TEST - El País Opinion Section")
    print("=" * 60)
    
    # Setup local Chrome driver
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        print("[INFO] Navigating to El País Opinion section...")
        driver.get("https://elpais.com/opinion/")
        
        # Wait for page to load completely
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
        
        # Get page title and validate
        title = driver.title
        print(f"[OK] Page Title: {title}")
        
        # Validate this is the correct page
        if "EL PAÍS" not in title and "Opinión" not in title:
            print(f"[WARNING] Unexpected page title: {title}")
            return False
        
        # Find articles
        articles = driver.find_elements(By.TAG_NAME, "article")
        print(f"[OK] Found {len(articles)} articles")
        
        # Check for Spanish content
        page_source = driver.page_source.lower()
        spanish_indicators = ["opinión", "artículo", "español", "país"]
        spanish_found = sum(1 for indicator in spanish_indicators if indicator in page_source)
        print(f"[OK] Spanish content indicators found: {spanish_found}/{len(spanish_indicators)}")
        
        # Validate minimum article count
        min_articles = 5
        if len(articles) >= min_articles:
            print(f"[OK] Sufficient articles found ({len(articles)} >= {min_articles})")
            
            # Additional validation - check article structure
            valid_articles = 0
            for i, article in enumerate(articles[:5]):
                try:
                    # Look for title elements
                    title_elements = article.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
                    if title_elements:
                        article_title = title_elements[0].text.strip()
                        if article_title:
                            valid_articles += 1
                            print(f"[OK] Article {i+1}: '{article_title[:50]}...'")
                        else:
                            print(f"[WARNING] Article {i+1}: Empty title")
                    else:
                        print(f"[WARNING] Article {i+1}: No title element found")
                except Exception as e:
                    print(f"[WARNING] Article {i+1}: Error - {e}")
            
            print(f"[OK] Valid articles with titles: {valid_articles}/{min(len(articles), 5)}")
            
            if valid_articles >= 3:  # At least 3 valid articles
                print("[PASSED] Local test validation successful!")
                return True
            else:
                print("[FAILED] Insufficient valid articles found")
                return False
        else:
            print(f"[FAILED] Insufficient articles found ({len(articles)} < {min_articles})")
            return False
            
    except Exception as e:
        print(f"[FAILED] Local test failed with error: {e}")
        return False
        
    finally:
        driver.quit()

if __name__ == "__main__":
    success = test_locally()
    if success:
        print("\n[PASSED] Local test validation completed successfully!")
        print("[INFO] Proceeding to BrowserStack testing...")
        
        # Import and run BrowserStack tests
        try:
            import browserstack_test
            browserstack_success = browserstack_test.main()
            if browserstack_success:
                print("\n[PASSED] All tests completed successfully!")
            else:
                print("\n[FAILED] Some BrowserStack tests failed!")
        except Exception as e:
            print(f"\n[FAILED] Error running BrowserStack tests: {e}")
    else:
        print("\n[FAILED] Local test validation failed!")
        print("[INFO] Please fix local issues before running BrowserStack tests.")
