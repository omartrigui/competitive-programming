#!/usr/bin/env python

import subprocess
import sys

# -----------------------------------------------------------------------------
# Brute Force Stress Tester for Python Solutions (Python Version)
#
# Usage:
#   python brute.py <correct.py> <your_wrong.py>
#
# -----------------------------------------------------------------------------


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <correct.py> <your_wrong.py>")
    sys.exit(1)

CORRECT = sys.argv[1]
WRONG = sys.argv[2]

for i in range(1, 10000):
    print(f"Test #{i}")

    try:
        input_data = subprocess.check_output(["python", "gen.py"], text=True)
    except subprocess.CalledProcessError as e:
        print("Error generating input:", e)
        break

    try:
        out1 = subprocess.run(
            ["python", WRONG],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=2
        )
    except subprocess.TimeoutExpired:
        print("Timeout on your wrong solution!")
        break

    try:
        out2 = subprocess.run(
            ["python", CORRECT],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=2
        )
    except subprocess.TimeoutExpired:
        print("Timeout on correct solution!")
        break

    if out1.returncode != 0:
        print("❌ Error during execution of your wrong solution!")
        print("Input:")
        print(input_data)
        print("Stderr:")
        print(out1.stderr)
        break

    if out2.returncode != 0:
        print("❌ Error during execution of correct solution!")
        print("Input:")
        print(input_data)
        print("Stderr:")
        print(out2.stderr)
        break

    if out1.stdout.strip() != out2.stdout.strip():
        print("❌ Mismatch found!")
        print("Input:")
        print(input_data)
        print("Your output:")
        print(out1.stdout)
        print("Correct output:")
        print(out2.stdout)
        break
    else:
        print("✅ OK")
