# Day 1

## Description
Hi, I'm ÉléonORe, and I'm struggling to organize a series of events...

Each event requires a dedicated room.

Some events have overlapping participants, so I can't schedule them in the same room at the same time.

How many rooms do I need? How can I assign each event to a room so that no two overlapping events are scheduled in the same one?

Ideally, I want to minimize the total number of rooms used.

Can you help me solve this problem?

## Problem's data

[instance.txt](./instance.txt)

## Solution 

[day1.py](./day1.py)

## Output
```
number_of_events=100, number_of_conflicts=2487
{1: e1(1..100), 2: e2(1..100), 3: e3(1..100), 4: e4(1..100), 5: e5(1..100), 6: e6(1..100), 7: e7(1..100), 8: e8(1..100), 9: e9(1..100), 10: e10(1..100), 11: e11(1..100), 12: e12(1..100), 13: e13(1..100), 14: e14(1..100), 15: e15(1..100), 16: e16(1..100), 17: e17(1..100), 18: e18(1..100), 19: e19(1..100), 20: e20(1..100), 21: e21(1..100), 22: e22(1..100), 23: e23(1..100), 24: e24(1..100), 25: e25(1..100), 26: e26(1..100), 27: e27(1..100), 28: e28(1..100), 29: e29(1..100), 30: e30(1..100), 31: e31(1..100), 32: e32(1..100), 33: e33(1..100), 34: e34(1..100), 35: e35(1..100), 36: e36(1..100), 37: e37(1..100), 38: e38(1..100), 39: e39(1..100), 40: e40(1..100), 41: e41(1..100), 42: e42(1..100), 43: e43(1..100), 44: e44(1..100), 45: e45(1..100), 46: e46(1..100), 47: e47(1..100), 48: e48(1..100), 49: e49(1..100), 50: e50(1..100), 51: e51(1..100), 52: e52(1..100), 53: e53(1..100), 54: e54(1..100), 55: e55(1..100), 56: e56(1..100), 57: e57(1..100), 58: e58(1..100), 59: e59(1..100), 60: e60(1..100), 61: e61(1..100), 62: e62(1..100), 63: e63(1..100), 64: e64(1..100), 65: e65(1..100), 66: e66(1..100), 67: e67(1..100), 68: e68(1..100), 69: e69(1..100), 70: e70(1..100), 71: e71(1..100), 72: e72(1..100), 73: e73(1..100), 74: e74(1..100), 75: e75(1..100), 76: e76(1..100), 77: e77(1..100), 78: e78(1..100), 79: e79(1..100), 80: e80(1..100), 81: e81(1..100), 82: e82(1..100), 83: e83(1..100), 84: e84(1..100), 85: e85(1..100), 86: e86(1..100), 87: e87(1..100), 88: e88(1..100), 89: e89(1..100), 90: e90(1..100), 91: e91(1..100), 92: e92(1..100), 93: e93(1..100), 94: e94(1..100), 95: e95(1..100), 96: e96(1..100), 97: e97(1..100), 98: e98(1..100), 99: e99(1..100), 100: e100(1..100)}

Starting CP-SAT solver v9.11.4210
Parameters: max_time_in_seconds: 60 log_search_progress: true
Setting number of workers to 10

Initial optimization model '': (model_fingerprint: 0xae61ad1f534a2952)
#Variables: 101 (#ints: 1 in objective)
  - 1 in [0,100]
  - 100 in [1,100]
#kLinMax: 1 (#expressions: 100)
#kLinear2: 2'487 (#complex_domain: 2'487)

Starting presolve at 0.00s
  2.77e-04s  0.00e+00d  [DetectDominanceRelations] 
  4.75e-03s  0.00e+00d  [PresolveToFixPoint] #num_loops=2 #num_dual_strengthening=1 
  1.67e-04s  0.00e+00d  [ExtractEncodingFromLinear] 
[Symmetry] Graph for symmetry has 2'786 nodes and 5'272 arcs.
[Symmetry] Symmetry computation done. time: 0.000281 dtime: 0.00071115
  1.75e-04s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  1.22e-02s  3.55e-03d  [Probe] #probed=4'974 #new_bounds=1 
  4.00e-05s  0.00e+00d  [MaxClique] 
  1.44e-04s  0.00e+00d  [DetectDominanceRelations] 
  1.47e-03s  0.00e+00d  [PresolveToFixPoint] #num_loops=2 #num_dual_strengthening=1 
  5.32e-04s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  4.10e-05s  0.00e+00d  [DetectDuplicateConstraints] 
  4.50e-05s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  3.00e-04s  1.82e-05d  [DetectDominatedLinearConstraints] #relevant_constraints=2'587 
  9.18e-04s  0.00e+00d  [DetectDifferentVariables] #different=2'487 #cliques=46 #size=300 
  1.50e-05s  0.00e+00d  [ProcessSetPPC] 
  1.61e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  2.00e-06s  0.00e+00d  [FindBigAtMostOneAndLinearOverlap] 
  4.85e-04s  1.31e-04d  [FindBigVerticalLinearOverlap] 
  5.00e-06s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  5.00e-06s  0.00e+00d  [MergeClauses] 
  1.51e-04s  0.00e+00d  [DetectDominanceRelations] 
  1.74e-03s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  1.31e-04s  0.00e+00d  [DetectDominanceRelations] 
  1.43e-03s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
[Symmetry] Graph for symmetry has 2'932 nodes and 5'672 arcs.
[Symmetry] Symmetry computation done. time: 0.000247 dtime: 0.0007465
  1.22e-04s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  1.41e-02s  3.85e-03d  [Probe] #probed=4'974 
  1.30e-05s  0.00e+00d  [MaxClique] 
  1.50e-04s  0.00e+00d  [DetectDominanceRelations] 
  1.62e-03s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  4.72e-04s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  9.80e-05s  0.00e+00d  [DetectDuplicateConstraints] 
  1.01e-04s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.76e-04s  1.82e-05d  [DetectDominatedLinearConstraints] #relevant_constraints=2'587 
  3.82e-04s  0.00e+00d  [DetectDifferentVariables] 
  9.00e-06s  0.00e+00d  [ProcessSetPPC] 
  8.00e-06s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  3.00e-06s  0.00e+00d  [FindBigAtMostOneAndLinearOverlap] 
  3.28e-04s  1.31e-04d  [FindBigVerticalLinearOverlap] 
  1.80e-05s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  6.00e-06s  0.00e+00d  [MergeClauses] 
  1.47e-04s  0.00e+00d  [DetectDominanceRelations] 
  1.55e-03s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  1.00e-05s  0.00e+00d  [ExpandObjective] 

Presolve summary:
  - 0 affine relations were detected.
  - rule 'TODO dual: only one unspecified blocking constraint?' was applied 6 times.
  - rule 'all_diff: inferred from x != y constraints' was applied 46 times.
  - rule 'lin_max: rewrite with precedences' was applied 1 time.
  - rule 'lin_max: target domain reduced' was applied 1 time.
  - rule 'linear: expanded complex rhs' was applied 2'487 times.
  - rule 'linear: simplified rhs' was applied 2'587 times.
  - rule 'presolve: 0 unused variables removed.' was applied 1 time.
  - rule 'presolve: iteration' was applied 2 times.

Presolved optimization model '': (model_fingerprint: 0xc5267e7b3477e9d2)
#Variables: 2'588 (#ints: 1 in objective)
  - 2'487 Booleans in [0,1]
  - 100 in [1,100]
  - 1 in [2,100]
#kAllDiff: 46
#kLinear2: 5'074 (#enforced: 4'974)

Preloading model.
#Bound   0.06s best:inf   next:[2,100]    initial_domain
[Symmetry] Graph for symmetry has 10'393 nodes and 18'107 arcs.
[Symmetry] Symmetry computation done. time: 0.000874 dtime: 0.00290338
#Model   0.07s var:2588/2588 constraints:5120/5120

Starting search at 0.07s with 10 workers.
7 full problem subsolvers: [default_lp, max_lp, no_lp, pseudo_costs, quick_restart, quick_restart_no_lp, reduced_costs]
3 first solution subsolvers: [fj, fs_random, fs_random_no_lp]
10 interleaved subsolvers: [feasibility_pump, graph_arc_lns, graph_cst_lns, graph_dec_lns, graph_var_lns, ls(2), rins/rens, rnd_cst_lns, rnd_var_lns]
3 helper subsolvers: [neighborhood_helper, synchronization_agent, update_gap_integral]

#1       0.09s best:62    next:[2,61]     no_lp (fixed_bools=0/2512)
#2       0.10s best:61    next:[2,60]     quick_restart_no_lp (fixed_bools=0/2527)
#3       0.12s best:60    next:[2,59]     no_lp (fixed_bools=3/2513)
#4       0.12s best:59    next:[2,58]     no_lp (fixed_bools=3/2513)
#5       0.12s best:58    next:[2,57]     no_lp (fixed_bools=5/2513)
#6       0.12s best:57    next:[2,56]     no_lp (fixed_bools=5/2514)
#7       0.13s best:56    next:[2,55]     no_lp (fixed_bools=5/2515)
#8       0.13s best:55    next:[2,54]     no_lp (fixed_bools=6/2515)
#9       0.13s best:54    next:[2,53]     no_lp (fixed_bools=7/2516)
#10      0.13s best:53    next:[2,52]     no_lp (fixed_bools=8/2516)
#11      0.14s best:52    next:[2,51]     no_lp (fixed_bools=10/2516)
#12      0.14s best:51    next:[2,50]     no_lp (fixed_bools=11/2517)
#13      0.14s best:50    next:[2,49]     no_lp (fixed_bools=12/2519)
#14      0.14s best:49    next:[2,48]     no_lp (fixed_bools=12/2520)
#15      0.15s best:48    next:[2,47]     no_lp (fixed_bools=13/2521)
#16      0.15s best:47    next:[2,46]     no_lp (fixed_bools=13/2522)
#17      0.15s best:46    next:[2,45]     quick_restart (fixed_bools=17/2616)
#18      0.17s best:45    next:[2,44]     default_lp (fixed_bools=10/2587)
#19      0.17s best:44    next:[2,43]     default_lp (fixed_bools=12/2605)
#20      0.18s best:43    next:[2,42]     no_lp (fixed_bools=17/2524)
#21      0.18s best:42    next:[2,41]     no_lp (fixed_bools=19/2525)
#22      0.18s best:41    next:[2,40]     no_lp (fixed_bools=20/2528)
#23      0.18s best:40    next:[2,39]     no_lp (fixed_bools=21/2530)
#24      0.19s best:39    next:[2,38]     no_lp (fixed_bools=22/2531)
#25      0.19s best:38    next:[2,37]     no_lp (fixed_bools=23/2531)
#26      0.19s best:37    next:[2,36]     no_lp (fixed_bools=23/2531)
#27      0.19s best:36    next:[2,35]     no_lp (fixed_bools=23/2531)
#28      0.20s best:35    next:[2,34]     no_lp (fixed_bools=24/2532)
#29      0.21s best:34    next:[2,33]     no_lp (fixed_bools=26/2532)
#30      0.21s best:33    next:[2,32]     no_lp (fixed_bools=27/2533)
#31      0.21s best:32    next:[2,31]     no_lp (fixed_bools=28/2537)
#32      0.22s best:31    next:[2,30]     no_lp (fixed_bools=28/2541)
#33      0.22s best:30    next:[2,29]     no_lp (fixed_bools=28/2542)
#34      0.22s best:29    next:[2,28]     no_lp (fixed_bools=29/2543)
#35      0.22s best:28    next:[2,27]     no_lp (fixed_bools=32/2545)
#36      0.23s best:27    next:[2,26]     no_lp (fixed_bools=33/2548)
#37      0.24s best:26    next:[2,25]     quick_restart_no_lp (fixed_bools=77/2636)
#38      0.25s best:25    next:[2,24]     default_lp (fixed_bools=24/2731)
#39      0.26s best:24    next:[2,23]     default_lp (fixed_bools=24/2747)
#40      0.26s best:23    next:[2,22]     no_lp (fixed_bools=39/2550)
#41      0.26s best:22    next:[2,21]     no_lp (fixed_bools=40/2550)
#42      0.27s best:21    next:[2,20]     quick_restart_no_lp (fixed_bools=93/2658)
#43      0.27s best:20    next:[2,19]     default_lp (fixed_bools=30/2771)
#44      0.27s best:19    next:[2,18]     default_lp (fixed_bools=37/2771)
#45      0.28s best:18    next:[2,17]     default_lp (fixed_bools=38/2773)
#Bound   0.47s best:18    next:[3,17]     pseudo_costs
#Bound   0.51s best:18    next:[4,17]     reduced_costs
#Bound   0.70s best:18    next:[5,17]     reduced_costs
#Bound   0.86s best:18    next:[6,17]     reduced_costs
#Bound   0.98s best:18    next:[7,17]     reduced_costs
#Bound   1.15s best:18    next:[8,17]     reduced_costs
#46      1.34s best:17    next:[8,16]     default_lp (fixed_bools=40/2795)
#47      4.40s best:16    next:[8,15]     pseudo_costs (fixed_bools=0/2487)

Task timing                      n [     min,      max]      avg      dev     time         n [     min,      max]      avg      dev    dtime
           'default_lp':         1 [   1.00m,    1.00m]    1.00m   0.00ns    1.00m         1 [  19.21s,   19.21s]   19.21s   0.00ns   19.21s
     'feasibility_pump':        99 [  9.00us,   6.43ms] 160.91us 649.43us  15.93ms        96 [ 13.90us,  78.32us]  14.57us   6.54us   1.40ms
                   'fj':         1 [ 54.71ms,  54.71ms]  54.71ms   0.00ns  54.71ms         1 [100.26ms, 100.26ms] 100.26ms   0.00ns 100.26ms
            'fs_random':         1 [ 27.17ms,  27.17ms]  27.17ms   0.00ns  27.17ms         1 [ 20.00ns,  20.00ns]  20.00ns   0.00ns  20.00ns
      'fs_random_no_lp':         1 [ 25.99ms,  25.99ms]  25.99ms   0.00ns  25.99ms         1 [  1.55ms,   1.55ms]   1.55ms   0.00ns   1.55ms
        'graph_arc_lns':        99 [  9.83ms, 473.38ms] 279.77ms 115.19ms   27.70s        97 [ 17.99us, 100.46ms]  66.70ms  38.37ms    6.47s
        'graph_cst_lns':        99 [ 42.70ms, 688.78ms] 275.73ms 126.10ms   27.30s        98 [798.15us, 100.78ms]  62.82ms  41.01ms    6.16s
        'graph_dec_lns':        99 [ 11.56ms, 511.11ms] 282.77ms 119.08ms   27.99s        96 [ 45.63us, 100.52ms]  67.37ms  37.70ms    6.47s
        'graph_var_lns':        99 [ 10.93ms, 761.30ms] 260.19ms 171.99ms   25.76s        76 [190.61us, 101.01ms]  71.35ms  41.67ms    5.42s
                   'ls':        99 [ 32.51ms, 127.02ms]  51.61ms  11.41ms    5.11s        99 [100.00ms, 100.51ms] 100.07ms  93.58us    9.91s
                   'ls':        99 [ 38.40ms, 113.96ms]  52.51ms   9.54ms    5.20s        99 [100.00ms, 100.49ms] 100.07ms  94.06us    9.91s
               'max_lp':         1 [  59.93s,   59.93s]   59.93s   0.00ns   59.93s         1 [  22.42s,   22.42s]   22.42s   0.00ns   22.42s
                'no_lp':         1 [   1.00m,    1.00m]    1.00m   0.00ns    1.00m         1 [  20.44s,   20.44s]   20.44s   0.00ns   20.44s
         'pseudo_costs':         1 [  59.93s,   59.93s]   59.93s   0.00ns   59.93s         1 [  22.07s,   22.07s]   22.07s   0.00ns   22.07s
        'quick_restart':         1 [   1.00m,    1.00m]    1.00m   0.00ns    1.00m         1 [  21.39s,   21.39s]   21.39s   0.00ns   21.39s
  'quick_restart_no_lp':         1 [   1.00m,    1.00m]    1.00m   0.00ns    1.00m         1 [  24.72s,   24.72s]   24.72s   0.00ns   24.72s
        'reduced_costs':         1 [  59.93s,   59.93s]   59.93s   0.00ns   59.93s         1 [  30.57s,   30.57s]   30.57s   0.00ns   30.57s
            'rins/rens':       100 [413.00us, 495.19ms] 162.45ms 157.44ms   16.24s        57 [ 12.33us, 100.44ms]  75.79ms  39.51ms    4.32s
          'rnd_cst_lns':        99 [ 33.29ms, 504.11ms] 277.51ms 119.95ms   27.47s        97 [ 48.91us, 100.78ms]  64.50ms  39.59ms    6.26s
          'rnd_var_lns':       100 [  1.07ms, 542.38ms] 164.25ms 185.25ms   16.42s        47 [  5.09us, 100.48ms]  74.76ms  39.92ms    3.51s

Search stats              Bools  Conflicts   Branches  Restarts  BoolPropag  IntegerPropag
           'default_lp':  2'837     64'628    299'132    92'249  69'061'935     28'730'230
            'fs_random':  2'487          0      2'698     2'698           0          5'396
      'fs_random_no_lp':  2'487          0      7'227     4'974           8         14'174
               'max_lp':  2'487     37'088    340'635   293'698  37'831'833     52'643'182
                'no_lp':  2'551     63'467    386'481   253'114  67'237'092     26'066'199
         'pseudo_costs':  2'487     37'681    203'180   154'287  38'236'125     52'792'936
        'quick_restart':  3'067     59'286  2'040'884   194'707  53'449'520     22'818'191
  'quick_restart_no_lp':  3'072     65'592  2'242'692   210'927  59'655'907     26'075'434
        'reduced_costs':  2'492     27'218  1'139'416   842'738  21'913'165     34'867'665

SAT stats                 ClassicMinim  LitRemoved  LitLearned  LitForgotten  Subsumed  MClauses  MDecisions  MLitTrue  MSubsumed  MLitRemoved  MReused
           'default_lp':        57'100     868'987   5'093'342     3'971'952        91     3'517      52'583         0         31          240      814
            'fs_random':             0           0           0             0         0         0           0         0          0            0        0
      'fs_random_no_lp':             0           0           0             0         0         0           0         0          0            0        0
               'max_lp':        35'845   1'076'150   2'235'955     1'385'475         2       116         464         0          0            0      116
                'no_lp':        61'662   2'181'777   3'246'805     2'596'761        26     1'152      19'326         0          6           43      330
         'pseudo_costs':        35'760   1'086'923   2'261'781     1'281'023         7        42         168         0          0            0       42
        'quick_restart':        28'581     125'855   3'039'685     2'210'745       480    60'714     554'224         0        821        4'734   12'329
  'quick_restart_no_lp':        33'615     161'618   3'622'110     2'315'936       431    65'398     562'218         0        601        3'267   12'945
        'reduced_costs':        15'214      71'730     627'889       258'505       564    12'195     268'891         0         82          913    3'829

Lp stats            Component  Iterations  AddedCuts  OPTIMAL  DUAL_F.  DUAL_U.
     'default_lp':          1           0          0   78'024        0        0
      'fs_random':          1           0          0        0        0        0
         'max_lp':          1     466'462     42'192       15   45'922        0
   'pseudo_costs':          1     471'017     26'234       49   46'421        0
  'quick_restart':          1           0          0  682'209        0        0
  'reduced_costs':          1     441'859     31'157      220   43'628        0

Lp dimension                                                           Final dimension of first component
     'default_lp':          0 rows, 101 columns, 0 entries with magnitude in [0.000000e+00, 0.000000e+00]
      'fs_random':          0 rows, 101 columns, 0 entries with magnitude in [0.000000e+00, 0.000000e+00]
         'max_lp':   3037 rows, 2588 columns, 9327 entries with magnitude in [1.535260e-01, 1.000000e+00]
   'pseudo_costs':   2950 rows, 2588 columns, 8974 entries with magnitude in [1.122093e-02, 1.000000e+00]
  'quick_restart':          0 rows, 101 columns, 0 entries with magnitude in [0.000000e+00, 0.000000e+00]
  'reduced_costs':  3721 rows, 2588 columns, 12575 entries with magnitude in [8.336247e-03, 1.000000e+00]

Lp debug            CutPropag  CutEqPropag  Adjust  Overflow     Bad  BadScaling
     'default_lp':          0            0       0         0       0           0
      'fs_random':          0            0       0         0       0           0
         'max_lp':          0            0       0         0  16'185           0
   'pseudo_costs':          0            0       1         0  13'326           0
  'quick_restart':          0            0       0         0       0           0
  'reduced_costs':          0            0       0         0  19'008           0

Lp pool             Constraints  Updates  Simplif  Merged  Shortened  Split  Strenghtened      Cuts/Call
     'default_lp':          100        0        0       0          0      0             0            0/0
      'fs_random':          100        0        0       0          0      0             0            0/0
         'max_lp':       34'830      229   26'756   4'436          0      5        44'190  42'192/88'073
   'pseudo_costs':       11'393      297   22'948   2'915          0     22        36'994  26'234/47'558
  'quick_restart':          100        0        0       0          0      0             0            0/0
  'reduced_costs':       11'232      460   14'875   2'999          0      2        29'434  31'157/56'065

Lp Cut            max_lp  reduced_costs  pseudo_costs
     AllDiff_ee:     531            508           533
          CG_FF:   5'921          4'727         3'486
           CG_K:   2'517          2'200         1'945
           CG_R:   4'632          4'251         3'398
          CG_RB:   5'207          5'146         3'966
         CG_RBP:     388            756           675
             IB:      77          1'329         1'015
       MIR_1_FF:   4'549          1'217         1'372
        MIR_1_K:       -              -             2
        MIR_1_R:      44            100            95
       MIR_1_RB:   4'086          2'229         2'126
      MIR_1_RBP:     874            370           378
       MIR_2_FF:   1'876            957           923
        MIR_2_K:     124            125           115
        MIR_2_R:      77            153           103
       MIR_2_RB:   2'045          1'602         1'373
      MIR_2_RBP:     516            196           181
       MIR_3_FF:     282            254           248
        MIR_3_K:     116             55            58
        MIR_3_R:      24             44            29
       MIR_3_RB:     335            245           309
      MIR_3_RBP:      29             10            10
       MIR_4_FF:      51             75            42
        MIR_4_K:       7              3             5
        MIR_4_R:      10             23            14
       MIR_4_RB:      76             95           109
      MIR_4_RBP:       5              1             1
       MIR_5_FF:      29             57            22
        MIR_5_K:       5              8            23
        MIR_5_R:      12             23            17
       MIR_5_RB:      56             30            80
      MIR_5_RBP:       -              -             1
       MIR_6_FF:       2             27            22
        MIR_6_K:      13              4            20
        MIR_6_R:       4             19             9
       MIR_6_RB:      21             11            58
      MIR_6_RBP:       -              -             1
   ZERO_HALF_FF:   2'390            386           405
    ZERO_HALF_K:     358            254            80
    ZERO_HALF_R:   2'170          2'849         2'025
   ZERO_HALF_RB:   2'235            638           742
  ZERO_HALF_RBP:     498            180           218

LNS stats           Improv/Calls  Closed  Difficulty  TimeLimit
  'graph_arc_lns':         99/99     52%        0.90       0.10
  'graph_cst_lns':         99/99     53%        0.91       0.10
  'graph_dec_lns':         98/98     52%        0.90       0.10
  'graph_var_lns':         99/99     51%        0.84       0.10
      'rins/rens':         82/82     50%        0.64       0.10
    'rnd_cst_lns':         99/99     53%        0.91       0.10
    'rnd_var_lns':         69/70     54%        0.95       0.10

LS stats                                Batches  Restarts/Perturbs  LinMoves  GenMoves  CompoundMoves  Bactracks  WeightUpdates  ScoreComputed
                         'fj_restart':        1                  1     5'890         0              0          0             88         90'058
                         'ls_restart':       36                 17   215'611         0              0          0          6'173      3'229'548
                'ls_restart_compound':       29                 14         0    47'665          6'127     20'737             46      2'407'486
        'ls_restart_compound_perturb':       16                  9         0    29'450          3'767     12'824             33      1'332'576
                   'ls_restart_decay':       22                 13   144'840         0              0          0          1'440      1'960'118
          'ls_restart_decay_compound':       14                  7         0    25'642          3'517     11'052             20      1'163'420
  'ls_restart_decay_compound_perturb':       38                 14         0    56'748          8'808     23'921             47      3'160'627
           'ls_restart_decay_perturb':       16                  8   105'808         0              0          0          1'027      1'425'378
                 'ls_restart_perturb':       27                 18   157'488         0              0          0          4'561      2'418'980

Solutions (47)            Num     Rank
           'default_lp':    8  [18,46]
                'no_lp':   34   [1,41]
         'pseudo_costs':    1  [47,47]
        'quick_restart':    1  [17,17]
  'quick_restart_no_lp':    3   [2,42]

Objective bounds     Num
  'initial_domain':    1
    'pseudo_costs':    1
   'reduced_costs':    5

Solution repositories    Added  Queried  Synchro
  'feasible solutions':     80    1'558       52
        'lp solutions':  1'452       50      754
                'pump':     98       50

Improving bounds shared      Num
            'default_lp':    707
                 'no_lp':  3'434
          'pseudo_costs':      1
         'quick_restart':    304
   'quick_restart_no_lp':    306
         'reduced_costs':      1

CpSolverResponse summary:
status: FEASIBLE
objective: 16
best_bound: 8
integers: 101
booleans: 2487
conflicts: 0
branches: 7227
propagations: 8
integer_propagations: 14174
restarts: 4974
lp_iterations: 0
walltime: 60.0557
usertime: 60.0557
deterministic_time: 219.366
gap_integral: 457.355
solution_fingerprint: 0x750558b6b4da8204


Statistics
  status   : FEASIBLE
  conflicts: 0
  branches : 7227
  wall time: 60.05568100000001 s
Rooms needed = 16
1: [1, 2, 38, 77, 80, 90, 94]
2: [4, 42, 47, 67, 83, 93]
3: [16, 40, 48, 55, 75, 92]
4: [20, 21, 29, 51, 68, 91]
5: [24, 34, 49, 73, 74, 88]
6: [36, 56, 62, 81, 87, 100]
7: [13, 27, 37, 64, 76, 78, 86, 99]
8: [22, 53, 58, 84, 85, 98]
9: [3, 8, 11, 41, 59, 72, 82, 97]
10: [12, 15, 32, 44, 71, 96]
11: [6, 18, 45, 66, 69, 70]
12: [5, 10, 17, 39, 61, 63]
13: [7, 25, 31, 50, 52, 95]
14: [28, 33, 57, 60, 89]
15: [19, 23, 30, 43, 46, 79]
16: [9, 14, 26, 35, 54, 65]
```