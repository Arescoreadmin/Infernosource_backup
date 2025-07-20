# backend/lighthouse_utils.py

import subprocess
import json
import os

def run_lighthouse(url: str, output_path: str = "lighthouse_report.json") -> dict:
    """
    Run Lighthouse CLI on the given URL and save the report as JSON.
    Requires Lighthouse installed globally: npm install -g lighthouse
    """
    try:
        cmd = [
            "lighthouse",
            url,
            "--quiet",
            "--chrome-flags='--headless'",
            f"--output=json",
            f"--output-path={output_path}"
        ]
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(" ".join(cmd), shell=True, check=True)
        with open(output_path, "r", encoding="utf-8") as f:
            report = json.load(f)
        print(f"Lighthouse audit complete. Results saved to {output_path}")
        return report
    except Exception as e:
        print(f"Error running Lighthouse: {e}")
        return {}

if __name__ == "__main__":
    test_url = "https://example.com"
    report = run_lighthouse(test_url)
    if report:
        print(json.dumps(report, indent=2)[:1500])  # Print first part of the report
    else:
        print("Lighthouse audit failed.")
