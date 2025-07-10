# El País News Scraper with Cross-Browser Testing

A comprehensive web scraping and testing solution that extracts Spanish news articles from El País Opinion section, translates them to English, and validates functionality across multiple browsers using BrowserStack's cloud infrastructure.

## 🎯 Project Overview

This project automates the complete workflow of news article processing from El País (Spanish news outlet):

1. **Website Access** - Visits El País and ensures Spanish language content
2. **Article Scraping** - Extracts the first 5 articles from the Opinion section
3. **Content Processing** - Downloads article titles, content, and cover images
4. **Translation** - Converts Spanish titles to English using translation APIs
5. **Text Analysis** - Identifies frequently repeated words across translated headers
6. **Cross-Browser Testing** - Validates functionality on 5 different browser/device combinations

## 🎯 Complete Project Requirements

### 1. Website Verification
- ✅ Visit El País Spanish news website
- ✅ Confirm content is displayed in Spanish language
- ✅ Navigate to the Opinion section

### 2. Article Scraping  
- ✅ Extract first 5 articles from Opinion section
- ✅ Capture article titles in Spanish
- ✅ Save article content in Spanish
- ✅ Download and save cover images locally

### 3. Translation Service
- ✅ Translate Spanish article titles to English
- ✅ Use professional translation API (Google Translate/Rapid Translate)
- ✅ Display both original and translated headers

### 4. Text Analysis
- ✅ Analyze translated headers for word frequency
- ✅ Identify words repeated more than twice
- ✅ Count and display word occurrence statistics

### 5. Cross-Browser Testing
- ✅ Run solution locally first for validation
- ✅ Execute on BrowserStack with 5 parallel threads
- ✅ Test desktop and mobile browser combinations
- ✅ Use BrowserStack free trial account

## 🛠️ Step-by-Step Setup Guide

### Step 1: Verify Python Installation
Ensure you have Python 3.7 or higher:
```bash
python --version
```
*Expected output: Python 3.7.x or higher*

### Step 2: Install Required Dependencies

Install each package individually to understand what each does:

```bash
# Web automation and browser control
pip install selenium

# Web scraping and HTML parsing
pip install beautifulsoup4

# HTTP requests for web data
pip install requests

# Environment variables for secure credentials
pip install python-dotenv

# Automatic web driver management
pip install webdriver-manager

# Translation services
pip install deep-translator

# Or install everything at once
pip install -r requirements.txt
```

**Package Purposes:**
- **`selenium`** - Controls web browsers automatically for testing
- **`beautifulsoup4`** - Parses and extracts data from HTML pages
- **`requests`** - Makes HTTP requests to download web content
- **`python-dotenv`** - Manages sensitive credentials securely
- **`webdriver-manager`** - Automatically downloads browser drivers
- **`deep-translator`** - Provides free translation services

