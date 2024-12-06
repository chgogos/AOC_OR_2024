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

Starting CP-SAT solver v9.11.4210
Parameters: max_time_in_seconds: 1200 log_search_progress: true
Setting number of workers to 10

Initial optimization model '': (model_fingerprint: 0x4f12bbba576fa0e4)
#Variables: 63'009 (#bools: 63'009 in objective)
  - 63'009 Booleans in [0,1]
#kLinear1: 7
#kLinear2: 2
#kLinear3: 3
#kLinearN: 495 (#terms: 472'046)

Starting presolve at 0.01s
  6.69e-02s  0.00e+00d  [DetectDominanceRelations] 
  1.31e-01s  0.00e+00d  [PresolveToFixPoint] #num_loops=2 #num_dual_strengthening=1 
  4.27e-04s  0.00e+00d  [ExtractEncodingFromLinear] 
[Symmetry] Graph for symmetry has 119'548 nodes and 584'315 arcs.
[Symmetry] Symmetry computation done. time: 0.019064 dtime: 0.0487117
[Symmetry] #generators: 472, average support size: 2
[Symmetry] The model contains 5 duplicate constraints !
[Symmetry] 456 orbits with sizes: 3,3,3,3,3,3,3,3,3,3,...
[Symmetry] Found orbitope of size 1 x 2
[SAT presolve] num removable Booleans: 0 / 63001
[SAT presolve] num trivial clauses: 0
[SAT presolve] [0s] clauses:36601 literals:528265 vars:63001 one_side_vars:56234 simple_definition:2746 singleton_clauses:0
[SAT presolve] [0.209589s] clauses:36584 literals:494425 vars:63000 one_side_vars:62999 simple_definition:1 singleton_clauses:0
[SAT presolve] [0.213847s] clauses:36584 literals:494425 vars:63000 one_side_vars:62999 simple_definition:1 singleton_clauses:0
  1.22e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.17e-01s  1.05e+00d *[Probe] #probed=126'002 
  2.97e-02s  0.00e+00d  [MaxClique] Merged 36115(72230 literals) into 36112(72226 literals) at_most_ones. 
  4.62e-02s  0.00e+00d  [DetectDominanceRelations] 
  4.46e-02s  0.00e+00d  [DetectDominanceRelations] 
  1.42e-01s  0.00e+00d  [PresolveToFixPoint] #num_loops=3 #num_dual_strengthening=3 
  1.76e-03s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  1.15e-02s  0.00e+00d  [DetectDuplicateConstraints] 
  1.28e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.42e-04s  0.00e+00d  [DetectDominatedLinearConstraints] 
  2.07e-04s  0.00e+00d  [DetectDifferentVariables] 
  1.43e-02s  2.30e-03d  [ProcessSetPPC] #relevant_constraints=467 
  6.79e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  1.78e-03s  2.67e-04d  [FindBigAtMostOneAndLinearOverlap] 
  3.16e-03s  2.45e-03d  [FindBigVerticalLinearOverlap] 
  4.30e-04s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  6.85e-03s  2.11e-03d  [MergeClauses] 
  4.32e-02s  0.00e+00d  [DetectDominanceRelations] 
  6.09e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  4.37e-02s  0.00e+00d  [DetectDominanceRelations] 
  6.08e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
