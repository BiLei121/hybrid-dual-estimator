# hybrid-dual-estimator

We provide an estimator by using the hybrid dual attack for all 5 LWE-based NIST candidates.

It includes 3 algorithms:
1. dual: the standard dual attack;
2. HYBRID1: the hybrid dual attack which guesses all possible vectors of the secret;
3. HYBTID2M: the hybrid dual attack with optimal pruning and efficient matrix multiplication.

## Verify the results 

To verify our results in Table 1 as follows for the 5 LWE-based NIST candidates, one just need to run the estimator directly.

## Estimate a new scheme

To estimate a new scheme other than those 5 NIST candidates, one need to provide the parameters of the scheme. 


## Remarks
1.  In HYBRID1 and HYBTID2M, we use ![](http://latex.codecogs.com/svg.latex?\max(T_{BKZ},T_{guess})) instead of ![](http://latex.codecogs.com/svg.latex?T_{BKZ}+T_{guess}) to make the algorithm easier and much quicker. This, however, may de- crease the final result by up to 1 bit.
2. The secret of NTRULPrime follows a distribution with a fixed Hamming weight. To unify the code, our estimator does not consider this restriction. The difference caused by this is negligible. For example, the results under HYBTID2M for NTRULPrime857 with and without the restriction are 167.326 and 167.307, respectively.


<table border=0 align="center" cellpadding=0 cellspacing=0 width=861 style='border-collapse:
 collapse;table-layout:fixed;width:644pt'>
 <col width=187 style='mso-width-source:userset;mso-width-alt:5973;width:140pt'>
 <col width=152 style='mso-width-source:userset;mso-width-alt:4864;width:114pt'>
 <col width=87 span=6 style='width:65pt'>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td text-align: "center" colspan=8 height=33 class=xl67 width=861 style='height:25.0pt;width:644pt'>Table 1: Estimations
  under classical core-SVP model</td>
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
  <td class=xl65 style='border-top:none;border-left:none'>112</td>
  <td class=xl65 style='border-top:none;border-left:none'>108</td>
  <td class=xl65 style='border-top:none;border-left:none'>14</td>
  <td class=xl65 style='border-top:none;border-left:none'>369</td>
  <td class=xl65 style='border-top:none;border-left:none'>482</td>
  <td class=xl65 style='border-top:none;border-left:none'>4</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Kyber768</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>182</td>
  <td class=xl65 style='border-top:none;border-left:none'>176</td>
  <td class=xl65 style='border-top:none;border-left:none'>24</td>
  <td class=xl65 style='border-top:none;border-left:none'>599</td>
  <td class=xl65 style='border-top:none;border-left:none'>676</td>
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
  <td class=xl65 style='border-top:none;border-left:none'>628</td>
  <td class=xl65 style='border-top:none;border-left:none'>740</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Saber1024</td>
  <td class=xl65 style='border-top:none;border-left:none'>5</td>
  <td class=xl65 style='border-top:none;border-left:none'>258</td>
  <td class=xl65 style='border-top:none;border-left:none'>250</td>
  <td class=xl65 style='border-top:none;border-left:none'>30</td>
  <td class=xl65 style='border-top:none;border-left:none'>855</td>
  <td class=xl65 style='border-top:none;border-left:none'>907</td>
  <td class=xl65 style='border-top:none;border-left:none'>8</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Dilithium768</td>
  <td class=xl65 style='border-top:none;border-left:none'>1</td>
  <td class=xl65 style='border-top:none;border-left:none'>100</td>
  <td class=xl65 style='border-top:none;border-left:none'>99</td>
  <td class=xl65 style='border-top:none;border-left:none'>6</td>
  <td class=xl65 style='border-top:none;border-left:none'>339</td>
  <td class=xl65 style='border-top:none;border-left:none'>890</td>
  <td class=xl65 style='border-top:none;border-left:none'>1</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Dilithium1024</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
  <td class=xl65 style='border-top:none;border-left:none'>142</td>
  <td class=xl65 style='border-top:none;border-left:none'>140</td>
  <td class=xl65 style='border-top:none;border-left:none'>10</td>
  <td class=xl65 style='border-top:none;border-left:none'>479</td>
  <td class=xl65 style='border-top:none;border-left:none'>1134</td>
  <td class=xl65 style='border-top:none;border-left:none'>2</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Dilithium1280</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>175</td>
  <td class=xl65 style='border-top:none;border-left:none'>172</td>
  <td class=xl65 style='border-top:none;border-left:none'>16</td>
  <td class=xl65 style='border-top:none;border-left:none'>588</td>
  <td class=xl65 style='border-top:none;border-left:none'>1317</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>Frodo640</td>
  <td class=xl65 style='border-top:none;border-left:none'>1</td>
  <td class=xl65 style='border-top:none;border-left:none'>142</td>
  <td class=xl65 style='border-top:none;border-left:none'>139</td>
  <td class=xl65 style='border-top:none;border-left:none'>11</td>
  <td class=xl65 style='border-top:none;border-left:none'>475</td>
  <td class=xl65 style='border-top:none;border-left:none'>640</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
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
  <td class=xl65 style='border-top:none;border-left:none'>36</td>
  <td class=xl65 style='border-top:none;border-left:none'>503</td>
  <td class=xl65 style='border-top:none;border-left:none'>588</td>
  <td class=xl65 style='border-top:none;border-left:none'>7</td>
 </tr>
 <tr height=33 style='mso-height-source:userset;height:25.0pt'>
  <td height=33 class=xl65 style='height:25.0pt;border-top:none'>NTRULPrime857</td>
  <td class=xl65 style='border-top:none;border-left:none'>3</td>
  <td class=xl65 style='border-top:none;border-left:none'>177</td>
  <td class=xl65 style='border-top:none;border-left:none'>168</td>
  <td class=xl65 style='border-top:none;border-left:none'>44</td>
  <td class=xl65 style='border-top:none;border-left:none'>571</td>
  <td class=xl65 style='border-top:none;border-left:none'>167</td>
  <td class=xl65 style='border-top:none;border-left:none'>9</td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=187 style='width:140pt'></td>
  <td width=152 style='width:114pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
 </tr>
 <![endif]>
</table>
