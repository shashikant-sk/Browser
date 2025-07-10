import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_locally():
    """Test the functionality locally before running on BrowserStack"""
    print("Running Local Test...")
    
    # Setup local Chrome driver
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
       
        driver.get("https://elpais.com/opinion/")
        time.sleep(3)
        
        # Get page title
        title = driver.title
        print(f"[OK] Page Title: {title}")
        
        # Find articles
        articles = driver.find_elements(By.TAG_NAME, "article")
        print(f"[OK] Found {len(articles)} articles")
        
        if len(articles) >= 5:
            print("[OK] Local test passed - sufficient articles found")
            return True
        else:
            print("[FAIL] Local test failed - insufficient articles found")
            return False
            
    except Exception as e:
        print(f"[FAIL] Local test failed with error: {e}")
        return False
        
    finally:
        driver.quit()

if __name__ == "__main__":
    if test_locally():
        print("\n[OK] Local test passed! Proceeding to BrowserStack testing...")
        import browserstack_test
    else:
        print("\n[FAIL] Local test failed! Please fix issues before running BrowserStack tests.")