[Symmetry] Graph for symmetry has 74'086 nodes and 444'183 arcs.
[Symmetry] Symmetry computation done. time: 0.010421 dtime: 0.0322565
[Symmetry] #generators: 256, average support size: 2
[Symmetry] 241 orbits with sizes: 3,3,3,3,3,3,3,3,3,3,...
[Symmetry] Found orbitope of size 1 x 2
[SAT presolve] num removable Booleans: 0 / 56229
[SAT presolve] num trivial clauses: 0
[SAT presolve] [0s] clauses:6647 literals:433575 vars:56229 one_side_vars:54889 simple_definition:646 singleton_clauses:0
[SAT presolve] [0.052113s] clauses:6644 literals:407013 vars:56229 one_side_vars:56228 simple_definition:1 singleton_clauses:0
[SAT presolve] [0.055679s] clauses:6644 literals:407013 vars:56229 one_side_vars:56228 simple_definition:1 singleton_clauses:0
  1.14e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.09e-01s  1.04e+00d *[Probe] #probed=112'466 
  5.97e-03s  0.00e+00d  [MaxClique] Merged 6181(12362 literals) into 6179(12359 literals) at_most_ones. 
  5.48e-02s  0.00e+00d  [DetectDominanceRelations] 
  8.54e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=2 #num_dual_strengthening=2 
  4.05e-03s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  1.20e-02s  0.00e+00d  [DetectDuplicateConstraints] 
  1.15e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  4.33e-04s  0.00e+00d  [DetectDominatedLinearConstraints] 
  4.17e-04s  0.00e+00d  [DetectDifferentVariables] 
  1.43e-02s  2.08e-03d  [ProcessSetPPC] #relevant_constraints=464 
  6.07e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  2.62e-03s  1.43e-03d  [FindBigAtMostOneAndLinearOverlap] 
  3.19e-03s  2.58e-03d  [FindBigVerticalLinearOverlap] 
  7.67e-04s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  6.74e-03s  1.97e-03d  [MergeClauses] 
  4.20e-02s  0.00e+00d  [DetectDominanceRelations] 
  6.13e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  4.23e-02s  0.00e+00d  [DetectDominanceRelations] 
  6.04e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
[Symmetry] Graph for symmetry has 115'106 nodes and 513'571 arcs.
[Symmetry] Symmetry computation done. time: 0.015239 dtime: 0.0432034
[Symmetry] #generators: 235, average support size: 2
[Symmetry] 222 orbits with sizes: 3,3,3,3,3,3,3,3,3,3,...
[Symmetry] Found orbitope of size 1 x 2
[SAT presolve] num removable Booleans: 0 / 54889
[SAT presolve] num trivial clauses: 0
[SAT presolve] [0s] clauses:34107 literals:461939 vars:54889 one_side_vars:46748 simple_definition:3268 singleton_clauses:0
[SAT presolve] [0.182995s] clauses:34106 literals:413385 vars:54889 one_side_vars:54889 simple_definition:0 singleton_clauses:0
[SAT presolve] [0.186697s] clauses:34106 literals:413385 vars:54889 one_side_vars:54889 simple_definition:0 singleton_clauses:0
  1.13e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  2.15e-01s  1.04e+00d *[Probe] #probed=109'788 
  2.70e-02s  0.00e+00d  [MaxClique] 
  3.90e-02s  0.00e+00d  [DetectDominanceRelations] 
  7.87e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=2 #num_dual_strengthening=2 
  1.98e-03s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  1.08e-02s  0.00e+00d  [DetectDuplicateConstraints] 
  1.05e-02s  0.00e+00d  [DetectDuplicateConstraintsWithDifferentEnforcements] 
  6.50e-04s  0.00e+00d  [DetectDominatedLinearConstraints] 
  5.43e-04s  0.00e+00d  [DetectDifferentVariables] 
  1.30e-02s  1.88e-03d  [ProcessSetPPC] #relevant_constraints=463 
  8.50e-04s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  1.71e-03s  1.44e-04d  [FindBigAtMostOneAndLinearOverlap] 
  3.46e-03s  1.99e-03d  [FindBigVerticalLinearOverlap] 
  8.90e-04s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  8.72e-03s  1.73e-03d  [MergeClauses] 
  3.93e-02s  0.00e+00d  [DetectDominanceRelations] 
  5.83e-02s  0.00e+00d  [PresolveToFixPoint] #num_loops=1 #num_dual_strengthening=1 
  7.64e-03s  0.00e+00d  [ExpandObjective] 

