# hybrid-dual-estimator

We provide an estimator by using the hybrid dual attack for all 5 LWE-based NIST candidates.

It includes 3 algorithms:
1. dual: the standard dual attack;
2. HYBRID1: the hybrid dual attack which guesses all possible vectors of the secret;
3. HYBRID2M: the hybrid dual attack with optimal pruning and efficient matrix multiplication.

## Verify the results 

To verify our results in Table 1 for the 5 LWE-based NIST candidates, one just need to run the estimator directly. 
The estimator only take less than 2 minutes for the core-SVP model, and it takes about 10-20 minutes for the practical model.

Among all the schemes, estimating Frodo takes the most time as its secret range is very large. 
Therefore, for Frodo, we use the following strategy to accelerate the estimator.
We reduce the "tk" for this kind of schemes with large secret range.
For example, the secret range of Frodo640 is (-12,12), then the exact value of "tk" is 13.
We set this value to 8 so that the estimator will finish in 2 minutes (for the classical core-SVP oracle).
Note that this strategy gives us an “upper bound” for the estimation.
Nevertheless, the influence of this change on the result is very small.
The recommended values for Frodo976 and Frodo1344 are 6 and 5, respectively.


<table border=0 align="center" cellpadding=0 cellspacing=0 width=845 style='border-collapse:
 collapse;table-layout:fixed;width:632pt'>
 <col width=187 style='mso-width-source:userset;mso-width-alt:5973;width:140pt'>
 <col width=136 style='mso-width-source:userset;mso-width-alt:4352;width:102pt'>
 <col width=87 span=6 style='width:65pt'>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td colspan=8 height=33 class=xl67 width=845 style='height:25.0pt;width:632pt'>Table1:
  Estimations under classical core-SVP model</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td rowspan=2 height=66 class=xl65 style='height:50.0pt;border-top:none'>Name</td>
  <td rowspan=2 class=xl65 style='border-top:none'>Security Level</td>
  <td class=xl65 style='border-top:none;border-left:none'>Dual</td>
  <td colspan=4 class=xl65 style='border-left:none'>HYBRID 2M</td>
  <td rowspan=2 class=xl65 style='border-top:none'>∆</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl66 style='height:25.0pt;border-top:none;border-left:
  none'>λ</td>
  <td class=xl66 style='border-top:none;border-left:none'>λ</td>
  <td class=xl65 style='border-top:none;border-left:none'>r</td>
  <td class=xl65 style='border-top:none;border-left:none'>b</td>
  <td class=xl65 style='border-top:none;border-left:none'>m</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Kyber512</td>
  <td class=xl65 style='border-top:none;border-left:none'>1</td>
  <td class=xl65 style='border-top:none;border-left:none'>118</td>
  <td class=xl65 style='border-top:none;border-left:none'>115</td>
  <td class=xl65 style='border-top:none;border-left:none'>13</td>
  <td class=xl65 style='border-top:none;border-left:none'>391</td>
  <td class=xl65 style='border-top:none;border-left:none'>502</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Kyber768</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>182</td>
  <td class=xl65 style='border-top:none;border-left:none'>176</td>
  <td class=xl65 style='border-top:none;border-left:none'>24</td>
  <td class=xl65 style='border-top:none;border-left:none'>600</td>
  <td class=xl65 style='border-top:none;border-left:none'>677</td>
  <td class=xl65 style='border-top:none;border-left:none'>8</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Kyber1024</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
  <td class=xl65 style='border-top:none;border-left:none'>254</td>
  <td class=xl65 style='border-top:none;border-left:none'>245</td>
  <td class=xl65 style='border-top:none;border-left:none'>34</td>
  <td class=xl65 style='border-top:none;border-left:none'>837</td>
  <td class=xl65 style='border-top:none;border-left:none'>862</td>
  <td class=xl65 style='border-top:none;border-left:none'>9</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Saber512</td>
  <td class=xl65 style='border-top:none;border-left:none'>1</td>
  <td class=xl65 style='border-top:none;border-left:none'>117</td>
  <td class=xl65 style='border-top:none;border-left:none'>115</td>
  <td class=xl65 style='border-top:none;border-left:none'>11</td>
  <td class=xl65 style='border-top:none;border-left:none'>392</td>
  <td class=xl65 style='border-top:none;border-left:none'>533</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Saber768</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>189</td>
  <td class=xl65 style='border-top:none;border-left:none'>184</td>
  <td class=xl65 style='border-top:none;border-left:none'>20</td>
  <td class=xl65 style='border-top:none;border-left:none'>629</td>
  <td class=xl65 style='border-top:none;border-left:none'>740</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Saber1024</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
  <td class=xl65 style='border-top:none;border-left:none'>258</td>
  <td class=xl65 style='border-top:none;border-left:none'>251</td>
  <td class=xl65 style='border-top:none;border-left:none'>30</td>
  <td class=xl65 style='border-top:none;border-left:none'>856</td>
  <td class=xl65 style='border-top:none;border-left:none'>908</td>
  <td class=xl65 style='border-top:none;border-left:none'>7</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Dilithium1024</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
  <td class=xl65 style='border-top:none;border-left:none'>124</td>
  <td class=xl65 style='border-top:none;border-left:none'>122</td>
  <td class=xl65 style='border-top:none;border-left:none'>14</td>
  <td class=xl65 style='border-top:none;border-left:none'>416</td>
  <td class=xl65 style='border-top:none;border-left:none'>1030</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Dilithium1280</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>182</td>
  <td class=xl65 style='border-top:none;border-left:none'>179</td>
  <td class=xl65 style='border-top:none;border-left:none'>15</td>
  <td class=xl65 style='border-top:none;border-left:none'>614</td>
  <td class=xl65 style='border-top:none;border-left:none'>1358</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Dilithium1792</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
  <td class=xl65 style='border-top:none;border-left:none'>251</td>
  <td class=xl65 style='border-top:none;border-left:none'>247</td>
  <td class=xl65 style='border-top:none;border-left:none'>29</td>
  <td class=xl65 style='border-top:none;border-left:none'>844</td>
  <td class=xl65 style='border-top:none;border-left:none'>1717</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Frodo640</td>
  <td class=xl65 style='border-top:none;border-left:none'>1</td>
  <td class=xl65 style='border-top:none;border-left:none'>142</td>
  <td class=xl65 style='border-top:none;border-left:none'>140</td>
  <td class=xl65 style='border-top:none;border-left:none'>9</td>
  <td class=xl65 style='border-top:none;border-left:none'>477</td>
  <td class=xl65 style='border-top:none;border-left:none'>640</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Frodo976</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>206</td>
  <td class=xl65 style='border-top:none;border-left:none'>202</td>
  <td class=xl65 style='border-top:none;border-left:none'>17</td>
  <td class=xl65 style='border-top:none;border-left:none'>690</td>
  <td class=xl65 style='border-top:none;border-left:none'>976</td>
  <td class=xl65 style='border-top:none;border-left:none'>4</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Frodo1344</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
  <td class=xl65 style='border-top:none;border-left:none'>271</td>
  <td class=xl65 style='border-top:none;border-left:none'>264</td>
  <td class=xl65 style='border-top:none;border-left:none'>29</td>
  <td class=xl65 style='border-top:none;border-left:none'>903</td>
  <td class=xl65 style='border-top:none;border-left:none'>1256</td>
  <td class=xl65 style='border-top:none;border-left:none'>7</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>NTRULPrime653</td>
  <td class=xl65 style='border-top:none;border-left:none'>1</td>
  <td class=xl65 style='border-top:none;border-left:none'>131</td>
  <td class=xl65 style='border-top:none;border-left:none'>125</td>
  <td class=xl65 style='border-top:none;border-left:none'>26</td>
  <td class=xl65 style='border-top:none;border-left:none'>425</td>
  <td class=xl65 style='border-top:none;border-left:none'>530</td>
  <td class=xl65 style='border-top:none;border-left:none'>6</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>NTRULPrime761</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
  <td class=xl65 style='border-top:none;border-left:none'>155</td>
  <td class=xl65 style='border-top:none;border-left:none'>148</td>
  <td class=xl65 style='border-top:none;border-left:none'>39</td>
  <td class=xl65 style='border-top:none;border-left:none'>502</td>
  <td class=xl65 style='border-top:none;border-left:none'>587</td>
  <td class=xl65 style='border-top:none;border-left:none'>7</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>NTRULPrime857</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
  <td class=xl65 style='border-top:none;border-left:none'>177</td>
  <td class=xl65 style='border-top:none;border-left:none'>168</td>
  <td class=xl65 style='border-top:none;border-left:none'>50</td>
  <td class=xl65 style='border-top:none;border-left:none'>570</td>
  <td class=xl65 style='border-top:none;border-left:none'>651</td>
  <td class=xl65 style='border-top:none;border-left:none'>9</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>NTRULPrime953</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>196</td>
  <td class=xl65 style='border-top:none;border-left:none'>187</td>
  <td class=xl65 style='border-top:none;border-left:none'>44</td>
  <td class=xl65 style='border-top:none;border-left:none'>635</td>
  <td class=xl65 style='border-top:none;border-left:none'>721</td>
  <td class=xl65 style='border-top:none;border-left:none'>9</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>NTRULPrime1013</td>
  <td class=xl65 style='border-top:none;border-left:none'>4</td>
  <td class=xl65 style='border-top:none;border-left:none'>210</td>
  <td class=xl65 style='border-top:none;border-left:none'>200</td>
  <td class=xl65 style='border-top:none;border-left:none'>43</td>
  <td class=xl65 style='border-top:none;border-left:none'>683</td>
  <td class=xl65 style='border-top:none;border-left:none'>780</td>
  <td class=xl65 style='border-top:none;border-left:none'>10</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>NTRULPrime1277</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
  <td class=xl65 style='border-top:none;border-left:none'>270</td>
  <td class=xl65 style='border-top:none;border-left:none'>256</td>
  <td class=xl65 style='border-top:none;border-left:none'>85</td>
  <td class=xl65 style='border-top:none;border-left:none'>869</td>
  <td class=xl65 style='border-top:none;border-left:none'>927</td>
  <td class=xl65 style='border-top:none;border-left:none'>14</td>
</table>

## Estimate a new scheme
To estimate a new scheme other than those 5 NIST candidates, one need to provide the parameters of the scheme.
Note that for the schemes that error and secret are from different distributions, one need to compute the scaling factor "c" in the parameter sets.

## Remarks
The secret of NTRULPrime follows a distribution with a fixed Hamming weight. To unify the code, our estimator does not consider this restriction. The difference caused by this is negligible. For example, the results under Hybrid 2 for NTRULPrime857 with and without the restriction are 168.022 and 168.024, respectively.
