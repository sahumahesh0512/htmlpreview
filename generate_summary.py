import json

# Load the JSON report
with open('test_report.json') as f:
    data = json.load(f)

# Extract summary information
summary = data.get('summary', {})
num_passed = summary.get('passed', 0)
num_failed = summary.get('failed', 0)
num_skipped = summary.get('skipped', 0)

# Extract duration
duration = data.get('duration', 0)  # The duration is in seconds

# Convert duration to minutes and seconds
minutes, seconds = divmod(duration, 60)
seconds = round(seconds, 2)  # Round seconds to 2 decimal places for better readability

# Generate markdown summary
with open('test_summary.md', 'w') as f:
    f.write('| Test Result :test_tube: | Passed :green_circle: | Failed :x: | Skipped :heavy_minus_sign: | Time Duration :alarm_clock: |\n')
    f.write('| ---------------------- | ------- | ----------- | ----------- | ------------- |\n')
    f.write(f'| Summary                | {num_passed}      | {num_failed}           | {num_skipped}           | {int(minutes)}m {seconds}s       |\n')