Presolve summary:
  - 0 affine relations were detected.
  - rule 'TODO domination: unexploited dominations' was applied 5 times.
  - rule 'TODO dual: only one blocking constraint?' was applied 56 times.
  - rule 'TODO dual: only one unspecified blocking constraint?' was applied 682'863 times.
  - rule 'at_most_one: empty or all false' was applied 1 time.
  - rule 'at_most_one: removed literals' was applied 75'934 times.
  - rule 'at_most_one: resolved two constraints with opposite literal' was applied 2 times.
  - rule 'at_most_one: singleton' was applied 6'649 times.
  - rule 'at_most_one: size one' was applied 75'930 times.
  - rule 'at_most_one: transformed into max clique.' was applied 2 times.
  - rule 'bool_or: always true' was applied 2 times.
  - rule 'domination: added implications' was applied 78'711 times.
  - rule 'domination: in at most one' was applied 1 time.
  - rule 'dual: fix variable' was applied 9'597 times.
  - rule 'exactly_one: singleton' was applied 3 times.
  - rule 'linear: always true' was applied 14 times.
  - rule 'linear: empty' was applied 6 times.
  - rule 'linear: fixed or dup variables' was applied 20 times.
  - rule 'linear: positive clause' was applied 487 times.
  - rule 'linear: reduced variable domains' was applied 6 times.
  - rule 'linear: simplified rhs' was applied 493 times.
  - rule 'objective: variable not used elsewhere' was applied 6'659 times.
  - rule 'presolve: 16256 unused variables removed.' was applied 1 time.
  - rule 'presolve: iteration' was applied 3 times.
  - rule 'symmetry: added symmetry breaking implication' was applied 3 times.

Presolved optimization model '': (model_fingerprint: 0x581b75e13d163e47)
#Variables: 46'748 (#bools: 46'748 in objective)
  - 46'748 Booleans in [0,1]
#kBoolAnd: 2'778 (#enforced: 2'778) (#literals: 5'556)
#kBoolOr: 462 (#literals: 346'097)

Preloading model.
#Bound   2.54s best:inf   next:[13,90731] initial_domain
[Symmetry] Graph for symmetry has 53'232 nodes and 357'675 arcs.
[Symmetry] Symmetry computation done. time: 0.007988 dtime: 0.0251472
[Symmetry] #generators: 206, average support size: 2
[Symmetry] Found orbitope of size 1 x 2
#Model   2.57s var:46748/46748 constraints:3240/3240

Starting search at 2.57s with 10 workers.
7 full problem subsolvers: [core, default_lp, max_lp, no_lp, quick_restart, quick_restart_no_lp, reduced_costs]
3 first solution subsolvers: [fj, fs_random, fs_random_no_lp]
10 interleaved subsolvers: [feasibility_pump, graph_arc_lns, graph_cst_lns, graph_dec_lns, graph_var_lns, ls(2), rins/rens, rnd_cst_lns, rnd_var_lns]
3 helper subsolvers: [neighborhood_helper, synchronization_agent, update_gap_integral]

#1       2.69s best:351   next:[13,350]   fj_restart(batch:1 lin{mvs:173 evals:843} #w_updates:0 #perturb:0)
#2       2.75s best:317   next:[13,316]   no_lp (fixed_bools=0/46748)
#Bound   2.75s best:317   next:[15,316]   am1_presolve (num_literals=46748 num_am1=1 increase=2 work_done=49527)
#Bound   2.78s best:317   next:[17,316]   bool_core (num_cores=1 [size:180 mw:2 d:8] a=46568 d=8 fixed=0/46927 clauses=641)
#Bound   3.17s best:317   next:[19,316]   bool_core (num_cores=2 [size:188 mw:2 d:8] a=46381 d=8 fixed=0/47292 clauses=1'006)
#Bound   3.18s best:317   next:[21,316]   bool_core (num_cores=3 [size:124 mw:2 d:7] a=46258 d=8 fixed=0/47601 clauses=1'315)
#Bound   3.19s best:317   next:[23,316]   bool_core (num_cores=4 [size:113 mw:2 d:7] a=46146 d=8 fixed=0/47835 clauses=1'549)
#Bound   3.22s best:317   next:[25,316]   bool_core (num_cores=5 [size:1098 mw:2 d:11] a=45049 d=11 fixed=0/49043 clauses=2'757)
#Model   3.40s var:46747/46748 constraints:3077/3240
#Bound   3.77s best:317   next:[161,316]  reduced_costs
#Bound   4.84s best:317   next:[167,316]  reduced_costs
#3       5.99s best:316   next:[167,315]  default_lp (fixed_bools=1/46748)
#4       6.12s best:244   next:[167,243]  quick_restart_no_lp (fixed_bools=1/46748)
#5       7.87s best:240   next:[167,239]  quick_restart_no_lp (fixed_bools=1/46748)
#6       8.01s best:239   next:[167,238]  core (fixed_bools=1/54951)
#7      10.38s best:238   next:[167,237]  quick_restart_no_lp (fixed_bools=1/46748)
#8      13.35s best:174   next:[167,173]  reduced_costs (fixed_bools=1/46748)
#9      15.44s best:171   next:[167,170]  max_lp (fixed_bools=1/46748)
#10     27.50s best:170   next:[167,169]  max_lp (fixed_bools=1/46748)
#11    381.34s best:169   next:[167,168]  reduced_costs (fixed_bools=1/46748)
#Model 389.00s var:39118/46748 constraints:2080/3240
#Model 526.09s var:38342/46748 constraints:1980/3240
#Model 589.18s var:37623/46748 constraints:1926/3240
#Model 600.13s var:36852/46748 constraints:1923/3240
#Model 768.90s var:36627/46748 constraints:1923/3240
#Model 773.08s var:36618/46748 constraints:1923/3240
#Model 803.38s var:36614/46748 constraints:1923/3240

