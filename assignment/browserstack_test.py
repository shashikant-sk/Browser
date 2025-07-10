import os
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from dotenv import load_dotenv

# Load credentials
load_dotenv()
USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
if not USERNAME or not ACCESS_KEY:
    raise Exception("Missing credentials in .env")

BS_URL = f"http://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"
TARGET = "https://elpais.com/opinion/"

# Capabilities setup
caps_list = [
    ("Chrome-Win11", ChromeOptions(), {
        "bstack:options": {"os": "Windows", "osVersion": "11", "sessionName": "Chrome-Win11"}
    }),
    ("Safari-MacOS", SafariOptions(), {
        "bstack:options": {"os": "OS X", "osVersion": "Monterey", "sessionName": "Safari-MacOS"}
    }),
    ("Firefox-Win10", FirefoxOptions(), {
        "bstack:options": {"os": "Windows", "osVersion": "10", "sessionName": "Firefox-Win10"}
    }),
    ("Mobile-GalaxyS22", ChromeOptions(), {
        "bstack:options": {"deviceName": "Samsung Galaxy S22", "osVersion": "12.0", "realMobile": "true", "sessionName": "GalaxyS22"}
    }),
    ("Mobile-iPhone13", ChromeOptions(), {
        "bstack:options": {"deviceName": "iPhone 13", "osVersion": "15", "realMobile": "true", "sessionName": "iPhone13"}
    })
]

# Function to run test
def run_test(name, opts, extra_bstack):
    driver = None
    try:
        print(f"[{name}] Starting test...")
        
        # Insert BrowserStack account into bstack:options
        extra_bstack["bstack:options"].update({
            "userName": USERNAME, "accessKey": ACCESS_KEY
        })
        opts.set_capability("bstack:options", extra_bstack["bstack:options"])
        
        if "deviceName" in extra_bstack["bstack:options"]:
            opts.set_capability("browserName", extra_bstack["bstack:options"].get("browserName", "Chrome"))
        else:
            opts.set_capability("browserName", name.split("-")[0])
        
        # Create driver with timeout
        driver = webdriver.Remote(command_executor=BS_URL, options=opts)
        driver.implicitly_wait(10)
        
        # Navigate and test
        driver.get(TARGET)
        time.sleep(3)
        
        title = driver.title
        articles = driver.find_elements(By.TAG_NAME, "article")
        
        print(f"[{name}] [OK] Title: {title} - Found {len(articles)} articles.")
        
        # Verify we found articles
        if len(articles) == 0:
            print(f"[{name}] Warning: No articles found!")
        
    except Exception as e:
        print(f"[{name}] [FAIL] Test failed: {str(e)}")
        
    finally:
        if driver:
            try:
                driver.quit()
                print(f"[{name}] Browser session closed.")
            except:
                pass

# Execute all tests in parallel
print("Starting BrowserStack cross-browser testing across 5 parallel threads...")
print(f"Testing URL: {TARGET}")
print("Browser configurations:")
for name, _, _ in caps_list:
    print(f"  - {name}")
print()

threads = []
start_time = time.time()

for name, opts, extra in caps_list:
    t = threading.Thread(target=run_test, args=(name, opts, extra))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"\nAll tests completed in {end_time - start_time:.2f} seconds")
