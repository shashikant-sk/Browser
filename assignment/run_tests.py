"""
Cross-Browser Testing Suite
==========================
This script follows the requirements:
1. Run solution locally to verify functionality
2. Execute on BrowserStack across 5 parallel threads
3. Test combination of desktop and mobile browsers
"""

import os
import subprocess
import sys

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import selenium
        import requests
        from dotenv import load_dotenv
        print("[OK] All dependencies are installed")
        return True
    except ImportError as e:
        print(f"[FAIL] Missing dependency: {e}")
        print("Please install dependencies: pip install -r requirements.txt")
        return False

def run_local_test():
    """Run local test first as per requirements"""
    print("=" * 60)
    print("STEP 1: Running Local Test")
    print("=" * 60)
    
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_test_path = os.path.join(script_dir, "local_test.py")
        
        result = subprocess.run([sys.executable, local_test_path], 
                              capture_output=True, text=True, cwd=script_dir)
        
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
            
        return result.returncode == 0
    except Exception as e:
        print(f"[FAIL] Failed to run local test: {e}")
        return False

def run_browserstack_test():
    """Run BrowserStack cross-browser test"""
    print("=" * 60)
    print("STEP 2: Running BrowserStack Cross-Browser Test")
    print("=" * 60)
    
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        browserstack_test_path = os.path.join(script_dir, "browserstack_test.py")
        
        result = subprocess.run([sys.executable, browserstack_test_path], 
                              capture_output=True, text=True, cwd=script_dir)
        
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
            
        return result.returncode == 0
    except Exception as e:
        print(f"[FAIL] Failed to run BrowserStack test: {e}")
        return False

def main():
    """Main execution following the requirements"""
    print("=" * 80)
    print("CROSS-BROWSER TESTING SUITE - El País Web Scraping Project")
    print("=" * 80)
    print("Requirements validation:")
    print("- Run solution locally to verify functionality")
    print("- Execute on BrowserStack across 5 parallel threads")
    print("- Test desktop and mobile browsers")
    print("- Validate Spanish content and article extraction")
    print()
    
    # Check dependencies
    if not check_dependencies():
        return 1
    
    # Step 1: Local validation
    print("PHASE 1: Local Environment Validation")
    print("-" * 50)
    if not run_local_test():
        print("\n[CRITICAL] Local test validation failed!")
        print("   Please fix local issues before running BrowserStack tests.")
        print("   Common issues:")
        print("   - Network connectivity to elpais.com")
        print("   - Chrome driver installation")
        print("   - Website structure changes")
        return 1
    
    print("\n[SUCCESS] Local validation passed!")
    print("   All basic functionality verified locally")
    print()
    
    # Step 2: BrowserStack cross-browser testing
    print("PHASE 2: BrowserStack Cross-Browser Testing")
    print("-" * 50)
    
    try:
        if not run_browserstack_test():
            print("\n[WARNING] Some BrowserStack tests encountered issues.")
            print("   Check the detailed results above for specific failures.")
            print("   Note: Partial failures may be acceptable depending on requirements.")
            return 1
    except Exception as e:
        print(f"\n[ERROR] Failed to execute BrowserStack tests: {e}")
        return 1
    
    print("\n" + "=" * 80)
    print("TESTING SUITE COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print("Local validation: PASSED")
    print("BrowserStack execution: COMPLETED")
    print("Cross-browser compatibility: VERIFIED")
    print("Spanish content validation: CONFIRMED")
    print("\nNext Steps:")
    print("   1. Review browserstack_test_results.json for detailed analysis")
    print("   2. Check BrowserStack dashboard for session recordings")
    print("   3. Verify article data extraction in articles_data/ folder")
    print("=" * 80)
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
