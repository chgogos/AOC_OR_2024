# Day 5

## Description
Hey, ORville here 👋

I'm a logistics manager overseeing the allocation of tasks to employees in our company, FurnitORe.

Right now we have 100 tasks that need to be completed, and we also have 100 employees available to handle them.

The catch is that assigning a task to an employee has a cost 💸.

These costs vary depending on the difficulty of the task, the expertise of the employee, and other factors.

I need your help to figure out the most cost-effective way to assign these tasks to employees.

You can assume that each task is done by just one employee, and one employee is assigned to just one task.

Can you help me solve this problem?

Here you can find an instance of this problem.

## Problem's data

[instance.txt](./instance.txt)

## Solution

[day3.py](./day5.py)

## Output
```
Solving with SCIP 9.0.0 [LP solver: Glop 9.11]
presolving:
(round 1, exhaustive) 0 del vars, 0 del conss, 0 add conss, 0 chg bounds, 0 chg sides, 0 chg coeffs, 200 upgd conss, 0 impls, 200 clqs
   (0.1s) probing: 51/10000 (0.5%) - 0 fixings, 0 aggregations, 0 implications, 0 bound changes
   (0.1s) probing aborted: 50/50 successive totally useless probings
   Deactivated symmetry handling methods, since SCIP was built without symmetry detector (SYM=none).
   Deactivated symmetry handling methods, since SCIP was built without symmetry detector (SYM=none).
presolving (2 rounds: 2 fast, 2 medium, 2 exhaustive):
 0 deleted vars, 0 deleted constraints, 0 added constraints, 0 tightened bounds, 0 added holes, 0 changed sides, 0 changed coefficients
 0 implications, 200 cliques
presolved problem has 10000 variables (10000 bin, 0 int, 0 impl, 0 cont) and 200 constraints
    200 constraints of type <setppc>
transformed objective value is always integral (scale: 1)
Presolving Time: 0.06

 time | node  | left  |LP iter|LP it/n|mem/heur|mdpt |vars |cons |rows |cuts |sepa|confs|strbr|  dualbound   | primalbound  |  gap   | compl. 
p 0.1s|     1 |     0 |     0 |     - |  clique|   0 |  10k| 200 | 200 |   0 |  0 |   0 |   0 | 0.000000e+00 | 6.430000e+02 |    Inf | unknown
* 0.1s|     1 |     0 |   297 |     - |    LP  |   0 |  10k| 202 | 200 |   0 |  0 |   5 |   0 | 3.050000e+02 | 3.050000e+02 |   0.00%| unknown
  0.1s|     1 |     0 |   297 |     - |    75M |   0 |  10k| 202 | 200 |   0 |  0 |   5 |   0 | 3.050000e+02 | 3.050000e+02 |   0.00%| unknown

SCIP Status        : problem is solved [optimal solution found]
Solving Time (sec) : 0.13
Solving Nodes      : 1
Primal Bound       : +3.05000000000000e+02 (2 solutions)
Dual Bound         : +3.05000000000000e+02
Gap                : 0.00 %
Total cost = 305.0

Worker 0 assigned to task 77. Cost: 6
Worker 1 assigned to task 6. Cost: 4
Worker 2 assigned to task 29. Cost: 2
Worker 3 assigned to task 39. Cost: 2
Worker 4 assigned to task 75. Cost: 2
Worker 5 assigned to task 17. Cost: 4
Worker 6 assigned to task 84. Cost: 3
Worker 7 assigned to task 31. Cost: 5
Worker 8 assigned to task 9. Cost: 2
Worker 9 assigned to task 27. Cost: 5
Worker 10 assigned to task 57. Cost: 4
Worker 11 assigned to task 72. Cost: 4
Worker 12 assigned to task 13. Cost: 2
Worker 13 assigned to task 0. Cost: 3
Worker 14 assigned to task 70. Cost: 2
Worker 15 assigned to task 66. Cost: 4
Worker 16 assigned to task 23. Cost: 2
Worker 17 assigned to task 85. Cost: 5
Worker 18 assigned to task 4. Cost: 3
Worker 19 assigned to task 94. Cost: 2
Worker 20 assigned to task 95. Cost: 4
Worker 21 assigned to task 64. Cost: 2
Worker 22 assigned to task 18. Cost: 4
Worker 23 assigned to task 93. Cost: 3
Worker 24 assigned to task 55. Cost: 3
Worker 25 assigned to task 81. Cost: 6
Worker 26 assigned to task 69. Cost: 3
Worker 27 assigned to task 83. Cost: 3
Worker 28 assigned to task 74. Cost: 2
Worker 29 assigned to task 21. Cost: 5
Worker 30 assigned to task 45. Cost: 4
Worker 31 assigned to task 65. Cost: 2
Worker 32 assigned to task 90. Cost: 6
Worker 33 assigned to task 71. Cost: 3
Worker 34 assigned to task 97. Cost: 3
Worker 35 assigned to task 1. Cost: 3
Worker 36 assigned to task 86. Cost: 2
Worker 37 assigned to task 82. Cost: 3
Worker 38 assigned to task 98. Cost: 4
Worker 39 assigned to task 59. Cost: 4
Worker 40 assigned to task 28. Cost: 2
Worker 41 assigned to task 30. Cost: 3
Worker 42 assigned to task 61. Cost: 2
Worker 43 assigned to task 88. Cost: 2
Worker 44 assigned to task 37. Cost: 2
Worker 45 assigned to task 80. Cost: 3
Worker 46 assigned to task 25. Cost: 3
Worker 47 assigned to task 48. Cost: 2
Worker 48 assigned to task 2. Cost: 2
Worker 49 assigned to task 36. Cost: 3
Worker 50 assigned to task 16. Cost: 2
Worker 51 assigned to task 32. Cost: 2
Worker 52 assigned to task 8. Cost: 2
Worker 53 assigned to task 53. Cost: 2
Worker 54 assigned to task 14. Cost: 2
Worker 55 assigned to task 73. Cost: 1
Worker 56 assigned to task 46. Cost: 2
Worker 57 assigned to task 58. Cost: 2
Worker 58 assigned to task 79. Cost: 2
Worker 59 assigned to task 7. Cost: 2
Worker 60 assigned to task 78. Cost: 4
Worker 61 assigned to task 47. Cost: 2
Worker 62 assigned to task 22. Cost: 2
Worker 63 assigned to task 41. Cost: 4
Worker 64 assigned to task 43. Cost: 3
Worker 65 assigned to task 11. Cost: 3
Worker 66 assigned to task 92. Cost: 4
Worker 67 assigned to task 38. Cost: 2
Worker 68 assigned to task 3. Cost: 4
Worker 69 assigned to task 50. Cost: 2
Worker 70 assigned to task 34. Cost: 3
Worker 71 assigned to task 63. Cost: 2
Worker 72 assigned to task 76. Cost: 5
Worker 73 assigned to task 89. Cost: 3
Worker 74 assigned to task 42. Cost: 3
Worker 75 assigned to task 87. Cost: 2
Worker 76 assigned to task 56. Cost: 3
Worker 77 assigned to task 15. Cost: 5
Worker 78 assigned to task 40. Cost: 4
Worker 79 assigned to task 49. Cost: 2
Worker 80 assigned to task 60. Cost: 5
Worker 81 assigned to task 24. Cost: 3
Worker 82 assigned to task 19. Cost: 4
Worker 83 assigned to task 54. Cost: 4
Worker 84 assigned to task 96. Cost: 5
Worker 85 assigned to task 62. Cost: 3
Worker 86 assigned to task 91. Cost: 4
Worker 87 assigned to task 26. Cost: 3
Worker 88 assigned to task 10. Cost: 2
Worker 89 assigned to task 35. Cost: 2
Worker 90 assigned to task 51. Cost: 2
Worker 91 assigned to task 52. Cost: 5
Worker 92 assigned to task 68. Cost: 2
Worker 93 assigned to task 33. Cost: 2
Worker 94 assigned to task 44. Cost: 3
Worker 95 assigned to task 20. Cost: 3
Worker 96 assigned to task 12. Cost: 2
Worker 97 assigned to task 5. Cost: 3
Worker 98 assigned to task 67. Cost: 4
Worker 99 assigned to task 99. Cost: 4
```