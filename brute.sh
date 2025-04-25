#!/bin/bash

# -----------------------------------------------------------------------------
# Brute Force Stress Tester for Python Solutions
#
# This script repeatedly generates random test cases using gen.py and compares
# the outputs of two Python programs: a "correct" reference solution and a
# potentially "wrong" solution under test. It is designed to help you find
# edge cases where your solution fails by running up to 999 tests or stopping
# early if a mismatch or timeout is detected.
#
# Usage:
#   ./brute.sh <correct.py> <your_wrong.py>
#
# Arguments:
#   correct.py     The reference solution expected to always produce correct output.
#   your_wrong.py  The solution you want to stress test.
#
# Requirements:
#   - gen.py must be present in the same directory and output valid test input.
#   - Python and the 'timeout' command must be available.
#
# The script prints the input and both outputs if a mismatch is found.
# -----------------------------------------------------------------------------


if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <correct.py> <your_wrong.py>"
    exit 1
fi

CORRECT="$1"
WRONG="$2"

for i in {1..999}; do

    echo "Test #$i"

    input_data=$(python gen.py)

    out1=$(echo "$input_data" | timeout 2s python "$WRONG")
    status1=$?
    out2=$(echo "$input_data" | timeout 2s python "$CORRECT")
    status2=$?

    if [[ $status1 -eq 124 || $status2 -eq 124 ]]; then
        echo "Timeout!"
        break
    fi

    if [[ "$out1" != "$out2" ]]; then
        echo "❌ Mismatch found!"
        echo "Input:"
        echo "$input_data"
        echo "Your output:"
        echo "$out1"
        echo "Correct output:"
        echo "$out2"
        break
    else
        echo "✅ OK"
    fi
done