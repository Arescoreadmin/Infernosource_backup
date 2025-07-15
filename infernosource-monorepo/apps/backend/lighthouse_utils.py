import subprocess
import json
import os

def run_lighthouse(url: str, output_path: str = "lighthouse_report.json") -> dict:
    """
    Runs Lighthouse CLI on the given URL and returns the parsed JSON report.

    Parameters:
        url (str): The website URL to audit.
        output_path (str): File path to save the Lighthouse JSON report.

    Returns:
        dict: Parsed Lighthouse audit results or error message.
    """

    try:
        # Run lighthouse with headless chrome and JSON output
        result = subprocess.run(
            [
                "lighthouse",
                url,
                "--output=json",
                f"--output-path={output_path}",
                "--quiet",
                "--chrome-flags=--headless"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        # Load JSON results from output file
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        else:
            return {"error": "Lighthouse did not generate an output file."}

    except subprocess.CalledProcessError as e:
        return {
            "error": "Lighthouse CLI execution failed.",
            "details": e.stderr
        }
    except Exception as ex:
        return {
            "error": "Unexpected error occurred while running Lighthouse.",
            "details": str(ex)
        }
