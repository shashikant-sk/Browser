import os
import threading
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
BUILD_NAME = os.getenv("BROWSERSTACK_BUILD_NAME", "El_Pais_Cross_Browser_Test")
PROJECT_NAME = os.getenv("BROWSERSTACK_PROJECT_NAME", "Technical_Assignment_BrowserStack")

if not USERNAME or not ACCESS_KEY:
    raise Exception("Missing BrowserStack credentials in .env file")

BS_URL = f"http://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"
TARGET = "https://elpais.com/opinion/"

# Global results tracking
test_results = []
results_lock = threading.Lock()

# Enhanced capabilities setup with better configuration
caps_list = [
    ("Chrome-Win11", ChromeOptions(), {
        "bstack:options": {
            "os": "Windows", 
            "osVersion": "11", 
            "sessionName": "Chrome-Win11-ElPais-Test",
            "buildName": BUILD_NAME,
            "projectName": PROJECT_NAME,
            "seleniumVersion": "4.0.0",
            "debug": True,
            "networkLogs": True
        }
    }),
    ("Safari-MacOS", SafariOptions(), {
        "bstack:options": {
            "os": "OS X", 
            "osVersion": "Big Sur", 
            "browserVersion": "14.1",
            "sessionName": "Safari-MacOS-ElPais-Test",
            "buildName": BUILD_NAME,
            "projectName": PROJECT_NAME,
            "seleniumVersion": "3.141.59",
            "debug": True,
            "networkLogs": True
        }
    }),
    ("Firefox-Win10", FirefoxOptions(), {
        "bstack:options": {
            "os": "Windows", 
            "osVersion": "10", 
            "sessionName": "Firefox-Win10-ElPais-Test",
            "buildName": BUILD_NAME,
            "projectName": PROJECT_NAME,
            "seleniumVersion": "4.0.0",
            "debug": True,
            "networkLogs": True
        }
    }),
    ("Mobile-GalaxyS22", ChromeOptions(), {
        "bstack:options": {
            "deviceName": "Samsung Galaxy S22", 
            "osVersion": "12.0", 
            "realMobile": "true", 
            "sessionName": "GalaxyS22-ElPais-Test",
            "buildName": BUILD_NAME,
            "projectName": PROJECT_NAME,
            "debug": True,
            "networkLogs": True
        }
    }),
    ("Mobile-iPhone13", ChromeOptions(), {
        "bstack:options": {
            "deviceName": "iPhone 13", 
            "osVersion": "15", 
            "realMobile": "true", 
            "sessionName": "iPhone13-ElPais-Test",
            "buildName": BUILD_NAME,
            "projectName": PROJECT_NAME,
            "debug": True,
            "networkLogs": True
        }
    })
]

# Enhanced test function with better error handling and validation
def run_test(name, opts, extra_bstack):
    driver = None
    session_id = None
    start_time = time.time()
    
    try:
        print(f"[{name}] Starting test...")
        
        # Setup BrowserStack capabilities
        extra_bstack["bstack:options"].update({
            "userName": USERNAME, 
            "accessKey": ACCESS_KEY
        })
        opts.set_capability("bstack:options", extra_bstack["bstack:options"])
        
        # Set browser name for desktop browsers
        if "deviceName" in extra_bstack["bstack:options"]:
            opts.set_capability("browserName", "Chrome")  # Mobile devices use Chrome
        else:
            browser_name = name.split("-")[0]
            opts.set_capability("browserName", browser_name)
        
        # Create driver with extended timeout
        driver = webdriver.Remote(command_executor=BS_URL, options=opts)
        session_id = driver.session_id
        driver.implicitly_wait(15)  # Increased timeout
        
        print(f"[{name}] Session started: {session_id}")
        
        # Navigate to target page with retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                driver.get(TARGET)
                
                # Wait for page to load completely
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.TAG_NAME, "article"))
                )
                break
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"[{name}] Retry {attempt + 1} - Navigation failed: {e}")
                time.sleep(2)
        
        # Verify page loaded correctly
        title = driver.title
        if "EL PAÍS" not in title and "Opinión" not in title:
            raise Exception(f"Unexpected page title: {title}")
        
        # Find articles with explicit wait
        articles = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "article"))
        )
        
        # Additional validation - check for Spanish content
        page_source = driver.page_source.lower()
        spanish_indicators = ["opinión", "artículo", "español", "país"]
        spanish_found = any(indicator in page_source for indicator in spanish_indicators)
        
        if not spanish_found:
            print(f"[{name}] Warning: Spanish content indicators not found")
        
        # Verify minimum article count
        min_articles = 5
        if len(articles) < min_articles:
            raise Exception(f"Insufficient articles found: {len(articles)} < {min_articles}")
        
        # Mark test as passed in BrowserStack
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Test completed successfully"}}')
        
        execution_time = time.time() - start_time
        result = {
            "browser": name,
            "status": "PASSED",
            "title": title,
            "articles_found": len(articles),
            "execution_time": f"{execution_time:.2f}s",
            "session_id": session_id,
            "spanish_content": spanish_found
        }
        
        with results_lock:
            test_results.append(result)
        
        print(f"[{name}] [PASSED] Title: '{title}' - Found {len(articles)} articles - Time: {execution_time:.2f}s")
        
    except Exception as e:
        execution_time = time.time() - start_time
        error_msg = str(e)
        
        # Mark test as failed in BrowserStack
        if driver:
            try:
                driver.execute_script(f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"failed", "reason": "{error_msg}"}}}}')
            except:
                pass
        
        result = {
            "browser": name,
            "status": "FAILED",
            "error": error_msg,
            "execution_time": f"{execution_time:.2f}s",
            "session_id": session_id
        }
        
        with results_lock:
            test_results.append(result)
        
        print(f"[{name}] [FAILED] Error: {error_msg} - Time: {execution_time:.2f}s")
        
    finally:
        if driver:
            try:
                driver.quit()
                print(f"[{name}] Browser session closed.")
            except Exception as e:
                print(f"[{name}] Error closing session: {e}")

