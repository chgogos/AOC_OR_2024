# Day 7

## Description
Hi, DORothy here 🇺🇸

I'm the Chief Operations Officer of OptimizeLogistics, a complex transportation and distribution company from the USA facing a critical optimization challenge.

There are a lot of products that need to be served to our clients, and multiple ways of selecting them.

We usually get several subsets of products, calculate their associated cost (at a subset of products level), and finally select those subsets that minimize our costs.

Of course, all the products must be delivered just once, meaning that a product cannot appear in two different subsets.

I'll give you an example with 135 products and all the 51975 subsets we built with a cost.

Can you help me solve this problem?

## Problem's data

[instance.txt](./instance.txt)

## Solution

* [day7.py](./day7.py)

## Output
```
# products = 135
# subsets = 51975

Starting CP-SAT solver v9.11.4210
Parameters: max_time_in_seconds: 300 log_search_progress: true
Setting number of workers to 10

Initial optimization model '': (model_fingerprint: 0xaaf03d7ea94212ec)
#Variables: 51'975 (#bools: 51'975 in objective)
  - 51'975 Booleans in [0,1]
#kLinearN: 135 (#terms: 410'894)

Starting presolve at 0.01s
  1.84e-02s  0.00e+00d  [DetectDominanceRelations] 
  1.36e-02s  0.00e+00d  [DetectDominanceRelations] 
  1.36e-01s  0.00e+00d  [PresolveToFixPoint] #num_loops=4 #num_dual_strengthening=3 
  7.60e-04s  0.00e+00d  [ExtractEncodingFromLinear] #potential_supersets=135 
[Symmetry] Graph for symmetry has 52'110 nodes and 395'224 arcs.
[Symmetry] Symmetry computation done. time: 0.006212 dtime: 0.018232
  1.05e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  6.00e-01s  1.00e+00d *[Probe] #probed=1'024 #new_binary_clauses=4 
  2.28e-03s  0.00e+00d  [MaxClique] 
  1.39e-02s  0.00e+00d  [DetectDominanceRelations] 
  3.24e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  1.37e-02s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  9.34e-03s  0.00e+00d  [DetectDuplicateConstraints] 
  9.21e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  1.00e-06s  0.00e+00d  [DetectDominatedLinearConstraints] 
  1.00e-06s  0.00e+00d  [DetectDifferentVariables] 
  1.68e-02s  1.77e-03d  [ProcessSetPPC] #relevant_constraints=135 
  4.25e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  6.50e-01s  1.00e+00d *[FindBigAtMostOneAndLinearOverlap] 
  2.70e-03s  2.22e-03d  [FindBigVerticalLinearOverlap] 
  9.00e-06s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  3.44e-04s  0.00e+00d  [MergeClauses] 
  1.41e-02s  0.00e+00d  [DetectDominanceRelations] 
  3.02e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  1.38e-02s  0.00e+00d  [DetectDominanceRelations] 
  2.95e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
[Symmetry] Graph for symmetry has 52'110 nodes and 395'224 arcs.
[Symmetry] Symmetry computation done. time: 0.006965 dtime: 0.0182321
  9.30e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  6.41e-01s  1.00e+00d *[Probe] #probed=1'024 #new_binary_clauses=4 
  3.15e-03s  0.00e+00d  [MaxClique] 
  1.43e-02s  0.00e+00d  [DetectDominanceRelations] 
  2.97e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  1.23e-02s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  9.69e-03s  0.00e+00d  [DetectDuplicateConstraints] 
  9.28e-03s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  1.00e-06s  0.00e+00d  [DetectDominatedLinearConstraints] 
  1.00e-06s  0.00e+00d  [DetectDifferentVariables] 
  1.69e-02s  1.77e-03d  [ProcessSetPPC] #relevant_constraints=135 
  3.53e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  6.52e-01s  1.00e+00d *[FindBigAtMostOneAndLinearOverlap] 
  2.56e-03s  2.22e-03d  [FindBigVerticalLinearOverlap] 
  1.10e-05s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  4.92e-04s  0.00e+00d  [MergeClauses] 
  1.42e-02s  0.00e+00d  [DetectDominanceRelations] 
  2.98e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  4.47e-01s  0.00e+00d  [ExpandObjective] #entries=100'002'058 #tight_variables=67'513 #tight_constraints=49 

Presolve summary:
  - 0 affine relations were detected.
  - rule 'TODO dual: only one unspecified blocking constraint?' was applied 16 times.
  - rule 'at_most_one: removed literals' was applied 30 times.
  - rule 'domination: in at most one' was applied 226 times.
  - rule 'domination: in exactly one' was applied 1'946 times.
  - rule 'dual: fix variable' was applied 1 time.
  - rule 'exactly_one: removed literals' was applied 134 times.
  - rule 'exactly_one: simplified objective' was applied 65 times.
  - rule 'exactly_one: singleton' was applied 30 times.
  - rule 'linear: positive equal one' was applied 135 times.
  - rule 'objective: shifted cost with exactly ones' was applied 60 times.
  - rule 'presolve: 2173 unused variables removed.' was applied 1 time.
  - rule 'presolve: iteration' was applied 2 times.

Presolved optimization model '': (model_fingerprint: 0x208cfba66677b20b)
#Variables: 49'772 (#bools: 49'700 in objective)
  - 49'772 Booleans in [0,1]
#kAtMostOne: 30 (#literals: 13'311)
#kExactlyOne: 105 (#literals: 381'913)

Preloading model.
#Bound   3.57s best:inf   next:[94752,292499604] initial_domain
[Symmetry] Graph for symmetry has 49'907 nodes and 395'224 arcs.
[Symmetry] Symmetry computation done. time: 0.006851 dtime: 0.0179686
#Model   3.59s var:49772/49772 constraints:135/135

Starting search at 3.59s with 10 workers.
7 full problem subsolvers: [core, default_lp, max_lp, no_lp, quick_restart, quick_restart_no_lp, reduced_costs]
3 first solution subsolvers: [fj, fs_random, fs_random_no_lp]
10 interleaved subsolvers: [feasibility_pump, graph_arc_lns, graph_cst_lns, graph_dec_lns, graph_var_lns, ls(2), rins/rens, rnd_cst_lns, rnd_var_lns]
3 helper subsolvers: [neighborhood_helper, synchronization_agent, update_gap_integral]

#Bound   4.94s best:inf   next:[94872,292499604] am1_presolve (num_literals=49700 num_am1=2 increase=40 work_done=221084)
#Model   5.10s var:49771/49772 constraints:135/135
#1       5.11s best:189624 next:[94872,189621] fs_random_no_lp (fixed_bools=1/49772)
#Bound   5.12s best:189624 next:[94914,189621] default_lp
#Bound   5.20s best:189624 next:[114852,189621] max_lp
#Model   5.20s var:49770/49772 constraints:135/135
#2       5.31s best:182979 next:[114852,182976] rnd_var_lns (d=0.50 s=16 t=0.10 p=0.00 stall=0 h=auto_l0)
#3       5.42s best:170436 next:[114852,170433] rnd_cst_lns (d=0.50 s=17 t=0.10 p=0.00 stall=0 h=auto_l0)
#4       5.48s best:114852 next:[]         max_lp (fixed_bools=2/49772)
#Done    5.48s max_lp

Task timing                      n [     min,      max]      avg      dev     time         n [     min,      max]      avg      dev    dtime
                 'core':         1 [   2.03s,    2.03s]    2.03s   0.00ns    2.03s         1 [947.06ms, 947.06ms] 947.06ms   0.00ns 947.06ms
           'default_lp':         1 [   1.96s,    1.96s]    1.96s   0.00ns    1.96s         1 [344.65ms, 344.65ms] 344.65ms   0.00ns 344.65ms
     'feasibility_pump':         3 [ 11.17ms, 110.36ms]  57.47ms  40.76ms 172.40ms         2 [  2.37ms,   3.21ms]   2.79ms 419.30us   5.59ms
                   'fj':         2 [ 42.16ms,  93.97ms]  68.07ms  25.90ms 136.14ms         2 [111.55ms, 111.91ms] 111.73ms 181.67us 223.46ms
            'fs_random':         1 [   1.59s,    1.59s]    1.59s   0.00ns    1.59s         1 [ 20.00ns,  20.00ns]  20.00ns   0.00ns  20.00ns
      'fs_random_no_lp':         1 [   1.52s,    1.52s]    1.52s   0.00ns    1.52s         1 [ 33.88ms,  33.88ms]  33.88ms   0.00ns  33.88ms
        'graph_arc_lns':         1 [212.05ms, 212.05ms] 212.05ms   0.00ns 212.05ms         1 [  2.07us,   2.07us]   2.07us   0.00ns   2.07us
        'graph_cst_lns':         1 [183.12ms, 183.12ms] 183.12ms   0.00ns 183.12ms         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
        'graph_dec_lns':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
        'graph_var_lns':         1 [257.84ms, 257.84ms] 257.84ms   0.00ns 257.84ms         1 [702.00ns, 702.00ns] 702.00ns   0.00ns 702.00ns
                   'ls':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                   'ls':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
               'max_lp':         1 [   1.88s,    1.88s]    1.88s   0.00ns    1.88s         1 [ 14.66ms,  14.66ms]  14.66ms   0.00ns  14.66ms
                'no_lp':         1 [   1.96s,    1.96s]    1.96s   0.00ns    1.96s         1 [419.93ms, 419.93ms] 419.93ms   0.00ns 419.93ms
        'quick_restart':         1 [   1.96s,    1.96s]    1.96s   0.00ns    1.96s         1 [235.23ms, 235.23ms] 235.23ms   0.00ns 235.23ms
  'quick_restart_no_lp':         1 [   1.96s,    1.96s]    1.96s   0.00ns    1.96s         1 [519.09ms, 519.09ms] 519.09ms   0.00ns 519.09ms
        'reduced_costs':         1 [   1.96s,    1.96s]    1.96s   0.00ns    1.96s         1 [ 25.54ms,  25.54ms]  25.54ms   0.00ns  25.54ms
            'rins/rens':         2 [236.54ms,    1.15s] 692.86ms 456.32ms    1.39s         2 [ 21.95ms, 100.19ms]  61.07ms  39.12ms 122.13ms
          'rnd_cst_lns':         1 [231.18ms, 231.18ms] 231.18ms   0.00ns 231.18ms         1 [  2.49ms,   2.49ms]   2.49ms   0.00ns   2.49ms
          'rnd_var_lns':         1 [201.13ms, 201.13ms] 201.13ms   0.00ns 201.13ms         1 [226.54us, 226.54us] 226.54us   0.00ns 226.54us

Search stats               Bools  Conflicts  Branches  Restarts  BoolPropag  IntegerPropag
                 'core':  49'774        396   254'282    50'748  12'048'701     11'935'923
           'default_lp':  49'772         50    69'231    50'737  11'224'439     11'047'869
            'fs_random':  49'772          0     1'008     1'008   9'739'130      9'735'540
      'fs_random_no_lp':  49'772         36     1'111     1'009   9'819'996      9'800'239
               'max_lp':  49'772          0     1'390     1'009   9'788'520      9'793'038
                'no_lp':  49'772         50    67'856    50'872  11'995'792     11'940'984
        'quick_restart':  49'772         10    46'395    46'326  10'092'135     10'149'564
  'quick_restart_no_lp':  49'772         10    54'145    50'921  12'934'544     12'974'350
        'reduced_costs':  49'772          0     1'008     1'008   9'739'130      9'740'142

SAT stats                 ClassicMinim  LitRemoved  LitLearned  LitForgotten  Subsumed  MClauses  MDecisions  MLitTrue  MSubsumed  MLitRemoved  MReused
                 'core':             1           1     830'076             0         0         0           0         0          0            0        0
           'default_lp':             0           0      27'895             0         0         0           0         0          0            0        0
            'fs_random':             0           0           0             0         0         0           0         0          0            0        0
      'fs_random_no_lp':             0           0      68'360             0         0         0           0         0          0            0        0
               'max_lp':             0           0           0             0         0         0           0         0          0            0        0
                'no_lp':             0           0      38'716             0         0         0           0         0          0            0        0
        'quick_restart':             0           0      40'725             0         0         0           0         0          0            0        0
  'quick_restart_no_lp':             0           0       9'470             0         0         0           0         0          0            0        0
        'reduced_costs':             0           0           0             0         0         0           0         0          0            0        0

Lp stats            Component  Iterations  AddedCuts  OPTIMAL  DUAL_F.  DUAL_U.
     'default_lp':          1           5          0        9        0        0
      'fs_random':          1           0          0        0        0        0
         'max_lp':          1          39          0        5        0        0
  'quick_restart':          1           6          0       26        0        0
  'reduced_costs':          1          91          0        7        0        0

Lp dimension                                                            Final dimension of first component
     'default_lp':      3 rows, 49700 columns, 3849 entries with magnitude in [1.000000e+00, 1.000000e+00]
      'fs_random':         0 rows, 49700 columns, 0 entries with magnitude in [0.000000e+00, 0.000000e+00]
         'max_lp':  135 rows, 49772 columns, 395224 entries with magnitude in [1.000000e+00, 1.000000e+00]
  'quick_restart':      3 rows, 49700 columns, 3849 entries with magnitude in [1.000000e+00, 1.000000e+00]
  'reduced_costs':   91 rows, 49772 columns, 330809 entries with magnitude in [1.000000e+00, 1.000000e+00]

Lp debug            CutPropag  CutEqPropag  Adjust  Overflow  Bad  BadScaling
     'default_lp':          0            0       0         0    0           0
      'fs_random':          0            0       0         0    0           0
         'max_lp':          0            0       5         0    0           0
  'quick_restart':          0            0       1         0    0           0
  'reduced_costs':          0            0       4         0    0           0

Lp pool             Constraints  Updates  Simplif  Merged  Shortened  Split  Strenghtened  Cuts/Call
     'default_lp':          135        0       13       0         13      0             0        0/0
      'fs_random':          135        0        0       0          0      0             0        0/0
         'max_lp':          135        0        0       0          0      0             0        0/0
  'quick_restart':          135        0       13       0         13      0             0        0/0
  'reduced_costs':          135        0        0       0          0      0             0        0/0

LNS stats           Improv/Calls  Closed  Difficulty  TimeLimit
  'graph_arc_lns':           0/1    100%        0.71       0.10
  'graph_cst_lns':           0/0      0%        0.50       0.10
  'graph_dec_lns':           0/0      0%        0.50       0.10
  'graph_var_lns':           1/1    100%        0.71       0.10
      'rins/rens':           2/2     50%        0.54       0.10
    'rnd_cst_lns':           1/1    100%        0.71       0.10
    'rnd_var_lns':           1/1    100%        0.71       0.10

LS stats                           Batches  Restarts/Perturbs  LinMoves  GenMoves  CompoundMoves  Bactracks  WeightUpdates  ScoreComputed
                    'fj_restart':        1                  1       212         0              0          0             63         49'771
  'fj_restart_decay_perturb_obj':        1                  1       696         0              0          0             21         49'772

Solutions (4)         Num   Rank
  'fs_random_no_lp':    1  [1,1]
           'max_lp':    1  [4,4]
      'rnd_cst_lns':    1  [3,3]
      'rnd_var_lns':    1  [2,2]

Objective bounds     Num
    'am1_presolve':    1
      'default_lp':    1
  'initial_domain':    1
          'max_lp':    1

Solution repositories    Added  Queried  Synchro
  'feasible solutions':      5       10        4
        'lp solutions':      3        0        1
                'pump':      2        2

Improving bounds shared    Num
                  'core':    2

Clauses shared            Num
                 'core':   20
      'fs_random_no_lp':    1
  'quick_restart_no_lp':    7

CpSolverResponse summary:
status: OPTIMAL
objective: 114852
best_bound: 114852
integers: 49924
booleans: 49772
conflicts: 36
branches: 1111
propagations: 9819996
integer_propagations: 9800239
restarts: 1009
lp_iterations: 0
walltime: 5.64853
usertime: 5.64853
deterministic_time: 6.90552
gap_integral: 6.86811
solution_fingerprint: 0xd8fb15d636375174

status: OPTIMAL
obj=114,852
bound=114,852
time=5.6
Selected subset 4 : (972, [1])
Selected subset 14 : (972, [2])
Selected subset 33 : (972, [3])
Selected subset 59 : (972, [4])
Selected subset 82 : (1617, [5, 60, 76])
Selected subset 196 : (972, [6])
Selected subset 281 : (972, [7])
Selected subset 410 : (2364, [8])
Selected subset 614 : (2364, [9])
Selected subset 823 : (2130, [10])
Selected subset 946 : (2529, [11, 64, 80])
Selected subset 1267 : (3099, [12])
Selected subset 1502 : (1455, [13])
Selected subset 1626 : (5460, [14, 59])
Selected subset 2042 : (2364, [15])
Selected subset 2328 : (687, [16])
Selected subset 2393 : (11937, [17, 27, 107, 121])
Selected subset 3203 : (2364, [18])
Selected subset 3671 : (2130, [19])
Selected subset 4118 : (768, [20, 127])
Selected subset 4604 : (2364, [21, 129])
Selected subset 5082 : (1455, [22])
Selected subset 5604 : (1455, [23])
Selected subset 6176 : (1455, [24])
Selected subset 6749 : (2130, [25])
Selected subset 7303 : (687, [26])
Selected subset 8502 : (1455, [28])
Selected subset 9140 : (687, [29])
Selected subset 9673 : (1293, [30, 96])
Selected subset 10499 : (1338, [31, 123])
Selected subset 10663 : (2490, [32, 45, 55, 103])
Selected subset 11757 : (1455, [33])
Selected subset 12499 : (723, [34, 100])
Selected subset 13251 : (543, [35])
Selected subset 13817 : (9537, [36, 66, 117])
Selected subset 14420 : (1035, [37, 69])
Selected subset 14992 : (2130, [38, 43])
Selected subset 16403 : (342, [39])
Selected subset 17256 : (1416, [40, 116])
Selected subset 18198 : (2364, [41, 97, 132])
Selected subset 19048 : (1455, [42])
Selected subset 20793 : (936, [44, 113])
Selected subset 22295 : (687, [46, 67])
Selected subset 23020 : (378, [47, 72])
Selected subset 23951 : (2424, [48, 104, 128])
Selected subset 24175 : (2322, [49, 58, 122, 125])
Selected subset 25353 : (642, [50, 88, 112])
Selected subset 26359 : (1116, [51, 73])
Selected subset 27097 : (1236, [52, 68])
Selected subset 28019 : (1293, [53, 95])
Selected subset 29316 : (1293, [54, 119])
Selected subset 30391 : (354, [56, 77])
Selected subset 31323 : (354, [57, 93])
Selected subset 33998 : (1509, [61, 70, 108, 114])
Selected subset 35207 : (414, [62, 82])
Selected subset 35715 : (408, [63, 79])
Selected subset 36939 : (1449, [65, 126, 134])
Selected subset 39784 : (1392, [71, 75, 105])
Selected subset 41173 : (687, [74, 87])
Selected subset 43352 : (2628, [78, 83])
Selected subset 44241 : (1875, [81, 101])
Selected subset 45364 : (1119, [84, 102])
Selected subset 45744 : (354, [85, 86])
Selected subset 46771 : (378, [89, 91])
Selected subset 47033 : (642, [90, 99, 109, 115])
Selected subset 47663 : (378, [92, 106])
Selected subset 48339 : (354, [94, 98])
Selected subset 51723 : (1293, [110, 120])
Selected subset 51800 : (1515, [111, 118, 133])
Selected subset 51966 : (282, [124, 135])
Selected subset 51973 : (231, [130, 131])
```