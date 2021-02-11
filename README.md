# hybrid-dual-estimator

We provide an estimator by using the hybrid dual attack for all 5 LWE-based NIST candidates.
It includes 3 algorithm:
1. dual: the standard dual attack;
2. HYBRID1: the hybrid dual attack which guesses all possible vectors of the secret;
3. HYBTID2M: the hybrid dual attack with optimal pruning and efficient matrix multiplication.

## Verify the results 

To verify our results 

**Estimate a new scheme.** 

**Remarks.**
1.  In “guess-all” and “optimal-guess”, we use ![](http://latex.codecogs.com/svg.latex?\max(T_{BKZ},T_{guess})) instead of ![](http://latex.codecogs.com/svg.latex?T_{BKZ}+T_{guess}) to make the algorithm easier and much quicker. This, however, may de- crease the final result by up to 1 bit.
2. The secret of NTRULPrime follows a distribution with a fixed Hamming weight. To unify the code, our estimator does not consider this restriction. The differ- ence caused by this is negligible. For example, the results under “optimal-guess” for NTRULPrime857 with and without the restriction are 167.326 and 167.307, respectively.

