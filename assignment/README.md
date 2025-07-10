# Cross-Browser Testing with BrowserStack

This project implements cross-browser testing as per the requirements:
1. ✅ Run solution locally to verify functionality
2. ✅ Execute on BrowserStack across 5 parallel threads  
3. ✅ Test combination of desktop and mobile browsers

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. BrowserStack Account
- Create a free trial account at [BrowserStack](https://www.browserstack.com/)
- Update `.env` file with your credentials:
```
BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
```

### 3. Run Tests
Execute the complete test suite:
```bash
python run_tests.py
```

Or run individual components:
- Local test only: `python local_test.py`
- BrowserStack only: `python browserstack_test.py`

## Test Configuration

### Browser Matrix (5 Parallel Threads)
1. **Chrome on Windows 11** (Desktop)
2. **Safari on macOS Monterey** (Desktop)  
3. **Firefox on Windows 10** (Desktop)
4. **Samsung Galaxy S22** (Mobile)
5. **iPhone 13** (Mobile)

### What Gets Tested
- Page loading and title extraction
- Article element detection on El País Opinion section
- Cross-browser compatibility verification

## Files Structure
- `run_tests.py` - Main test runner (follows requirements)
- `local_test.py` - Local validation before BrowserStack
- `browserstack_test.py` - BrowserStack cross-browser testing
- `main.py` - Original scraping functionality
- `requirements.txt` - Python dependencies
- `.env` - BrowserStack credentials

## Requirements Compliance

✅ **Local Testing First**: `local_test.py` validates functionality locally before BrowserStack

✅ **5 Parallel Threads**: Uses Python threading for simultaneous browser testing

✅ **Desktop + Mobile Mix**: Tests 3 desktop browsers + 2 mobile devices

✅ **BrowserStack Integration**: Configured with proper capabilities and credentials
