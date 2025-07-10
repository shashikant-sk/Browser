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
    print("Cross-Browser Testing Suite")
    print("Requirements:")
    print("- Run solution locally to verify functionality")
    print("- Execute on BrowserStack across 5 parallel threads")
    print("- Test desktop and mobile browsers")
    print()
    
    # Check dependencies
    if not check_dependencies():
        return 1
    
    # Step 1: Local validation
    if not run_local_test():
        print("[FAIL] Local test failed! Stopping execution.")
        print("Please fix local issues before running BrowserStack tests.")
        return 1
    
    print("[OK] Local test passed! Proceeding to BrowserStack...")
    print()
    
    # Step 2: BrowserStack cross-browser testing
    if not run_browserstack_test():
        print("[FAIL] BrowserStack test encountered issues.")
        return 1
    
    print("\nAll tests completed successfully!")
    print("[OK] Solution validated locally")
    print("[OK] Cross-browser testing completed on BrowserStack")
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