# Enhanced main execution with comprehensive reporting
def main():
    print("=" * 80)
    print("BrowserStack Cross-Browser Testing - El País Opinion Section")
    print("=" * 80)
    print(f"Target URL: {TARGET}")
    print(f"Build Name: {BUILD_NAME}")
    print(f"Project: {PROJECT_NAME}")
    print(f"BrowserStack User: {USERNAME}")
    print("\nBrowser configurations:")
    for name, _, extra in caps_list:
        if "deviceName" in extra["bstack:options"]:
            device = extra["bstack:options"]["deviceName"]
            os_ver = extra["bstack:options"]["osVersion"]
            print(f"  [MOBILE] {name}: {device} (OS {os_ver})")
        else:
            browser = name.split("-")[0]
            os_name = extra["bstack:options"]["os"]
            os_ver = extra["bstack:options"]["osVersion"]
            print(f"  [DESKTOP] {name}: {browser} on {os_name} {os_ver}")
    print("\n" + "=" * 80)
    
    threads = []
    start_time = time.time()
    
    # Execute tests in parallel
    for name, opts, extra in caps_list:
        t = threading.Thread(target=run_test, args=(name, opts, extra))
        threads.append(t)
        t.start()
        time.sleep(1)  # Stagger thread starts slightly
    
    # Wait for all tests to complete
    for t in threads:
        t.join()
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Generate comprehensive report
    print("\n" + "=" * 80)
    print("TEST EXECUTION SUMMARY")
    print("=" * 80)
    
    passed_tests = [r for r in test_results if r["status"] == "PASSED"]
    failed_tests = [r for r in test_results if r["status"] == "FAILED"]
    
    print(f"Total Tests: {len(test_results)}")
    print(f"Passed: {len(passed_tests)}")
    print(f"Failed: {len(failed_tests)}")
    print(f"Total Execution Time: {total_time:.2f} seconds")
    print(f"Success Rate: {(len(passed_tests)/len(test_results)*100):.1f}%")
    
    if passed_tests:
        print(f"\nPASSED TESTS ({len(passed_tests)}):")
        for result in passed_tests:
            spanish_indicator = "[ES]" if result.get("spanish_content", False) else "[WARNING]"
            print(f"   {spanish_indicator} {result['browser']}: {result['articles_found']} articles ({result['execution_time']})")
            print(f"      Session: {result['session_id']}")
    
    if failed_tests:
        print(f"\nFAILED TESTS ({len(failed_tests)}):")
        for result in failed_tests:
            print(f"   [FAIL] {result['browser']}: {result['error']} ({result['execution_time']})")
            if result.get('session_id'):
                print(f"      Session: {result['session_id']}")
    
    # Save results to JSON file for later analysis
    results_file = "browserstack_test_results.json"
    try:
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump({
                "summary": {
                    "total_tests": len(test_results),
                    "passed": len(passed_tests),
                    "failed": len(failed_tests),
                    "success_rate": (len(passed_tests)/len(test_results)*100),
                    "total_time": total_time,
                    "build_name": BUILD_NAME,
                    "project_name": PROJECT_NAME,
                    "target_url": TARGET
                },
                "results": test_results
            }, f, indent=2)
        print(f"\nDetailed results saved to: {results_file}")
    except Exception as e:
        print(f"\nFailed to save results file: {e}")
    
    print("\n" + "=" * 80)
    
    return len(failed_tests) == 0  # Return True if all tests passed

if __name__ == "__main__":
    success = main()
    if success:
        print("All BrowserStack tests completed successfully!")
        exit(0)
    else:
        print("Some BrowserStack tests failed!")
        exit(1)
