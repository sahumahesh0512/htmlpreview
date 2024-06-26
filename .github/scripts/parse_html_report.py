import os
import sys
from bs4 import BeautifulSoup

def parse_html_report(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip header row

    test_results = {
        'total': 0,
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'duration': 0.0,
    }

    test_cases = []

    for row in rows:
        cols = row.find_all('td')
        test_name = cols[0].text
        result = cols[1].text
        time = float(cols[2].text.replace('s', ''))

        test_results['total'] += 1
        if result.lower() == 'passed':
            test_results['passed'] += 1
        elif result.lower() == 'failed':
            test_results['failed'] += 1
        elif result.lower() == 'skipped':
            test_results['skipped'] += 1
        
        test_results['duration'] += time
        test_cases.append((test_name, result, time))

    return test_results, test_cases

def generate_summary(test_results, test_cases):
    summary = "### Test Summary\n"
    summary += f"- **Total Tests**: {test_results['total']}\n"
    summary += f"- **Passed**: {test_results['passed']}\n"
    summary += f"- **Failed**: {test_results['failed']}\n"
    summary += f"- **Skipped**: {test_results['skipped']}\n"
    summary += f"- **Total Duration**: {test_results['duration']}s\n"

    summary += "\n### Test Details\n"
    for test in test_cases:
        summary += f"- **{test[0]}**: {test[1]} ({test[2]}s)\n"

    return summary

def append_to_summary(summary):
    summary_file = os.getenv('GITHUB_STEP_SUMMARY')
    if summary_file:
        with open(summary_file, 'a') as file:
            file.write(summary)
    else:
        print(summary)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: parse_html_report.py <path_to_html_report>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    test_results, test_cases = parse_html_report(file_path)
    summary = generate_summary(test_results, test_cases)
    append_to_summary(summary)
