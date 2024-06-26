import json

# Load the test report
with open('test_report.json', 'r') as f:
    report = json.load(f)

# Initialize table
table_header = "| Test Result :test_tube: | Passed :green_circle: | Failed :x: | Skipped | Time Duration :alarm_clock: |\n"
table_header += "| ---------------------- | ------- | ------- | ------- | ---------------- |\n"
table_rows = ""

# Extract results
summary = report['summary']
num_tests = summary['total']
num_passed = summary['passed']
num_failed = summary['failed']
num_skipped = summary['skipped']
duration = summary['duration']

# Create table rows
row = f"| Total | {num_passed} | {num_failed} | {num_skipped} | {duration:.2f}s |\n"
table_rows += row

# Write the markdown table to a file
with open('test_summary.md', 'w') as f:
    f.write(table_header + table_rows)
