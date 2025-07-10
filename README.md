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
├── run_tests.py          
├── local_test.py         
├── browserstack_test.py  
├── main.py              
├── requirements.txt     
├── .env                
└── articles_data/       
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

## 📝 Final Notes & Tips

- **Free Tier Limits**: BrowserStack free trial provides sufficient minutes for testing
- **Data Storage**: Extracted articles saved locally in `articles_data/` folder
- **Language Detection**: Script automatically validates Spanish content
- **Image Handling**: Cover images saved as JPG files in respective article folders
- **Translation Accuracy**: Uses Google Translate API for professional-quality translations
- **Test Duration**: Typically takes 60-90 seconds to complete all cross-browser tests
- **BrowserStack Usage**: Uses approximately 5 minutes of your BrowserStack quota
- **Cross-Platform**: Works on Windows, macOS, and Linux systems
- **Browser Support**: Tested across major browser engines (Chromium, WebKit, Gecko)
