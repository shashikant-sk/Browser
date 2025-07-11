#!/usr/bin/env python3
"""
BrowserStack Test Results Analysis
==================================
This script analyzes the test results and provides actionable insights.
"""

import json
import os
from datetime import datetime

def analyze_results(results_file="browserstack_test_results.json"):
    """Analyze BrowserStack test results and provide insights"""
    
    if not os.path.exists(results_file):
        print(f"❌ Results file not found: {results_file}")
        print("   Run the tests first to generate results.")
        return False
    
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading results file: {e}")
        return False
    
    summary = data.get("summary", {})
    results = data.get("results", [])
    
    print("=" * 80)
    print("BROWSERSTACK TEST RESULTS ANALYSIS")
    print("=" * 80)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Build Name: {summary.get('build_name', 'N/A')}")
    print(f"Project: {summary.get('project_name', 'N/A')}")
    print(f"Target URL: {summary.get('target_url', 'N/A')}")
    print()
    
    # Overall Statistics
    print("📊 OVERALL PERFORMANCE")
    print("-" * 40)
    total_tests = summary.get('total_tests', 0)
    passed_tests = summary.get('passed', 0) 
    failed_tests = summary.get('failed', 0)
    success_rate = summary.get('success_rate', 0)
    total_time = summary.get('total_time', 0)
    
    print(f"Total Tests Executed: {total_tests}")
    print(f"Tests Passed: {passed_tests}")
    print(f"Tests Failed: {failed_tests}")
    print(f"Success Rate: {success_rate:.1f}%")
    print(f"Total Execution Time: {total_time:.2f} seconds")
    print(f"Average Time per Test: {(total_time/total_tests):.2f} seconds")
    print()
    
    # Browser Performance Analysis
    print("🌐 BROWSER PERFORMANCE BREAKDOWN")
    print("-" * 40)
    
    desktop_browsers = []
    mobile_browsers = []
    
    for result in results:
        browser_name = result.get('browser', 'Unknown')
        if 'Mobile-' in browser_name:
            mobile_browsers.append(result)
        else:
            desktop_browsers.append(result)
    
    print(f"Desktop Browsers: {len(desktop_browsers)}")
    print(f"Mobile Browsers: {len(mobile_browsers)}")
    print()
    
    # Detailed Results
    for result in results:
        status = result.get('status', 'UNKNOWN')
        browser = result.get('browser', 'Unknown')
        exec_time = result.get('execution_time', 'N/A')
        
        if status == "PASSED":
            articles = result.get('articles_found', 0)
            spanish_content = result.get('spanish_content', False)
            session_id = result.get('session_id', 'N/A')
            
            print(f"✅ {browser}")
            print(f"   Status: PASSED")
            print(f"   Articles Found: {articles}")
            print(f"   Spanish Content: {'Yes' if spanish_content else 'No'}")
            print(f"   Execution Time: {exec_time}")
            print(f"   Session ID: {session_id}")
            print()
        else:
            error = result.get('error', 'Unknown error')
            session_id = result.get('session_id', 'N/A')
            
            print(f"❌ {browser}")
            print(f"   Status: FAILED")
            print(f"   Error: {error}")
            print(f"   Execution Time: {exec_time}")
            if session_id != 'N/A':
                print(f"   Session ID: {session_id}")
            print()
    
    # Recommendations
    print("💡 RECOMMENDATIONS")
    print("-" * 40)
    
    if success_rate >= 80:
        print("✅ Good overall success rate! Your tests are performing well.")
    elif success_rate >= 60:
        print("⚠️ Moderate success rate. Consider reviewing failed tests.")
    else:
        print("❌ Low success rate. Immediate attention required.")
    
    if failed_tests > 0:
        print(f"\n🔧 Failed Tests Analysis:")
        for result in results:
            if result.get('status') == 'FAILED':
                browser = result.get('browser', 'Unknown')
                error = result.get('error', '')
                
                if 'Safari' in browser and 'Selenium JAR' in error:
                    print(f"   • {browser}: Update Safari browser version or downgrade Selenium")
                elif 'timeout' in error.lower():
                    print(f"   • {browser}: Increase timeout values or check network connectivity")
                elif 'element not found' in error.lower():
                    print(f"   • {browser}: Update element selectors or add explicit waits")
                else:
                    print(f"   • {browser}: Review detailed error logs for specific issue")
    
    # Performance Insights
    if total_tests > 0:
        avg_time = total_time / total_tests
        if avg_time > 30:
            print(f"\n⏱️ Performance: Tests are taking longer than expected ({avg_time:.1f}s avg)")
            print("   Consider optimizing wait times or page load strategies")
        elif avg_time < 10:
            print(f"\n⚡ Performance: Excellent test execution speed ({avg_time:.1f}s avg)")
        else:
            print(f"\n✅ Performance: Good test execution speed ({avg_time:.1f}s avg)")
    
    print("\n📋 NEXT STEPS")
    print("-" * 40)
    print("1. Review BrowserStack dashboard for detailed session recordings")
    print("2. Check console logs for any JavaScript errors")
    print("3. Verify that all article data was extracted correctly")
    print("4. Consider adding more robust retry mechanisms for failed tests")
    print("5. Monitor test stability over multiple runs")
    
    print("\n" + "=" * 80)
    
    return success_rate >= 80

if __name__ == "__main__":
    success = analyze_results()
    if success:
        print("🎉 Analysis complete - Tests are performing well!")
    else:
        print("⚠️ Analysis complete - Review recommendations above.")