Task timing                      n [     min,      max]      avg      dev     time         n [     min,      max]      avg      dev    dtime
                 'core':         1 [  19.96m,   19.96m]   19.96m   0.00ns   19.96m         1 [  46.70m,   46.70m]   46.70m   0.00ns   46.70m
           'default_lp':         1 [  19.96m,   19.96m]   19.96m   0.00ns   19.96m         1 [  13.00m,   13.00m]   13.00m   0.00ns   13.00m
     'feasibility_pump':         1 [ 67.58ms,  67.58ms]  67.58ms   0.00ns  67.58ms         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                   'fj':         1 [ 48.07ms,  48.07ms]  48.07ms   0.00ns  48.07ms         1 [ 20.85ms,  20.85ms]  20.85ms   0.00ns  20.85ms
            'fs_random':         1 [171.51ms, 171.51ms] 171.51ms   0.00ns 171.51ms         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
      'fs_random_no_lp':         1 [145.60ms, 145.60ms] 145.60ms   0.00ns 145.60ms         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
        'graph_arc_lns':       252 [ 89.93ms,   16.56s]    1.53s    1.91s    6.42m       251 [ 10.00ns, 109.00ms]  61.38ms  47.03ms   15.41s
        'graph_cst_lns':       251 [ 40.23ms,   16.75s]    3.91s    2.70s   16.36m       250 [ 10.00ns, 108.67ms]  59.90ms  48.04ms   14.97s
        'graph_dec_lns':       251 [ 93.88ms,   12.17s] 778.29ms    1.19s    3.26m       251 [  4.52us, 108.38ms]  59.86ms  47.58ms   15.03s
        'graph_var_lns':       252 [ 88.63ms,   21.06s]    3.95s    3.14s   16.59m       251 [ 10.00ns, 109.05ms]  58.94ms  48.50ms   14.79s
                   'ls':       251 [ 23.27ms, 270.79ms]  39.28ms  18.51ms    9.86s       251 [100.12ms, 102.55ms] 100.99ms 418.45us   25.35s
                   'ls':       251 [ 23.60ms, 159.34ms]  38.34ms  13.96ms    9.62s       251 [100.11ms, 102.48ms] 101.01ms 411.97us   25.35s
               'max_lp':         1 [  19.96m,   19.96m]   19.96m   0.00ns   19.96m         1 [  31.92m,   31.92m]   31.92m   0.00ns   31.92m
                'no_lp':         1 [  19.96m,   19.96m]   19.96m   0.00ns   19.96m         1 [  15.89m,   15.89m]   15.89m   0.00ns   15.89m
        'quick_restart':         1 [  19.96m,   19.96m]   19.96m   0.00ns   19.96m         1 [   9.51m,    9.51m]    9.51m   0.00ns    9.51m
  'quick_restart_no_lp':         1 [  19.96m,   19.96m]   19.96m   0.00ns   19.96m         1 [   9.43m,    9.43m]    9.43m   0.00ns    9.43m
        'reduced_costs':         1 [  19.96m,   19.96m]   19.96m   0.00ns   19.96m         1 [  26.32m,   26.32m]   26.32m   0.00ns   26.32m
            'rins/rens':       252 [ 30.48ms,   10.48s] 225.92ms 655.43ms   56.93s       247 [ 10.00ns, 108.65ms]  56.36ms  50.95ms   13.92s
          'rnd_cst_lns':       252 [145.46ms,   22.86s]    2.99s    2.47s   12.56m       251 [ 10.00ns, 108.78ms]  60.32ms  47.84ms   15.14s
          'rnd_var_lns':       252 [ 83.92ms,   17.32s] 794.63ms    1.46s    3.34m       252 [350.00ns, 108.86ms]  60.34ms  47.66ms   15.21s