### Step 3: Set Up BrowserStack Account
1. **Create Account**: Visit [BrowserStack.com](https://www.browserstack.com/)
2. **Sign Up**: Register for a free trial account (no credit card required)
3. **Find Credentials**: 
   - Log into your BrowserStack dashboard
   - Go to "Account" → "Settings" 
   - Copy your Username and Access Key
4. **Create Environment File**: Create a `.env` file in the project folder:

```env
BROWSERSTACK_USERNAME=your_actual_username_here
BROWSERSTACK_ACCESS_KEY=your_actual_access_key_here
```

⚠️ **Important**: Replace the placeholder values with your actual BrowserStack credentials

### Step 4: Understand Project Structure

```
assignment/
├── run_tests.py          # 🎮 Main test orchestrator (START HERE)
├── local_test.py         # 🖥️  Local browser testing
├── browserstack_test.py  # ☁️  Cloud browser testing  
├── main.py              # 🔧 Core scraping functionality
├── requirements.txt     # 📦 Python dependencies list
├── .env                # 🔐 BrowserStack credentials (you create this)
└── articles_data/       # 📁 Scraped articles storage
    ├── original_titles.txt
    ├── article_1/
    │   ├── title_es.txt
    │   ├── title_en.txt
    │   ├── content_es.txt
    │   └── cover.jpg
    └── ... (more articles)
```

### Step 5: Run the Complete Solution
Execute the main workflow:
```bash
python run_tests.py
```

## 🖥️ Cross-Browser Testing Matrix

Our testing validates functionality across 5 configurations simultaneously:

| Browser | Operating System | Device Type | Screen Size | Purpose |
|---------|------------------|-------------|-------------|---------|
| Chrome 91+ | Windows 11 | Desktop | 1920x1080 | Modern desktop experience |
| Safari 14+ | macOS Monterey | Desktop | 1440x900 | Mac user experience |
| Firefox 89+ | Windows 10 | Desktop | 1920x1080 | Alternative browser testing |
| Samsung Internet | Galaxy S22 | Mobile | 375x812 | Android mobile experience |
| Safari Mobile | iPhone 13 | Mobile | 390x844 | iOS mobile experience |

## 🧪 What the System Tests

### Local Testing Phase:
1. **Python Dependencies** - Verifies all packages are installed
2. **Website Access** - Connects to El País Opinion section
3. **Page Loading** - Confirms page title loads correctly
4. **Article Detection** - Counts available articles (minimum 5 required)
5. **Spanish Content** - Validates content is in Spanish language

### Cross-Browser Testing Phase:
For each of the 5 browser configurations:
1. **Page Navigation** - Opens `https://elpais.com/opinion/`
2. **Title Verification** - Checks page title is "Opinión en EL PAÍS"
3. **Article Counting** - Finds and counts article elements
4. **Functionality Validation** - Ensures minimum article threshold is met
5. **Session Management** - Properly closes browser connections

## 🚀 Expected Test Output

Here's exactly what you'll see when running the complete solution:

```
Cross-Browser Testing Suite
Requirements:
- Run solution locally to verify functionality
- Execute on BrowserStack across 5 parallel threads
- Test desktop and mobile browsers

[OK] All dependencies are installed
============================================================
STEP 1: Running Local Test
============================================================

Running Local Test...
[OK] Page Title: Opinión en EL PAÍS
[OK] Found 27 articles
[OK] Local test passed - sufficient articles found

[OK] Local test passed! Proceeding to BrowserStack testing...
Starting BrowserStack cross-browser testing across 5 parallel threads...
Testing URL: https://elpais.com/opinion/
Browser configurations:
  - Chrome-Win11
  - Safari-MacOS
  - Firefox-Win10
  - Mobile-GalaxyS22
  - Mobile-iPhone13

[Chrome-Win11] Starting test...
[Safari-MacOS] Starting test...
[Firefox-Win10] Starting test...
[Mobile-GalaxyS22] Starting test...
[Mobile-iPhone13] Starting test...
[Safari-MacOS] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Safari-MacOS] Browser session closed.
[Firefox-Win10] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Firefox-Win10] Browser session closed.
[Mobile-iPhone13] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Mobile-GalaxyS22] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Mobile-iPhone13] Browser session closed.
[Mobile-GalaxyS22] Browser session closed.
[Chrome-Win11] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Chrome-Win11] Browser session closed.

All tests completed in 76.93 seconds

============================================================
STEP 2: Running BrowserStack Cross-Browser Test
============================================================

✅ All tests completed successfully!
✅ Solution validated locally
✅ Cross-browser testing completed on BrowserStack
```

## 🔧 Running Individual Components

### Run Complete Scraping Workflow
```bash
python main.py
```
*Executes the full article scraping, translation, and analysis process*

### Run Local Testing Only
```bash
python local_test.py
```
*Tests using your local Chrome browser only*

### Run BrowserStack Testing Only
```bash
python browserstack_test.py
```
*Runs cloud-based cross-browser tests only*

## 📊 Article Processing Features

### 1. Article Extraction
- Identifies first 5 opinion articles automatically
- Extracts Spanish titles and content
- Downloads cover images to local storage
- Organizes data in structured folders

### 2. Translation Processing
- Converts Spanish titles to English using Google Translate
- Maintains original Spanish text for reference
- Handles special characters and accents properly
- Saves both versions for comparison

### 3. Word Frequency Analysis
- Analyzes all translated English titles
- Identifies words appearing more than twice
- Counts total occurrences of each repeated word
- Displays statistical word frequency report

## ⚠️ Common Issues and Solutions

### 🔴 Dependency Installation Problems
**Error Message**: `ModuleNotFoundError: No module named 'selenium'`
**Solution**: 
```bash
pip install --upgrade pip
pip install selenium beautifulsoup4 requests python-dotenv webdriver-manager deep-translator
```

### 🔴 BrowserStack Authentication Issues
**Error Message**: `Missing credentials in .env`
**Solution**:
1. Verify `.env` file exists in project folder
2. Check BrowserStack username and access key are correct
3. Ensure no extra spaces in credential values
4. Confirm BrowserStack account is active with available minutes

### 🔴 Chrome Browser Not Found
**Error Message**: Chrome driver issues
**Solution**:
1. Install Google Chrome browser if not present
2. Update Chrome to latest version
3. `webdriver-manager` will handle driver installation automatically

### 🔴 Website Access Problems
**Error Message**: Connection timeout or page not loading
**Solution**:
1. Check internet connection stability
2. Verify El País website (`https://elpais.com/opinion/`) loads in browser
3. Try running tests at different times (site might be busy)
4. Check if your IP/location has access to the Spanish website

### 🔴 Low Article Count
**Warning**: Found fewer than 5 articles
**Solution**:
1. Website structure may have changed temporarily
2. Try running the script at different times of day
3. Check if Opinion section has recent articles published
4. Script will work with any number of available articles

## 📈 Performance Expectations

### Local Testing:
- **Duration**: 10-15 seconds
- **Resource Usage**: Low CPU and memory
- **Internet**: Required for page loading
- **Success Rate**: 95%+ for stable connections

### BrowserStack Testing:
- **Duration**: 60-90 seconds for all 5 browsers
- **Parallel Execution**: All browsers tested simultaneously
- **BrowserStack Minutes Used**: ~5 minutes from your quota
- **Success Rate**: 90%+ for active BrowserStack accounts

## 🎯 Success Criteria Checklist

A successful complete run includes:

**Local Phase:**
- ✅ All Python dependencies installed successfully
- ✅ Local Chrome browser opens El País Opinion page
- ✅ Page title correctly shows "Opinión en EL PAÍS"
- ✅ At least 5 articles detected on the page
- ✅ Spanish language content confirmed

**BrowserStack Phase:**
- ✅ All 5 browser configurations start successfully
- ✅ Each browser loads the Opinion page correctly
- ✅ All browsers find articles on the page
- ✅ No authentication or connection errors
- ✅ All browser sessions close properly

**Article Processing Phase (when running main.py):**
- ✅ First 5 articles extracted with Spanish titles
- ✅ Article content saved in Spanish
- ✅ Cover images downloaded successfully
- ✅ Spanish titles translated to English
- ✅ Word frequency analysis completed
- ✅ Repeated words identified and counted

## 📝 Additional Notes

- **Free Tier Limits**: BrowserStack free trial provides sufficient minutes for testing
- **Data Storage**: Extracted articles saved locally in `articles_data/` folder
- **Language Detection**: Script automatically validates Spanish content
- **Image Handling**: Cover images saved as JPG files in respective article folders
- **Translation Accuracy**: Uses Google Translate API for professional-quality translations
- **Cross-Platform**: Works on Windows, macOS, and Linux systems
- **Browser Support**: Tested across major browser engines (Chromium, WebKit, Gecko)

## 📋 Requirements Met

✅ **Local Testing First** - Validates functionality locally before cloud testing  
✅ **5 Parallel Threads** - Runs tests simultaneously on 5 different configurations  
✅ **Desktop + Mobile Mix** - Tests both desktop browsers and mobile devices  
✅ **BrowserStack Integration** - Uses professional cloud testing infrastructure

## 🛠️ Step-by-Step Setup Guide

### Step 1: Check Python Installation
Make sure you have Python 3.7 or higher installed:
```bash
python --version
```

### Step 2: Install Required Packages
Install all necessary dependencies one by one:

```bash
# Core web automation library
pip install selenium

# HTTP requests library  
pip install requests

# Environment variables management
pip install python-dotenv

# Or install everything at once
pip install -r requirements.txt
```

**What each package does:**
- `selenium` - Controls web browsers automatically
- `requests` - Makes HTTP requests to websites
- `python-dotenv` - Manages sensitive credentials securely

### Step 3: Create BrowserStack Account
1. Visit [BrowserStack.com](https://www.browserstack.com/)
2. Sign up for a free trial account
3. Go to "Account" → "Settings" to find your credentials
4. Create a `.env` file in the project folder with your credentials:

```env
BROWSERSTACK_USERNAME=your_actual_username
BROWSERSTACK_ACCESS_KEY=your_actual_access_key
```

### Step 4: Run the Complete Test Suite
Execute the main test runner:
```bash
python run_tests.py
```

## 🖥️ Browser Test Matrix

Our testing covers 5 different configurations running in parallel:

| Browser | Operating System | Device Type | Purpose |
|---------|------------------|-------------|---------|
| Chrome 91+ | Windows 11 | Desktop | Modern desktop experience |
| Safari 14+ | macOS Monterey | Desktop | Mac user experience |
| Firefox 89+ | Windows 10 | Desktop | Alternative browser testing |
| Samsung Internet | Galaxy S22 | Mobile | Android mobile experience |
| Safari Mobile | iPhone 13 | Mobile | iOS mobile experience |

## 📁 Project Structure

```
assignment/
├── run_tests.py          # Main test orchestrator
├── local_test.py         # Local browser testing
├── browserstack_test.py  # Cloud browser testing
├── main.py              # Core scraping functionality
├── requirements.txt     # Python dependencies
└── .env                # BrowserStack credentials (create this)
```

**File Descriptions:**
- **`run_tests.py`** - The main script that runs everything in order
- **`local_test.py`** - Tests using your local Chrome browser first
- **`browserstack_test.py`** - Tests on BrowserStack's cloud browsers
- **`main.py`** - Contains the core website scraping logic
- **`requirements.txt`** - Lists all Python packages needed

## 🧪 What Gets Tested

For each browser configuration, the test:
1. **Opens the El País Opinion page** (`https://elpais.com/opinion/`)
2. **Verifies the page title** (should be "Opinión en EL PAÍS")
3. **Counts article elements** (should find at least 10 articles)
4. **Reports success/failure** for each browser

## 🚀 Sample Test Output

Here's what you'll see when running the tests successfully:

```
Cross-Browser Testing Suite
Requirements:
- Run solution locally to verify functionality
- Execute on BrowserStack across 5 parallel threads
- Test desktop and mobile browsers

[OK] All dependencies are installed
============================================================
STEP 1: Running Local Test
============================================================

Running Local Test...
[OK] Page Title: Opinión en EL PAÍS
[OK] Found 27 articles
[OK] Local test passed - sufficient articles found

[OK] Local test passed! Proceeding to BrowserStack testing...
Starting BrowserStack cross-browser testing across 5 parallel threads...
Testing URL: https://elpais.com/opinion/
Browser configurations:
  - Chrome-Win11
  - Safari-MacOS
  - Firefox-Win10
  - Mobile-GalaxyS22
  - Mobile-iPhone13

[Chrome-Win11] Starting test...
[Safari-MacOS] Starting test...
[Firefox-Win10] Starting test...
[Mobile-GalaxyS22] Starting test...
[Mobile-iPhone13] Starting test...
[Safari-MacOS] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Safari-MacOS] Browser session closed.
[Firefox-Win10] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Firefox-Win10] Browser session closed.
[Mobile-iPhone13] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Mobile-GalaxyS22] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Mobile-iPhone13] Browser session closed.
[Mobile-GalaxyS22] Browser session closed.
[Chrome-Win11] [OK] Title: Opinión en EL PAÍS - Found 27 articles.
[Chrome-Win11] Browser session closed.

All tests completed in 76.93 seconds

✅ All tests completed successfully!
✅ Solution validated locally
✅ Cross-browser testing completed on BrowserStack
```

## 🔧 Running Individual Tests

You can also run specific parts of the test suite:

### Local Test Only
```bash
python local_test.py
```
This runs the test using your local Chrome browser.

### BrowserStack Test Only
```bash
python browserstack_test.py
```
This runs only the cloud-based cross-browser tests.

## ⚠️ Common Warnings and Solutions

### Security Warning
You might see this warning (it's harmless):
```
UserWarning: Embedding username and password in URL could be insecure, use ClientConfig instead
```
**Solution:** This is just a security notice from Selenium. Your credentials are still protected.

### Chrome DevTools Messages
You might see browser debugging messages like:
```
DevTools listening on ws://127.0.0.1:51712/devtools/browser/...
```
**Solution:** These are normal Chrome debugging messages and don't affect test results.

## 🆘 Troubleshooting

### Problem: "Missing dependency" error
**Solution:** Install the missing package:
```bash
pip install [package-name]
```

### Problem: BrowserStack authentication failed
**Solution:** 
1. Check your `.env` file has the correct credentials
2. Verify your BrowserStack account is active
3. Make sure you have available testing minutes

### Problem: Local test fails
**Solution:**
1. Make sure Chrome browser is installed
2. Check your internet connection
3. Verify the El País website is accessible

### Problem: Tests run but find 0 articles
**Solution:**
1. The website structure might have changed
2. Check if the website is loading properly in your browser
3. Verify your internet connection is stable

## 📊 Success Criteria

A successful test run means:
- ✅ Local test finds the correct page title
- ✅ Local test finds at least 10 articles  
- ✅ All 5 BrowserStack configurations complete successfully
- ✅ Each browser finds articles on the page
- ✅ No critical errors occur during testing

## 📝 Notes

- **Test Duration:** Typically takes 60-90 seconds to complete all tests
- **Data Usage:** Minimal - only loads the webpage content
- **BrowserStack Minutes:** Uses approximately 5 minutes of your BrowserStack quota
- **Internet Required:** Yes, for both local and cloud testing
