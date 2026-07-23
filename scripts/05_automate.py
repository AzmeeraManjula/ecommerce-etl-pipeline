import os
import schedule
import time
import subprocess
from datetime import datetime

os.chdir(r'C:\Users\Aaryan\Desktop\Project')

def run_pipeline():
    print(f"\n{'='*50}")
    print(f"Pipeline started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

    scripts = scripts = [
    'scripts/02_transform.py',
    'scripts/04_load.py'
]

    for script in scripts:
        print(f"\nRunning {script}...")
        result = subprocess.run(
            ['python', script],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✓ {script} completed successfully")
        else:
            print(f"✗ {script} failed:")
            print(result.stderr)

    print(f"\n{'='*50}")
    print(f"Pipeline complete: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

# Run once immediately to test
print("Running pipeline once to test...")
run_pipeline()

# Schedule to run every day at 8 AM
schedule.every().day.at("08:00").do(run_pipeline)

print("\nScheduler is running!")
print("Pipeline will run automatically every day at 8:00 AM")
print("Press Ctrl+C to stop the scheduler")

while True:
    schedule.run_pending()
    time.sleep(60)