Search stats                Bools  Conflicts     Branches   Restarts      BoolPropag  IntegerPropag
                 'core':  274'433    737'586   70'105'756    852'454  13'445'898'923    546'770'875
           'default_lp':   46'748  2'812'413    8'368'626    120'784   1'263'688'886  3'266'841'786
            'fs_random':   46'748          0       72'198     72'198           4'237         76'436
      'fs_random_no_lp':   46'748          0       58'656     58'656           3'648         62'305
               'max_lp':   46'748     20'731    3'014'346    561'784       3'750'106    111'349'448
                'no_lp':   46'748  7'374'235   16'877'274    120'623   1'039'750'289  3'992'182'705
        'quick_restart':   46'748    403'594  793'650'193    877'537     373'794'776  2'469'014'070
  'quick_restart_no_lp':   46'748    403'393  806'238'931  2'809'249     349'384'064  2'297'477'954
        'reduced_costs':   46'748     17'113    9'263'838  1'727'522       6'895'095    359'146'781

SAT stats                 ClassicMinim   LitRemoved     LitLearned   LitForgotten  Subsumed  MClauses  MDecisions  MLitTrue  MSubsumed  MLitRemoved  MReused
                 'core':       679'237  371'063'280  1'684'575'783  1'604'771'682     1'819       378   2'338'028         0         77       19'010      380
           'default_lp':     1'533'609    2'770'995    641'763'873    604'288'322   141'795         2     200'404         0          0            0        0
            'fs_random':             0            0              0              0         0         0           0         0          0            0        0
      'fs_random_no_lp':             0            0              0              0         0         0           0         0          0            0        0
               'max_lp':        18'269    6'178'025     36'043'205     25'684'079        14       358   2'096'773         0          0            0      384
                'no_lp':       854'028    1'405'105  2'863'954'643  2'390'315'930   870'579         2     200'404         0          0            0        0
        'quick_restart':       154'083      480'534    209'402'452    183'603'809    22'014       465   3'278'111         0          0            0      534
  'quick_restart_no_lp':       165'196      526'305    216'235'545    190'189'324    17'472     1'841  11'790'137         0          0            0    1'810
        'reduced_costs':        14'542   13'240'396     11'542'961      6'164'593        13     1'146   7'036'564         0          0            0    1'418

Lp stats            Component  Iterations  AddedCuts  OPTIMAL  DUAL_F.  DUAL_U.
         'max_lp':          1   9'545'301          2   60'127      100       15
  'reduced_costs':          1   7'247'800          0   38'997      286        0

Lp dimension                                                            Final dimension of first component
         'max_lp':  387 rows, 46748 columns, 218789 entries with magnitude in [1.000000e+00, 1.000000e+00]
  'reduced_costs':  422 rows, 46748 columns, 261448 entries with magnitude in [1.000000e+00, 1.000000e+00]

Lp debug            CutPropag  CutEqPropag  Adjust  Overflow     Bad  BadScaling
         'max_lp':          0            0  60'126         0   9'179           0
  'reduced_costs':          0            0  39'057         0  11'101           0

