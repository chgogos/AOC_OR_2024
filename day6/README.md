# Day 6

## Description
Hi, IsiDOra qui 🇮🇹

I'm a railway operations planner in La FerrORvia Italiana.

Our railway system in Italy is one of the busiest in Europe, and efficient planning is crucial to maitaining smooth operations.

We face a logistical challenge: optimizing the assignment of maintenance resources to ensure that all critical segments of our railway network are covered.

We want to minimize the costs of such operations.

Can you help me solve this problem?

## Problem's data

[instance.txt](./instance.txt)

## Solution

* [day6.py](./day6.py)

## Output
```
# segments = 507
# possibilities = 63009
Possibility index=0, cost=2, segments=[42, 43, 44, 318, 319, 422, 423]
Possibility index=1, cost=2, segments=[42, 43, 56, 11, 373]
Possibility index=2, cost=2, segments=[42, 43, 56, 262, 263, 372, 373]
Possibility index=3, cost=2, segments=[42, 43, 56, 262, 263, 373]
Possibility index=4, cost=2, segments=[42, 43, 56, 262, 372, 373]
Possibility index=5, cost=2, segments=[42, 43, 124, 38, 129, 36, 37]
Possibility index=6, cost=2, segments=[42, 43, 124, 38, 462, 129, 36, 37]
Possibility index=7, cost=2, segments=[42, 43, 124, 458, 129, 36, 37, 414]
Possibility index=8, cost=2, segments=[42, 43, 124, 458, 459, 460, 402, 403, 414]
Possibility index=9, cost=2, segments=[42, 43, 124, 458, 459, 460, 402, 414]
Possibility index=10, cost=2, segments=[42, 43, 124, 459, 460, 402, 403, 414]
Possibility index=11, cost=2, segments=[42, 43, 124, 459, 460, 402, 414]
Possibility index=12, cost=2, segments=[42, 43, 124, 462, 129, 36, 37, 414]
Possibility index=13, cost=2, segments=[42, 43, 124, 462, 129, 36, 37, 423]
Possibility index=14, cost=1, segments=[42, 43, 124, 125]
Possibility index=15, cost=2, segments=[42, 43, 124, 269, 36, 37, 414, 424]
Possibility index=16, cost=2, segments=[42, 43, 124, 269, 36, 37, 423, 424]
Possibility index=17, cost=2, segments=[42, 43, 124, 269, 36, 273, 370]
Possibility index=18, cost=2, segments=[42, 43, 124, 269, 36, 380, 372, 373]
Possibility index=19, cost=2, segments=[42, 43, 124, 269, 36, 380, 373]
Possibility index=62990, cost=2, segments=[388, 389, 269, 36, 380, 467, 386, 387]
Possibility index=62991, cost=2, segments=[388, 389, 269, 37, 385, 386, 387]
Possibility index=62992, cost=2, segments=[388, 389, 269, 37, 385, 387]
Possibility index=62993, cost=2, segments=[388, 389, 269, 130]
Possibility index=62994, cost=2, segments=[388, 389, 269, 375, 263, 264]
Possibility index=62995, cost=2, segments=[388, 389, 269, 375, 263, 386, 387]
Possibility index=62996, cost=2, segments=[388, 389, 269, 375, 263, 387]
Possibility index=62997, cost=2, segments=[388, 389, 269, 375, 273, 386, 387]
Possibility index=62998, cost=2, segments=[388, 389, 269, 375, 376]
Possibility index=62999, cost=2, segments=[388, 389, 269, 375, 380, 381]
Possibility index=63000, cost=2, segments=[388, 389, 269, 375, 380, 386, 387]
Possibility index=63001, cost=2, segments=[388, 389, 269, 375, 380, 387]
Possibility index=63002, cost=2, segments=[388, 389, 269, 375, 380, 467, 386, 387]
Possibility index=63003, cost=2, segments=[388, 389, 269, 375, 381]
Possibility index=63004, cost=2, segments=[388, 389, 269, 376]
Possibility index=63005, cost=2, segments=[388, 389, 269, 454, 263, 264]
Possibility index=63006, cost=2, segments=[388, 389, 269, 454, 264]
Possibility index=63007, cost=2, segments=[388, 389, 269, 454, 380, 381]
Possibility index=63008, cost=2, segments=[388, 389, 269, 454, 381]

Starting CP-SAT solver v9.11.4210
Parameters: max_time_in_seconds: 300 log_search_progress: true
Setting number of workers to 10

Initial optimization model '': (model_fingerprint: 0x3b54f2abc83d4151)
#Variables: 63'009 (#bools: 63'009 in objective)
  - 63'009 Booleans in [0,1]
#kLinear1: 8
#kLinear2: 3
#kLinear3: 3
#kLinearN: 493 (#terms: 409'326)

Starting presolve at 0.01s
  7.56e-02s  0.00e+00d  [DetectDominanceRelations] 
  1.43e-01s  0.00e+00d  [PresolveToFixPoint] #num_loops=4 #num_dual_strengthening=2 
  1.99e-04s  0.00e+00d  [ExtractEncodingFromLinear] 
[Symmetry] Graph for symmetry has 147'034 nodes and 608'222 arcs.
[Symmetry] Symmetry computation done. time: 0.022113 dtime: 0.0560056
[Symmetry] #generators: 565, average support size: 2
[Symmetry] The model contains 5 duplicate constraints !
[Symmetry] 549 orbits with sizes: 3,3,3,3,3,3,3,3,3,3,...
[Symmetry] Found orbitope of size 1 x 2
[SAT presolve] num removable Booleans: 0 / 62999
[SAT presolve] num trivial clauses: 0
[SAT presolve] [0s] clauses:58975 literals:524686 vars:62999 one_side_vars:43981 simple_definition:9731 singleton_clauses:0
[SAT presolve] [0.194404s] clauses:58957 literals:405785 vars:62998 one_side_vars:62997 simple_definition:1 singleton_clauses:0
[SAT presolve] [0.19889s] clauses:58957 literals:405785 vars:62998 one_side_vars:62997 simple_definition:1 singleton_clauses:0
  1.33e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.41e-01s  1.04e+00d *[Probe] #probed=126'000 
  4.60e-02s  0.00e+00d  [MaxClique] Merged 58492(116984 literals) into 58489(116980 literals) at_most_ones. 
  4.32e-02s  0.00e+00d  [DetectDominanceRelations] 
  3.55e-02s  0.00e+00d  [DetectDominanceRelations] 
  1.35e-01s  0.00e+00d  [PresolveToFixPoint] #num_loops=3 #num_dual_strengthening=3 
  3.84e-03s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  1.03e-02s  0.00e+00d  [DetectDuplicateConstraints] 
  9.70e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  7.16e-04s  0.00e+00d  [DetectDominatedLinearConstraints] 
  6.72e-04s  0.00e+00d  [DetectDifferentVariables] 
  1.20e-02s  1.39e-03d  [ProcessSetPPC] #relevant_constraints=466 
  9.43e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  2.91e-03s  9.76e-04d  [FindBigAtMostOneAndLinearOverlap] 
  2.62e-03s  1.91e-03d  [FindBigVerticalLinearOverlap] 
  8.22e-04s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  5.56e-03s  1.44e-03d  [MergeClauses] 
  3.55e-02s  0.00e+00d  [DetectDominanceRelations] 
  5.09e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  3.60e-02s  0.00e+00d  [DetectDominanceRelations] 
  5.07e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
[Symmetry] Graph for symmetry has 100'068 nodes and 374'271 arcs.
[Symmetry] Symmetry computation done. time: 0.013962 dtime: 0.0337467
[Symmetry] #generators: 1205, average support size: 2
[Symmetry] 1116 orbits with sizes: 6,6,6,6,6,6,4,4,4,4,...
[Symmetry] Found orbitope of size 1 x 2
[SAT presolve] num removable Booleans: 0 / 43976
[SAT presolve] num trivial clauses: 0
[SAT presolve] [0s] clauses:25282 literals:337677 vars:43976 one_side_vars:34841 simple_definition:4872 singleton_clauses:0
[SAT presolve] [0.089737s] clauses:25274 literals:273581 vars:43976 one_side_vars:43975 simple_definition:1 singleton_clauses:0
[SAT presolve] [0.092757s] clauses:25274 literals:273581 vars:43976 one_side_vars:43975 simple_definition:1 singleton_clauses:0
  9.86e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.16e-01s  1.03e+00d *[Probe] #probed=87'962 
  2.23e-02s  0.00e+00d  [MaxClique] Merged 24820(49640 literals) into 24818(49637 literals) at_most_ones. 
  3.53e-02s  0.00e+00d  [DetectDominanceRelations] 
  6.82e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=2 #num_dual_strengthening=2 
  2.98e-03s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  8.74e-03s  0.00e+00d  [DetectDuplicateConstraints] 
  8.14e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  7.37e-04s  0.00e+00d  [DetectDominatedLinearConstraints] 
  6.89e-04s  0.00e+00d  [DetectDifferentVariables] 
  9.03e-03s  1.04e-03d  [ProcessSetPPC] #relevant_constraints=458 
  7.98e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  2.25e-03s  5.54e-04d  [FindBigAtMostOneAndLinearOverlap] 
  2.38e-03s  1.44e-03d  [FindBigVerticalLinearOverlap] 
  7.99e-04s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  5.44e-03s  1.12e-03d  [MergeClauses] 
  3.00e-02s  0.00e+00d  [DetectDominanceRelations] 
  4.32e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  3.10e-02s  0.00e+00d  [DetectDominanceRelations] 
  4.41e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
[Symmetry] Graph for symmetry has 84'275 nodes and 273'681 arcs.
[Symmetry] Symmetry computation done. time: 0.01128 dtime: 0.0248897
[Symmetry] #generators: 1109, average support size: 2
[Symmetry] 1002 orbits with sizes: 6,6,6,6,5,4,4,4,4,4,...
[Symmetry] Found orbitope of size 1 x 2
[SAT presolve] num removable Booleans: 0 / 34841
[SAT presolve] num trivial clauses: 0
[SAT presolve] [0s] clauses:14919 literals:252871 vars:34841 one_side_vars:29912 simple_definition:2289 singleton_clauses:0
[SAT presolve] [0.046634s] clauses:14908 literals:213137 vars:34841 one_side_vars:34840 simple_definition:1 singleton_clauses:0
[SAT presolve] [0.049028s] clauses:14908 literals:213137 vars:34841 one_side_vars:34840 simple_definition:1 singleton_clauses:0
  7.66e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.11e-01s  1.02e+00d *[Probe] #probed=69'694 
  1.35e-02s  0.00e+00d  [MaxClique] 
  3.67e-02s  0.00e+00d  [DetectDominanceRelations] 
  6.70e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=3 #num_dual_strengthening=3 
  2.94e-03s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  7.58e-03s  0.00e+00d  [DetectDuplicateConstraints] 
  7.48e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  8.11e-04s  0.00e+00d  [DetectDominatedLinearConstraints] 
  8.03e-04s  0.00e+00d  [DetectDifferentVariables] 
  8.25e-03s  8.25e-04d  [ProcessSetPPC] #relevant_constraints=447 
  9.35e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  2.05e-03s  3.77e-04d  [FindBigAtMostOneAndLinearOverlap] 
  1.86e-03s  1.17e-03d  [FindBigVerticalLinearOverlap] 
  8.42e-04s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  4.82e-03s  9.21e-04d  [MergeClauses] 
  2.90e-02s  0.00e+00d  [DetectDominanceRelations] 
  4.14e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  6.02e-03s  0.00e+00d  [ExpandObjective] 

Presolve summary:
  - 1 affine relations were detected.
  - rule 'TODO domination: unexploited dominations' was applied 3 times.
  - rule 'TODO dual: only one blocking constraint?' was applied 62 times.
  - rule 'TODO dual: only one unspecified blocking constraint?' was applied 564'553 times.
  - rule 'TODO linear2: contains a Boolean.' was applied 2 times.
  - rule 'affine: new relation' was applied 1 time.
  - rule 'at_most_one: empty or all false' was applied 1 time.
  - rule 'at_most_one: removed literals' was applied 97'762 times.
  - rule 'at_most_one: resolved two constraints with opposite literal' was applied 2 times.
  - rule 'at_most_one: singleton' was applied 16'877 times.
  - rule 'at_most_one: size one' was applied 97'758 times.
  - rule 'at_most_one: transformed into max clique.' was applied 2 times.
  - rule 'bool_and: dual equality.' was applied 1 time.
  - rule 'bool_and: x => x' was applied 1 time.
  - rule 'bool_or: always true' was applied 3 times.
  - rule 'bool_or: implications' was applied 1 time.
  - rule 'domination: added implications' was applied 107'577 times.
  - rule 'domination: in at most one' was applied 1 time.
  - rule 'dual: fix variable' was applied 16'204 times.
  - rule 'exactly_one: singleton' was applied 3 times.
  - rule 'linear: always true' was applied 11 times.
  - rule 'linear: empty' was applied 7 times.
  - rule 'linear: fixed or dup variables' was applied 18 times.
  - rule 'linear: positive clause' was applied 489 times.
  - rule 'linear: reduced variable domains' was applied 7 times.
  - rule 'linear: simplified rhs' was applied 496 times.
  - rule 'objective: variable not used elsewhere' was applied 16'887 times.
  - rule 'presolve: 33091 unused variables removed.' was applied 1 time.
  - rule 'presolve: iteration' was applied 3 times.
  - rule 'symmetry: added symmetry breaking implication' was applied 3 times.

Presolved optimization model '': (model_fingerprint: 0x591433126e57f459)
#Variables: 29'912 (#bools: 29'912 in objective)
  - 29'912 Booleans in [0,1]
#kBoolAnd: 9'819 (#enforced: 9'819) (#literals: 19'638)
#kBoolOr: 443 (#literals: 184'207)

Preloading model.
#Bound   2.32s best:inf   next:[16,57799] initial_domain
[Symmetry] Graph for symmetry has 45'477 nodes and 218'967 arcs.
[Symmetry] Symmetry computation done. time: 0.009047 dtime: 0.0199804
[Symmetry] #generators: 1841, average support size: 2
[Symmetry] Found orbitope of size 1 x 2
#Model   2.34s var:29912/29912 constraints:10262/10262

Starting search at 2.34s with 10 workers.
7 full problem subsolvers: [core, default_lp, max_lp, no_lp, quick_restart, quick_restart_no_lp, reduced_costs]
3 first solution subsolvers: [fj, fs_random, fs_random_no_lp]
10 interleaved subsolvers: [feasibility_pump, graph_arc_lns, graph_cst_lns, graph_dec_lns, graph_var_lns, ls(2), rins/rens, rnd_cst_lns, rnd_var_lns]
3 helper subsolvers: [neighborhood_helper, synchronization_agent, update_gap_integral]

#Bound   2.42s best:inf   next:[24,57799] am1_presolve (num_literals=29912 num_am1=5 increase=8 work_done=39737)
#1       2.43s best:326   next:[24,325]   no_lp (fixed_bools=0/29912)
#2       2.44s best:324   next:[24,323]   fj_restart(batch:1 lin{mvs:167 evals:847} #w_updates:3 #perturb:0)
#Bound   2.72s best:324   next:[26,323]   bool_core (num_cores=1 [size:51 mw:2 d:6] a=29857 d=6 fixed=0/29966 clauses=505)
#Bound   2.96s best:324   next:[28,323]   bool_core (num_cores=2 [size:130 mw:2 d:8] a=29728 d=8 fixed=0/30144 clauses=671)
#Bound   3.11s best:324   next:[169,323]  reduced_costs
#Bound   3.80s best:324   next:[173,323]  reduced_costs
#3       4.47s best:248   next:[173,247]  quick_restart_no_lp (fixed_bools=0/29912)
#4       4.83s best:245   next:[173,244]  quick_restart_no_lp (fixed_bools=0/29912)
#5       5.02s best:241   next:[173,240]  quick_restart (fixed_bools=0/29912)
#6       8.72s best:240   next:[173,239]  quick_restart_no_lp (fixed_bools=0/29912)
#7       9.59s best:182   next:[173,181]  reduced_costs (fixed_bools=0/29912)
#Model  10.40s var:29911/29912 constraints:10123/10262
#8      10.67s best:177   next:[173,176]  max_lp (fixed_bools=0/29912)
#9      20.41s best:176   next:[173,175]  reduced_costs (fixed_bools=1/29912)
#10     33.20s best:175   next:[173,174]  max_lp (fixed_bools=1/29912)
#Model  48.88s var:29351/29912 constraints:9373/10262
#Model 136.20s var:29330/29912 constraints:9358/10262
#Model 142.25s var:29327/29912 constraints:9355/10262

Task timing                      n [     min,      max]      avg      dev     time         n [     min,      max]      avg      dev    dtime
                 'core':         1 [   4.96m,    4.96m]    4.96m   0.00ns    4.96m         1 [  12.85m,   12.85m]   12.85m   0.00ns   12.85m
           'default_lp':         1 [   4.96m,    4.96m]    4.96m   0.00ns    4.96m         1 [   3.97m,    3.97m]    3.97m   0.00ns    3.97m
     'feasibility_pump':         1 [ 25.59ms,  25.59ms]  25.59ms   0.00ns  25.59ms         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                   'fj':         1 [ 79.42ms,  79.42ms]  79.42ms   0.00ns  79.42ms         1 [ 16.64ms,  16.64ms]  16.64ms   0.00ns  16.64ms
            'fs_random':         1 [119.59ms, 119.59ms] 119.59ms   0.00ns 119.59ms         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
      'fs_random_no_lp':         1 [ 97.88ms,  97.88ms]  97.88ms   0.00ns  97.88ms         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
        'graph_arc_lns':        75 [ 53.73ms,    8.59s] 853.25ms    1.22s    1.07m        74 [  5.25us, 102.69ms]  57.45ms  47.81ms    4.25s
        'graph_cst_lns':        75 [ 77.15ms,    9.04s]    3.42s    1.79s    4.28m        73 [ 10.00ns, 119.52ms]  57.94ms  47.97ms    4.23s
        'graph_dec_lns':        74 [ 78.88ms,    5.90s] 617.70ms 797.26ms   45.71s        74 [ 26.34us, 102.13ms]  58.24ms  46.35ms    4.31s
        'graph_var_lns':        75 [ 76.49ms,   10.89s]    3.73s    2.58s    4.66m        74 [ 10.00ns, 103.24ms]  59.60ms  45.91ms    4.41s
                   'ls':        74 [ 23.70ms,  87.64ms]  37.09ms  10.68ms    2.74s        74 [100.13ms, 101.20ms] 100.56ms 233.49us    7.44s
                   'ls':        74 [ 23.76ms,  65.95ms]  36.45ms   8.39ms    2.70s        74 [100.02ms, 101.10ms] 100.59ms 227.08us    7.44s
               'max_lp':         1 [   4.96m,    4.96m]    4.96m   0.00ns    4.96m         1 [   6.33m,    6.33m]    6.33m   0.00ns    6.33m
                'no_lp':         1 [   4.96m,    4.96m]    4.96m   0.00ns    4.96m         1 [   6.20m,    6.20m]    6.20m   0.00ns    6.20m
        'quick_restart':         1 [   4.96m,    4.96m]    4.96m   0.00ns    4.96m         1 [   2.59m,    2.59m]    2.59m   0.00ns    2.59m
  'quick_restart_no_lp':         1 [   4.97m,    4.97m]    4.97m   0.00ns    4.97m         1 [   2.66m,    2.66m]    2.66m   0.00ns    2.66m
        'reduced_costs':         1 [   4.97m,    4.97m]    4.97m   0.00ns    4.97m         1 [   6.37m,    6.37m]    6.37m   0.00ns    6.37m
            'rins/rens':        75 [ 23.76ms, 673.36ms] 156.84ms 114.75ms   11.76s        73 [ 10.00ns, 102.16ms]  60.72ms  49.01ms    4.43s
          'rnd_cst_lns':        75 [414.69ms,   11.65s]    2.54s    2.03s    3.17m        75 [265.34us, 102.24ms]  58.56ms  46.44ms    4.39s
          'rnd_var_lns':        75 [ 63.41ms,    6.36s] 510.29ms 928.44ms   38.27s        75 [ 20.66us, 102.32ms]  61.52ms  44.60ms    4.61s

Search stats                Bools  Conflicts     Branches   Restarts     BoolPropag  IntegerPropag
                 'core':  140'628    391'423   56'038'215    526'346  2'640'436'433    178'701'053
           'default_lp':   29'912  2'148'312    3'279'623     95'556     60'836'489    742'612'556
            'fs_random':   29'912          0       59'824     59'824         19'639         79'464
      'fs_random_no_lp':   29'912          0       43'648     43'648         17'862         61'511
               'max_lp':   29'912      5'102    4'129'515    758'623      2'224'373    140'791'076
                'no_lp':   29'912    521'975    7'444'312    229'847  1'129'059'430  2'256'760'256
        'quick_restart':   29'912    139'472  201'857'487    733'854    140'481'401    696'399'687
  'quick_restart_no_lp':   29'912    140'886  204'136'382    834'140    149'334'662    715'571'638
        'reduced_costs':   29'912      3'287    6'720'537  1'222'523      3'736'762    232'637'614

SAT stats                 ClassicMinim   LitRemoved     LitLearned  LitForgotten  Subsumed  MClauses  MDecisions  MLitTrue  MSubsumed  MLitRemoved  MReused
                 'core':       361'639  128'873'832    729'620'918   708'168'024       749    75'037   2'209'647         1        771      248'743   11'293
           'default_lp':        28'851       34'611  1'046'626'441   877'096'011   214'823        54     157'596         0          2          827       84
            'fs_random':             0            0              0             0         0         0           0         0          0            0        0
      'fs_random_no_lp':             0            0              0             0         0         0           0         0          0            0        0
               'max_lp':         4'864    2'127'975      4'922'063             0         4       898   3'140'775         0          2          827    2'358
                'no_lp':       233'319      518'014    100'059'472    84'301'996    41'121       248     752'033         0          2          827      195
        'quick_restart':        85'151    1'164'624     46'103'814    37'263'868     2'785     1'673   5'768'530         0          2          827    2'261
  'quick_restart_no_lp':        87'171    1'160'625     45'126'699    39'619'682     2'740     1'738   6'113'508         0          2          827    2'307
        'reduced_costs':         2'988    1'263'194      1'262'616             0         4     1'491   5'177'444         0          2          827    3'194

Lp stats            Component  Iterations  AddedCuts  OPTIMAL  DUAL_F.  DUAL_U.
         'max_lp':          1   1'934'584         33   15'154       78        4
  'reduced_costs':          1   1'610'060         33    8'197      179        0

Lp dimension                                                            Final dimension of first component
         'max_lp':  400 rows, 29912 columns, 114976 entries with magnitude in [1.000000e+00, 1.000000e+00]
  'reduced_costs':  436 rows, 29912 columns, 145467 entries with magnitude in [1.000000e+00, 1.000000e+00]

Lp debug            CutPropag  CutEqPropag  Adjust  Overflow    Bad  BadScaling
         'max_lp':          0            0  15'183         0  7'249           0
  'reduced_costs':          0            0   8'363         0  8'983           0

Lp pool             Constraints  Updates  Simplif  Merged  Shortened  Split  Strenghtened  Cuts/Call
         'max_lp':       10'295       60      420       0        143      0             3   33/1'294
  'reduced_costs':       10'295       54      559       0        142      0            14     33/802

Lp Cut           max_lp  reduced_costs
         CG_FF:       3              6
         CG_KL:       -              1
          CG_R:       2              2
        Clique:       1              1
      MIR_2_FF:      22             19
  ZERO_HALF_FF:       5              4

LNS stats           Improv/Calls  Closed  Difficulty  TimeLimit
  'graph_arc_lns':          0/74     49%        0.13       0.10
  'graph_cst_lns':          0/74     47%        0.10       0.10
  'graph_dec_lns':          0/74     49%        0.16       0.10
  'graph_var_lns':          1/74     47%        0.09       0.10
      'rins/rens':          0/73     40%        0.00       0.10
    'rnd_cst_lns':          1/75     48%        0.11       0.10
    'rnd_var_lns':          1/75     48%        0.12       0.10

LS stats                                Batches  Restarts/Perturbs  LinMoves  GenMoves  CompoundMoves  Bactracks  WeightUpdates  ScoreComputed
                         'fj_restart':        1                  1       167         0              0          0              3            847
                         'ls_restart':       16                  4     2'879         0              0          0            529        426'321
                'ls_restart_compound':       12                  8         0     1'874              2        928              1        185'490
        'ls_restart_compound_perturb':       26                 14         0     4'045             44      1'983             11        415'932
                   'ls_restart_decay':       17                 12     6'518         0              0          0            293        493'463
          'ls_restart_decay_compound':       35                 10         0     5'644             24      2'801              7        704'477
  'ls_restart_decay_compound_perturb':       11                  8         0     1'769              6        872              3        179'984
           'ls_restart_decay_perturb':       16                  8     6'283         0              0          0            232        465'608
                 'ls_restart_perturb':       15                 11     2'695         0              0          0            827        395'588

Solutions (10)            Num    Rank
           'fj_restart':    1   [2,2]
               'max_lp':    2  [8,10]
                'no_lp':    1   [1,1]
        'quick_restart':    1   [5,5]
  'quick_restart_no_lp':    3   [3,6]
        'reduced_costs':    2   [7,9]

Objective bounds     Num
    'am1_presolve':    1
       'bool_core':    2
  'initial_domain':    1
   'reduced_costs':    2

Solution repositories    Added  Queried  Synchro
  'feasible solutions':    272    1'177      270
        'lp solutions':  2'140       75      874
                'pump':      0        0

Improving bounds shared    Num
                'max_lp':   21
         'reduced_costs':  564

Clauses shared      Num
          'no_lp':    1
  'reduced_costs':    1

CpSolverResponse summary:
status: FEASIBLE
objective: 175
best_bound: 173
integers: 30086
booleans: 29912
conflicts: 0
branches: 43648
propagations: 17862
integer_propagations: 61511
restarts: 43648
lp_iterations: 0
walltime: 300.375
usertime: 300.375
deterministic_time: 2507.18
gap_integral: 1737.4
solution_fingerprint: 0x4be2241c498f8089

status: FEASIBLE
obj=175
bound=173
time=300.4
Selected possibility 245 : (2, [47, 48, 16, 131])
Selected possibility 351 : (2, [128, 129, 130, 123, 124, 125])
Selected possibility 583 : (2, [132, 139, 140, 473, 474, 475, 383, 384])
Selected possibility 609 : (2, [133, 38, 39, 316, 317, 191])
Selected possibility 1392 : (1, [374, 375, 380, 467, 373])
Selected possibility 2009 : (1, [403, 284, 285, 436])
Selected possibility 2063 : (1, [409, 410, 90, 91, 435])
Selected possibility 2416 : (1, [425, 179, 66, 444])
Selected possibility 2654 : (1, [445, 126, 127])
Selected possibility 2856 : (2, [120, 121, 122, 352, 353, 157])
Selected possibility 2948 : (2, [151, 152, 153, 154, 442, 443, 150])
Selected possibility 3022 : (2, [158, 159, 298, 117, 118, 146])
Selected possibility 3111 : (2, [221, 222, 223, 327, 239])
Selected possibility 3154 : (2, [229, 230, 320, 334, 335, 241])
Selected possibility 3174 : (2, [238, 3, 427, 399, 400, 401, 109])
Selected possibility 3264 : (2, [240, 215, 182, 235, 236, 247])
Selected possibility 3457 : (2, [248, 113, 217, 65, 177, 237])
Selected possibility 5234 : (2, [21, 22, 23, 24, 25, 26, 27, 49, 50, 446, 447])
Selected possibility 5775 : (2, [30, 31, 32, 430, 18, 144, 145])
Selected possibility 5890 : (1, [33, 34, 348, 349])
Selected possibility 6045 : (1, [55, 17, 222])
Selected possibility 6229 : (1, [63, 180, 249, 110])
Selected possibility 6595 : (1, [86, 242])
Selected possibility 6882 : (1, [92, 93, 312, 313])
Selected possibility 7178 : (1, [98, 99, 342, 343])
Selected possibility 7279 : (1, [100, 101, 51, 5])
Selected possibility 7854 : (2, [137, 138, 283, 414, 415])
Selected possibility 9025 : (1, [181, 281, 222])
Selected possibility 9261 : (1, [218, 251])
Selected possibility 9344 : (2, [220, 216, 245, 250, 211, 219])
Selected possibility 9946 : (1, [227, 176, 97])
Selected possibility 9963 : (1, [227, 228, 244])
Selected possibility 10652 : (1, [271, 276, 258, 278])
Selected possibility 10683 : (1, [275, 64, 102, 272])
Selected possibility 11076 : (1, [297, 359])
Selected possibility 11222 : (1, [323, 6, 421])
Selected possibility 11396 : (1, [323, 324, 325, 88, 89])
Selected possibility 11594 : (1, [328, 329, 326, 361])
Selected possibility 11812 : (1, [344, 345, 338, 347])
Selected possibility 11958 : (1, [350, 351, 209, 210])
Selected possibility 12129 : (1, [354, 355, 503, 366])
Selected possibility 12382 : (2, [364, 95, 96, 212, 213, 279])
Selected possibility 12492 : (2, [367, 339, 191, 404, 405, 280, 87])
Selected possibility 12645 : (1, [396, 397, 398, 430, 431, 432])
Selected possibility 13074 : (1, [416, 417, 418, 451, 452, 453])
Selected possibility 13297 : (2, [422, 423, 424, 286, 193, 194])
Selected possibility 14451 : (2, [448, 205, 287, 85])
Selected possibility 15198 : (1, [460, 332, 333, 330, 331])
Selected possibility 15910 : (2, [469, 470, 378, 261, 53, 54])
Selected possibility 16591 : (2, [473, 474, 475, 44, 292, 293])
Selected possibility 17876 : (2, [7, 200])
Selected possibility 18531 : (2, [52, 336, 341, 358, 198])
Selected possibility 18537 : (2, [69, 200])
Selected possibility 19939 : (2, [199, 70])
Selected possibility 20646 : (1, [289, 4])
Selected possibility 20667 : (2, [291, 479, 480, 195, 1])
Selected possibility 20668 : (2, [291, 479, 480, 196, 290])
Selected possibility 22385 : (2, [427, 19, 20, 460, 243, 79, 80])
Selected possibility 23777 : (1, [58, 288, 81, 82])
Selected possibility 23889 : (1, [67, 489, 430, 188, 189])
Selected possibility 24172 : (1, [77, 355, 309, 310, 311])
Selected possibility 25973 : (2, [83, 84, 480, 481, 482, 74])
Selected possibility 27079 : (2, [161, 162, 163, 164, 450])
Selected possibility 27539 : (2, [185, 505, 167, 76, 495, 500])
Selected possibility 30755 : (1, [256, 257, 426, 71, 72])
Selected possibility 30826 : (1, [294, 295, 296, 299, 300, 301])
Selected possibility 31065 : (2, [294, 490, 491, 492, 60, 502, 165, 166])
Selected possibility 31546 : (2, [301, 306, 190, 183, 184, 408, 255])
Selected possibility 32508 : (1, [307, 78, 352, 504])
Selected possibility 33189 : (1, [412, 413, 252, 253, 254])
Selected possibility 34017 : (2, [419, 420, 2, 119, 8, 9, 10])
Selected possibility 36506 : (1, [495, 500, 147, 148, 449, 450])
Selected possibility 38062 : (2, [173, 174, 175, 418, 428, 171, 172])
Selected possibility 38224 : (2, [411, 68, 438, 439])
Selected possibility 38381 : (1, [440, 441, 506, 62])
Selected possibility 39025 : (2, [29, 14, 15, 268, 269, 22, 23, 25])
Selected possibility 39076 : (2, [29, 134, 135, 136, 141, 142, 143, 21])
Selected possibility 39708 : (1, [43, 56, 28])
Selected possibility 40632 : (1, [263, 264, 382, 383])
Selected possibility 40831 : (1, [266, 267, 11])
Selected possibility 40832 : (1, [266, 267, 262, 263])
Selected possibility 41128 : (1, [273, 370, 393, 475])
Selected possibility 41195 : (1, [274, 433, 434, 42])
Selected possibility 41743 : (1, [375, 376, 377, 378])
Selected possibility 42314 : (1, [380, 381, 259, 260, 457])
Selected possibility 42365 : (2, [380, 467, 12, 13, 92, 224, 35, 36])
Selected possibility 42429 : (1, [380, 467, 468, 178, 101, 456, 457])
Selected possibility 43867 : (1, [458, 459, 460, 402, 403, 385, 386])
Selected possibility 44803 : (2, [470, 378, 379, 192, 283, 423, 390, 391])
Selected possibility 44972 : (2, [471, 472, 437, 149, 277, 251, 465, 466])
Selected possibility 45302 : (2, [477, 389, 46, 269, 270, 371, 372, 470, 378])
Selected possibility 45716 : (2, [61, 186, 187, 188, 306, 307])
Selected possibility 47884 : (1, [160, 103, 337, 493])
Selected possibility 48002 : (2, [202, 487, 488, 489, 500, 501, 502, 197])
Selected possibility 48276 : (1, [226, 360])
Selected possibility 48922 : (2, [308, 304, 305, 302, 303, 326])
Selected possibility 51821 : (2, [355, 45, 46, 463, 464, 363])
Selected possibility 53275 : (1, [365, 282])
Selected possibility 54596 : (1, [494, 495, 500, 506, 507])
Selected possibility 55670 : (2, [111, 112, 113, 114, 115, 116])
Selected possibility 55674 : (1, [40, 41])
Selected possibility 55759 : (2, [461, 462, 454, 455, 476, 477, 478])
Selected possibility 56143 : (2, [73, 74, 75, 168, 169, 170])
Selected possibility 56641 : (1, [94, 362, 314, 315])
Selected possibility 56703 : (2, [103, 104, 105, 206, 207, 208])
Selected possibility 56842 : (2, [155, 156, 406, 407, 496, 497])
Selected possibility 56964 : (2, [203, 204, 205, 106, 107, 108])
Selected possibility 57117 : (1, [225, 231])
Selected possibility 57149 : (2, [232, 233, 234, 246, 356, 357])
Selected possibility 57905 : (1, [318, 319, 340, 341])
Selected possibility 57921 : (2, [321, 322, 3, 201, 214])
Selected possibility 60232 : (2, [346, 483, 484, 485, 486, 99])
Selected possibility 61649 : (2, [498, 499, 428, 429, 57, 58, 59])
Selected possibility 62298 : (2, [265, 266, 386, 391, 471, 394, 395])
Selected possibility 62370 : (1, [368, 369, 466, 392])
Selected possibility 62959 : (2, [388, 389, 46, 269, 36, 37, 385, 386, 387])
```