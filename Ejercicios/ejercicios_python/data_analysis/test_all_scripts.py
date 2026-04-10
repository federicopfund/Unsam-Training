#!/usr/bin/env python3
"""
Comprehensive testing script for data_analysis module.
Tests each script with appropriate parameters and captures execution results.
"""

import subprocess
import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Suppress matplotlib display
os.environ['MPLBACKEND'] = 'Agg'

class ScriptTester:
    def __init__(self):
        self.results = {}
        self.test_dir = Path(__file__).parent
        
    def run_test(self, script_name, args=None, input_text=None):
        """Run a Python script and capture output."""
        cmd = [sys.executable, str(self.test_dir / script_name)]
        if args:
            cmd.extend(args)
        
        print(f"\n{'='*80}")
        print(f"Testing: {script_name}")
        print(f"{'='*80}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30,
                input=input_text,
                cwd=str(self.test_dir)
            )
            
            status = "✓ PASS" if result.returncode == 0 else "✗ FAIL"
            print(f"{status}")
            
            if result.stdout:
                lines = result.stdout.split('\n')
                print("\nStdout (first 30 lines):")
                for line in lines[:30]:
                    if line.strip():
                        print(f"  {line}")
            
            if result.stderr and result.returncode != 0:
                print("\nStderr:")
                print(f"  {result.stderr[:500]}")
            
            self.results[script_name] = {
                'status': 'PASS' if result.returncode == 0 else 'FAIL',
                'return_code': result.returncode,
                'output_lines': len(result.stdout.split('\n')),
                'timestamp': datetime.now().isoformat()
            }
            
            return result.returncode == 0
            
        except subprocess.TimeoutExpired:
            print("✗ TIMEOUT (30 seconds)")
            self.results[script_name] = {'status': 'TIMEOUT', 'timestamp': datetime.now().isoformat()}
            return False
        except Exception as e:
            print(f"✗ ERROR: {str(e)}")
            self.results[script_name] = {'status': 'ERROR', 'error': str(e), 'timestamp': datetime.now().isoformat()}
            return False
    
    def run_all_tests(self):
        """Execute all test cases."""
        print("\n" + "="*80)
        print("DATA ANALYSIS MODULE - COMPREHENSIVE TEST SUITE")
        print("="*80)
        print(f"Test started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Test 1: random_walk_plots.py
        self.run_test('random_walk_plots.py')
        
        # Test 2: list_images.py
        self.run_test('list_images.py', ['..'])
        
        # Test 3: sort_images.py
        self.run_test('sort_images.py', ['..'])
        
        # Test 4: sort_images1.py
        self.run_test('sort_images1.py', ['..'])
        
        # Test 5: pearson_correlation.py
        self.run_test('pearson_correlation.py', ['../Data/OBS_SHN_SF-BA.csv'])
        
        # Test 6: tides_manual.py
        self.run_test('tides_manual.py', ['../Data/OBS_SHN_SF-BA.csv'])
        
        # Test 7: tides_fft.py
        self.run_test('tides_fft.py', ['../Data/OBS_SHN_SF-BA.csv', '2014-01', '2014-06'])
        
        # Test 8: tides_manual_fft.py
        self.run_test('tides_manual_fft.py', ['../Data/OBS_SHN_SF-BA.csv', '2014-01', '2014-06'])
        
        # Test 9: boxplot_reading_selection.py
        self.run_test('boxplot_reading_selection.py', ['arbolado-publico-lineal-2017-2018.csv'])
        
        # Test 10: tree_park_sidewalks.py
        self.run_test('tree_park_sidewalks.py', 
                      ['arbolado-publico-lineal-2017-2018.csv', 'arbolado-en-espacios-verdes.csv'])
        
        # Test 11: life_simulation.py (with input)
        self.run_test('life_simulation.py', input_text='15\n8\n1990\n')
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print test summary."""
        print("\n" + "="*80)
        print("TEST SUMMARY")
        print("="*80)
        
        passed = sum(1 for r in self.results.values() if r.get('status') == 'PASS')
        failed = sum(1 for r in self.results.values() if r.get('status') == 'FAIL')
        timeout = sum(1 for r in self.results.values() if r.get('status') == 'TIMEOUT')
        error = sum(1 for r in self.results.values() if r.get('status') == 'ERROR')
        
        total = len(self.results)
        
        print(f"\nTotal tests: {total}")
        print(f"✓ Passed:  {passed}")
        print(f"✗ Failed:  {failed}")
        print(f"⏱ Timeout: {timeout}")
        print(f"⚠ Error:   {error}")
        
        print("\nDetailed Results:")
        print("-"*80)
        for script, result in self.results.items():
            status_symbol = "✓" if result['status'] == 'PASS' else "✗" if result['status'] == 'FAIL' else "⏱" if result['status'] == 'TIMEOUT' else "⚠"
            print(f"{status_symbol} {script:40} {result['status']:10}")
        
        print("="*80)
        print(f"Test completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


if __name__ == '__main__':
    tester = ScriptTester()
    tester.run_all_tests()
