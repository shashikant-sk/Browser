# BrowserStack Test Configuration
# This file contains all the settings for your cross-browser tests

import os
from dotenv import load_dotenv

load_dotenv()

# BrowserStack Configuration
BROWSERSTACK_CONFIG = {
    "username": os.getenv("BROWSERSTACK_USERNAME"),
    "access_key": os.getenv("BROWSERSTACK_ACCESS_KEY"),
    "build_name": os.getenv("BROWSERSTACK_BUILD_NAME", "El_Pais_Cross_Browser_Test"),
    "project_name": os.getenv("BROWSERSTACK_PROJECT_NAME", "Technical_Assignment_BrowserStack"),
    "hub_url": "hub-cloud.browserstack.com/wd/hub"
}

# Test Configuration
TEST_CONFIG = {
    "target_url": "https://elpais.com/opinion/",
    "min_articles": 5,
    "page_load_timeout": 20,
    "implicit_wait": 15,
    "max_retries": 3,
    "spanish_indicators": ["opinión", "artículo", "español", "país"],
    "expected_title_keywords": ["EL PAÍS", "Opinión"]
}

# Browser Capabilities
BROWSER_CAPABILITIES = [
    {
        "name": "Chrome-Win11",
        "browserName": "Chrome",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11",
            "browserVersion": "latest",
            "sessionName": "Chrome-Win11-ElPais-Test",
            "seleniumVersion": "4.0.0",
            "debug": True,
            "networkLogs": True,
            "consoleLogs": "info"
        }
    },
    {
        "name": "Safari-MacOS", 
        "browserName": "Safari",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Monterey", 
            "browserVersion": "latest",
            "sessionName": "Safari-MacOS-ElPais-Test",
            "seleniumVersion": "4.0.0",
            "debug": True,
            "networkLogs": True,
            "consoleLogs": "info"
        }
    },
    {
        "name": "Firefox-Win10",
        "browserName": "Firefox", 
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "browserVersion": "latest", 
            "sessionName": "Firefox-Win10-ElPais-Test",
            "seleniumVersion": "4.0.0",
            "debug": True,
            "networkLogs": True,
            "consoleLogs": "info"
        }
    },
    {
        "name": "Mobile-GalaxyS22",
        "browserName": "Chrome",
        "bstack:options": {
            "deviceName": "Samsung Galaxy S22",
            "osVersion": "12.0",
            "realMobile": "true",
            "sessionName": "GalaxyS22-ElPais-Test", 
            "debug": True,
            "networkLogs": True,
            "consoleLogs": "info"
        }
    },
    {
        "name": "Mobile-iPhone13",
        "browserName": "Chrome", 
        "bstack:options": {
            "deviceName": "iPhone 13",
            "osVersion": "15",
            "realMobile": "true",
            "sessionName": "iPhone13-ElPais-Test",
            "debug": True,
            "networkLogs": True,
            "consoleLogs": "info"
        }
    }
]

def validate_config():
    """Validate that all required configuration is present"""
    if not BROWSERSTACK_CONFIG["username"] or not BROWSERSTACK_CONFIG["access_key"]:
        raise Exception("BrowserStack credentials not found in .env file")
    
    print("✅ Configuration validated successfully")
    return True