Lp pool             Constraints  Updates  Simplif  Merged  Shortened  Split  Strenghtened  Cuts/Call
         'max_lp':        3'242      623      492       0        166      0             0      2/511
  'reduced_costs':        3'240      784      655       0        166      0             0      0/524

Lp Cut       max_lp
  MIR_2_FF:       2

LNS stats           Improv/Calls  Closed  Difficulty  TimeLimit
  'graph_arc_lns':         0/251     49%        0.11       0.11
  'graph_cst_lns':         0/251     49%        0.09       0.11
  'graph_dec_lns':         0/251     50%        0.11       0.11
  'graph_var_lns':         1/251     49%        0.10       0.11
      'rins/rens':         0/247     47%        0.00       0.11
    'rnd_cst_lns':         1/251     49%        0.08       0.11
    'rnd_var_lns':         1/252     49%        0.10       0.11

LS stats                                Batches  Restarts/Perturbs  LinMoves  GenMoves  CompoundMoves  Bactracks  WeightUpdates  ScoreComputed
                         'fj_restart':        1                  1       173         0              0          0              0            843
                         'ls_restart':       58                 29     6'667         0              0          0          2'063      1'715'843
                'ls_restart_compound':       61                 24         0     6'210             18      3'076              9        759'703
        'ls_restart_compound_perturb':       58                 33         0     5'901             28      2'907             11        733'601
                   'ls_restart_decay':       66                 15    15'690         0              0          0            580      2'399'130
          'ls_restart_decay_compound':       36                 19         0     3'667              4      1'812              2        488'732
  'ls_restart_decay_compound_perturb':       94                 28         0     9'666             57      4'774             17      1'267'180
           'ls_restart_decay_perturb':       62                 29    16'078         0              0          0            699      2'341'454
                 'ls_restart_perturb':       67                 30     7'745         0              0          0          2'141      2'099'184

Solutions (11)            Num    Rank
                 'core':    1   [6,6]
           'default_lp':    1   [3,3]
           'fj_restart':    1   [1,1]
               'max_lp':    2  [9,10]
                'no_lp':    1   [2,2]
  'quick_restart_no_lp':    3   [4,7]
        'reduced_costs':    2  [8,11]

Objective bounds     Num
    'am1_presolve':    1
       'bool_core':    5
  'initial_domain':    1
   'reduced_costs':    2

Solution repositories    Added  Queried  Synchro
  'feasible solutions':    945    3'918      934
        'lp solutions':  7'919      252    4'116
                'pump':      0        0

Improving bounds shared      Num
            'default_lp':      1
                'max_lp':    953
         'reduced_costs':  9'180

CpSolverResponse summary:
status: FEASIBLE
objective: 169
best_bound: 167
integers: 46965
booleans: 46748
conflicts: 0
branches: 58656
propagations: 3648
integer_propagations: 62305
restarts: 58656
lp_iterations: 0
walltime: 1200.59
usertime: 1200.59
deterministic_time: 9323.75
gap_integral: 6475.02
solution_fingerprint: 0x50e5e7f32cb25c02

