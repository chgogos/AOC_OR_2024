# Day 8

## Description
Today I'm the Operations Manager at AmazOR, responsible for efficiently packing items into shipping containers.

I'm always looking for a clear, optimized packing plan to reduce our costs.

The fewer bins we use, the less money we spend on transportation and warehousing.

However, we must be careful not to violate container limits, as overpacked bins can lead to fines or damage.

I'll give you some examples of the issue that we have, considering:

* The bin capacity
* The number of items to be packed
* The number of bins we got in a solution (as a reference for you)
* And the size of each item to be packed

Can you help me solve this problem?
* PS: what strategies would you use to determine which items go into each bin?
* PS2: what challenges do you think arise when scaling this problem to thousands of items and multiple bin capacities?

## Problem's data

[instance.txt](./instance.txt)

## Notes

[ORTools - The Bin Packing Problem](https://developers.google.com/optimization/pack/bin_packing)

## Solution

* [day8.py](./day8.py)

## Output
```
SCIP 60sec
u120_00, bins_needed = 49, optimal bins = 48
u120_01, bins_needed = 51, optimal bins = 49
u120_02, bins_needed = 47, optimal bins = 46
u120_03, bins_needed = 51, optimal bins = 49
u120_04, bins_needed = 51, optimal bins = 50
u120_05, bins_needed = 50, optimal bins = 48
u120_06, bins_needed = 49, optimal bins = 48
u120_07, bins_needed = 50, optimal bins = 49
u120_08, bins_needed = 51, optimal bins = 51 (*)
u120_09, bins_needed = 47, optimal bins = 46
u120_10, bins_needed = 53, optimal bins = 52
u120_11, bins_needed = 51, optimal bins = 49
u120_12, bins_needed = 50, optimal bins = 48
u120_13, bins_needed = 50, optimal bins = 49
u120_14, bins_needed = 51, optimal bins = 50
u120_15, bins_needed = 49, optimal bins = 48
u120_16, bins_needed = 53, optimal bins = 52
u120_17, bins_needed = 54, optimal bins = 52
u120_18, bins_needed = 50, optimal bins = 49
u120_19, bins_needed = 51, optimal bins = 50
Optimality reached in 1 instances
```