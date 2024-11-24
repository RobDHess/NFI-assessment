import subprocess
import sys
from pathlib import Path

# Dynamically add project_root to sys.path if it's not already present
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from config import MAIN_PATH


def run_main(spoor, profielen):
    """Run the main script with the given spoor and profielen sequences."""
    results = {}
    script_path = MAIN_PATH

    # Prepare inputs for a single session
    inputs = f"{spoor}\n"  # Input the spoor sequence
    for profiel in profielen:
        inputs += f"{profiel}\n"  # Input each profiel sequence
    inputs += "X\n"  # End the session with "X" to stop the program

    # Run the script in a subprocess
    process = subprocess.Popen(
        ["python3", script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Communicate with the subprocess
    stdout, stderr = process.communicate(input=inputs)

    # Check if the process was successful
    if process.returncode != 0:
        return {"error": stderr.strip()}

    # Process the output to extract all relevant lines for each profiel
    output_lines = stdout.strip().split("\n")
    prompt = "Voer een sequentie voor het dna profiel in:"
    exit_statement = "Het programma sluit af..."
    error_statement = "Een DNASpoor mag alleen bestaan uit:"
    results = {}

    # Loop over printed lines and extract the results for each profiel
    for line in output_lines:
        # Catch spoor error, which would set the first profiel as the spoor
        if error_statement in line:
            error_msg = line.removeprefix(
                "Voer een sequentie voor het spoor in:"
            ).strip()
            return {"error": error_msg}
        if prompt in line:
            if exit_statement in line:
                continue

            line = line.split(prompt)[1].strip()
            idx = len(results)
            profiel = profielen[idx]
            results[profiel] = line

    return results