status: FEASIBLE
obj=169
bound=167
time=1200.6
Selected possibility 245 : (2, [4, 47, 48, 16, 131])
Selected possibility 246 : (1, [3, 126, 127, 404])
Selected possibility 351 : (2, [6, 128, 129, 130, 123, 124, 125])
Selected possibility 583 : (2, [8, 132, 139, 140, 473, 474, 475, 383, 384])
Selected possibility 619 : (2, [7, 133, 38, 39, 348, 349, 444, 445])
Selected possibility 1392 : (1, [5, 374, 375, 380, 467, 373])
Selected possibility 2009 : (1, [4, 403, 284, 285, 436])
Selected possibility 2063 : (1, [5, 409, 410, 90, 91, 435])
Selected possibility 2448 : (2, [10, 425, 426, 427, 428, 171, 399, 400, 401, 402, 403])
Selected possibility 2855 : (2, [6, 120, 121, 122, 352, 353, 119])
Selected possibility 2948 : (2, [7, 151, 152, 153, 154, 442, 443, 150])
Selected possibility 3037 : (2, [7, 158, 159, 488, 451, 148, 149, 157])
Selected possibility 3114 : (2, [7, 221, 222, 223, 224, 330, 331, 86])
Selected possibility 3154 : (2, [6, 229, 230, 320, 334, 335, 241])
Selected possibility 3264 : (2, [6, 240, 215, 182, 235, 236, 247])
Selected possibility 3306 : (1, [2, 242, 146])
Selected possibility 3457 : (2, [6, 248, 113, 217, 65, 177, 237])
Selected possibility 4340 : (1, [3, 13, 239, 250])
Selected possibility 5234 : (2, [11, 21, 22, 23, 24, 25, 26, 27, 49, 50, 446, 447])
Selected possibility 6229 : (1, [4, 63, 180, 249, 110])
Selected possibility 6859 : (1, [4, 92, 93, 155, 156])
Selected possibility 6882 : (1, [4, 92, 93, 312, 313])
Selected possibility 7190 : (1, [4, 98, 99, 346, 347])
Selected possibility 7248 : (1, [4, 100, 64, 102, 272])
Selected possibility 9030 : (2, [5, 191, 192, 283, 414, 415])
Selected possibility 9261 : (1, [2, 218, 251])
Selected possibility 9614 : (2, [7, 222, 220, 216, 176, 101, 181, 281])
Selected possibility 9963 : (1, [3, 227, 228, 244])
Selected possibility 10849 : (1, [4, 277, 251, 271, 276])
Selected possibility 12118 : (1, [4, 354, 355, 209, 366])
Selected possibility 12321 : (1, [4, 360, 329, 326, 327])
Selected possibility 12391 : (1, [4, 364, 95, 96, 278])
Selected possibility 12497 : (1, [2, 367, 343])
Selected possibility 12645 : (1, [6, 396, 397, 398, 430, 431, 432])
Selected possibility 13108 : (2, [7, 416, 417, 418, 507, 279, 280, 87])
Selected possibility 13297 : (2, [6, 422, 423, 424, 286, 193, 194])
Selected possibility 14451 : (2, [4, 448, 205, 287, 85])
Selected possibility 15239 : (1, [3, 464, 109, 238])
Selected possibility 15910 : (2, [6, 469, 470, 378, 261, 53, 54])
Selected possibility 17409 : (1, [3, 476, 17, 222])
Selected possibility 17630 : (2, [4, 481, 413, 51, 484])
Selected possibility 18536 : (2, [5, 52, 340, 341, 358, 198])
Selected possibility 18537 : (2, [2, 69, 200])
Selected possibility 18570 : (2, [8, 71, 72, 185, 186, 187, 188, 83, 84])
Selected possibility 19939 : (2, [2, 199, 70])
Selected possibility 20667 : (2, [5, 291, 479, 480, 195, 1])
Selected possibility 20668 : (2, [5, 291, 479, 480, 196, 290])
Selected possibility 22381 : (2, [6, 427, 19, 20, 245, 79, 80])
Selected possibility 23798 : (1, [4, 67, 68, 486, 494])
Selected possibility 27079 : (2, [5, 161, 162, 163, 164, 450])
Selected possibility 29252 : (2, [9, 189, 495, 452, 453, 297, 298, 299, 300, 301])
Selected possibility 30808 : (2, [6, 294, 295, 296, 342, 483, 449])
Selected possibility 31546 : (2, [7, 301, 306, 190, 183, 184, 408, 255])
Selected possibility 32578 : (1, [4, 307, 308, 503, 504])
Selected possibility 34326 : (2, [8, 430, 256, 257, 258, 212, 30, 31, 32])
Selected possibility 36209 : (2, [6, 495, 442, 484, 485, 81, 82])
Selected possibility 37750 : (2, [7, 501, 502, 197, 359, 252, 253, 254])
Selected possibility 38069 : (2, [7, 173, 174, 175, 489, 500, 147, 172])
Selected possibility 38349 : (2, [6, 411, 412, 407, 408, 18, 439])
Selected possibility 38381 : (1, [4, 440, 441, 506, 62])
Selected possibility 39024 : (2, [9, 29, 14, 15, 268, 269, 22, 23, 24, 25])
Selected possibility 39076 : (2, [8, 29, 134, 135, 136, 141, 142, 143, 21])
Selected possibility 39708 : (1, [3, 43, 56, 28])
Selected possibility 40779 : (1, [3, 264, 382, 383])
Selected possibility 40832 : (1, [4, 266, 267, 262, 263])
Selected possibility 40907 : (2, [12, 266, 459, 460, 332, 333, 45, 46, 269, 22, 23, 24, 25])
Selected possibility 41195 : (1, [4, 274, 433, 434, 42])
Selected possibility 41711 : (1, [4, 375, 273, 370, 393])
Selected possibility 41743 : (1, [4, 375, 376, 377, 378])
Selected possibility 41912 : (2, [7, 378, 379, 138, 283, 423, 390, 391])
Selected possibility 42429 : (1, [7, 380, 467, 468, 178, 101, 456, 457])
Selected possibility 42440 : (1, [4, 381, 259, 260, 43])
Selected possibility 42657 : (1, [4, 386, 387, 388, 389])
Selected possibility 43738 : (1, [6, 458, 129, 36, 37, 385, 386])
Selected possibility 45045 : (2, [9, 472, 437, 438, 505, 419, 420, 421, 465, 466])
Selected possibility 45304 : (2, [8, 477, 389, 46, 269, 270, 371, 391, 378])
Selected possibility 45488 : (2, [6, 34, 304, 305, 302, 303, 326])
Selected possibility 45651 : (2, [6, 61, 144, 145, 363, 497, 338])
Selected possibility 47884 : (1, [4, 160, 103, 337, 493])
Selected possibility 48257 : (1, [3, 226, 227, 328])
Selected possibility 48559 : (2, [4, 288, 289, 206, 482])
Selected possibility 49406 : (2, [5, 322, 3, 201, 231, 487])
Selected possibility 50540 : (2, [6, 339, 137, 405, 406, 407, 496])
Selected possibility 51825 : (2, [6, 355, 117, 118, 243, 79, 33])
Selected possibility 52109 : (2, [8, 355, 309, 310, 311, 490, 491, 492, 321])
Selected possibility 52551 : (2, [7, 361, 179, 66, 323, 324, 325, 88])
Selected possibility 53275 : (1, [2, 365, 282])
Selected possibility 55670 : (2, [6, 111, 112, 113, 114, 115, 116])
Selected possibility 55674 : (1, [2, 40, 41])
Selected possibility 55759 : (2, [7, 461, 462, 454, 455, 476, 477, 478])
Selected possibility 55819 : (2, [5, 35, 36, 273, 43, 44])
Selected possibility 56023 : (2, [6, 60, 210, 211, 97, 350, 351])
Selected possibility 56143 : (2, [6, 73, 74, 75, 168, 169, 170])
Selected possibility 56641 : (1, [4, 94, 362, 314, 315])
Selected possibility 56688 : (2, [6, 103, 89, 275, 219, 213, 214])
Selected possibility 56703 : (2, [6, 103, 104, 105, 206, 207, 208])
Selected possibility 56892 : (2, [6, 165, 166, 167, 76, 77, 78])
Selected possibility 56964 : (2, [6, 203, 204, 205, 106, 107, 108])
Selected possibility 57101 : (1, [2, 225, 202])
Selected possibility 57149 : (2, [6, 232, 233, 234, 246, 356, 357])
Selected possibility 57175 : (1, [4, 292, 293, 344, 345])
Selected possibility 57768 : (2, [8, 316, 317, 55, 462, 463, 464, 336, 337])
Selected possibility 57905 : (1, [4, 318, 319, 340, 341])
Selected possibility 61649 : (2, [7, 498, 499, 428, 429, 57, 58, 59])
Selected possibility 62290 : (2, [7, 265, 266, 372, 391, 471, 394, 395])
Selected possibility 62362 : (1, [5, 368, 369, 386, 391, 392])
```