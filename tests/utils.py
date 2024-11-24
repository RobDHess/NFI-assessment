import subprocess
import sys

from config import MAIN_PATH


def create_inputs(tracks, close=True):
    """Create a list of inputs for the script"""
    inputs = []
    for track in tracks:
        inputs.append(f"{track}\n")
    if close:
        inputs.append("X\n")
    return inputs


def run_script(inputs):
    """Run the script with the given inputs and return the result"""
    result = subprocess.run(
        [sys.executable, str(MAIN_PATH)],
        input="".join(inputs),
        text=True,
        capture_output=True,
    )
    return result
