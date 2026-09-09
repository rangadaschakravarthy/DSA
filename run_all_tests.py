"""
Master Test Suite Runner

Automatically discovers and executes all level_*.py test files across all 19 topic folders.
Outputs a clean summary of test results.
"""

import os
import sys
import glob
import subprocess
import time

def run_all_tests():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    test_files = sorted(glob.glob(os.path.join(root_dir, "*", "level_*.py")))
    
    print("=" * 70)
    print(f"RUNNING DSA MASTER SUITE ({len(test_files)} TEST MODULES)")
    print("=" * 70)
    
    passed = 0
    failed = 0
    start_time = time.time()
    
    for file_path in test_files:
        rel_path = os.path.relpath(file_path, root_dir)
        t0 = time.time()
        
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True
        )
        
        elapsed = time.time() - t0
        
        if result.returncode == 0:
            passed += 1
            print(f"  [PASS] {rel_path:<45} ({elapsed:.3f}s)")
        else:
            failed += 1
            print(f"  [FAIL] {rel_path:<45} ({elapsed:.3f}s)")
            print("-" * 50)
            print(result.stderr)
            print("-" * 50)
            
    total_time = time.time() - start_time
    print("=" * 70)
    print(f"RESULTS: {passed} PASSED | {failed} FAILED | TOTAL: {len(test_files)}")
    print(f"Total Execution Time: {total_time:.2f} seconds")
    print("=" * 70)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
