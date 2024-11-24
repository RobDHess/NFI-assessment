import time
import random
from pathlib import Path

from .utils import create_inputs, run_script


def test_performance(size=100, N=10, repeats=10, seed=0):
    """Test the performance of the script."""
    random.seed(seed)

    spoor_choices = "ATCGWSMKRYBDHVN"
    profiel_choices = "ATCG"

    times = []
    for _ in range(repeats):
        # Generate random spoor and profielen
        spoor = "".join(random.choices(spoor_choices, k=size))
        profielen = ["".join(random.choices(profiel_choices, k=size)) for _ in range(N)]

        inputs = create_inputs(spoor, profielen)

        # Measure the execution time
        start = time.time()
        run_script(inputs)
        end = time.time()
        times.append(end - start)

    # Calculate performance metrics
    avg_time = sum(times) / len(times)
    max_time = max(times)
    min_time = min(times)

    # Log results to a performance report
    report_path = Path("performance_report.txt")
    with report_path.open("w") as report_file:
        report_file.write(f"Performance Test Results:\n")
        report_file.write(
            f"Sequence size: {size}, Candidates: {N}, Repeats: {repeats}\n"
        )
        report_file.write(f"Average Time: {avg_time:.6f} seconds\n")
        report_file.write(f"Max Time: {max_time:.6f} seconds\n")
        report_file.write(f"Min Time: {min_time:.6f} seconds\n")
