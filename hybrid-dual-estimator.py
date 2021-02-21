import math
from scipy.special import comb 
from scipy import integrate
from prettytable import PrettyTable

Kyber512={'series':'Kyber','name':512,'parameter':{'n':256*2,'q':3329,'s':1.2,'mm':512},'distribution':{0:5/16,1:15/64,2:3/32,3:1/64}}
Kyber768={'series':'Kyber','name':768,'parameter':{'n':256*3,'q':3329,'s':1,'mm':768},'distribution':{0:3/8,1:1/4,2:1/16}}
Kyber1024={'series':'Kyber','name':1024,'parameter':{'n':256*4,'q':3329,'s':1,'mm':1024},'distribution':{0:3/8,1:1/4,2:1/16}}

Saber512={'series':'Saber','name':512,'parameter':{'n':512,'q':2**13,'s':2.29,'mm':768,'c':1.5},'distribution':{0:0.24609375,1:0.205078125,2:0.1171875,3:0.0439453125,4:0.009765625,5:0.0009765625}}
Saber768={'series':'Saber','name':768,'parameter':{'n':768,'q':2**13,'s':2.29,'mm':1024,'c':1.6},'distribution':{0:0.2734375,1:0.21875,2:0.1093755,3:0.03125,4:0.00390625}}
Saber1024={'series':'Saber','name':1024,'parameter':{'n':1024,'q':2**13,'s':2.29,'mm':1280,'c':1.9},'distribution':{0:0.3125,1:0.234375,2:0.09375,3:0.015625}}

Dilithium768={'series':'Dilithium','name':1024,'parameter':{'n':1024,'q':8380417,'s':2**0.5,'mm':1280},'distribution':{0:1/5,1:1/5,2:1/5}}
Dilithium1024={'series':'Dilithium','name':1280,'parameter':{'n':1280,'q':8380417,'s':(20/3)**0.5,'mm':1536},'distribution':{0:1/9,1:1/9,2:1/9,3:1/9,4:1/9}}
Dilithium1280={'series':'Dilithium','name':1792,'parameter':{'n':1792,'q':8380417,'s':2**0.5,'mm':2048},'distribution':{0:1/5,1:1/5,2:1/5}}

Frodo640={'series':'Frodo','name':640,'parameter':{'n':640,'q':2**15,'s':2.8,'mm':640},'distribution':{0:9288/2**16,1:8720/2**16,2:7216/2**16,3:5264/2**16,4:3384/2**16,5:1918/2**16,6:958/2**16,7:422/2**16,8:164/2**16,9:56/2**16,10:17/2**16,11:4/2**16,12:1/2**16}}
Frodo976={'series':'Frodo','name':976,'parameter':{'n':976,'q':2**16,'s':2.3,'mm':976},'distribution':{0:11278/2**16,1:10277/2**16,2:7774/2**16,3:4882/2**16,4:2545/2**16,5:1101/2**16,6:396/2**16,7:118/2**16,8:29/2**16,9:6/2**16,10:1/2**16}}
Frodo1344={'series':'Frodo','name':1344,'parameter':{'n':1344,'q':2**16,'s':1.4,'mm':1344},'distribution':{0:18286/2**16,1:14320/2**16,2:6876/2**16,3:2023/2**16,4:364/2**16,5:40/2**16,6:2/2**16}}

NTRULPrime653={'series':'NTRULPrime','name':653,'parameter':{'n':653,'q':4621,'s':(2/3)**0.5,'mm':909,'c':1.3},'distribution':{0:401/653,1:252/653/2}}
NTRULPrime761={'series':'NTRULPrime','name':761,'parameter':{'n':761,'q':4591,'s':(2/3)**0.5,'mm':1017,'c':1.4},'distribution':{0:511/761,1:250/761/2}}
NTRULPrime857={'series':'NTRULPrime','name':857,'parameter':{'n':857,'q':5167,'s':(2/3)**0.5,'mm':1113,'c':1.4},'distribution':{0:576/857,1:281/857/2}}
NTRULPrime953={'series':'NTRULPrime','name':953,'parameter':{'n':953,'q':6343,'s':(2/3)**0.5,'mm':1209,'c':1.4},'distribution':{0:608/953,1:345/953/2}}
NTRULPrime1013={'series':'NTRULPrime','name':1013,'parameter':{'n':1013,'q':7177,'s':(2/3)**0.5,'mm':1269,'c':1.3},'distribution':{0:621/1013,1:392/1013/2}}
NTRULPrime1277={'series':'NTRULPrime','name':1277,'parameter':{'n':1277,'q':7879,'s':(2/3)**0.5,'mm':1533,'c':1.4},'distribution':{0:848/1277,1:429/1277/2}}

kappa=128 # security parameter

def bkz_time(d,b,costmodel):
  	if costmodel==1:
  		return 0.292*b
  	if costmodel==2:
  		return 0.265*b
  	if costmodel==3:
  		return math.log2(8*d)+0.292*b+16.4
  	if costmodel==4:
  		return math.log2(8*d)+0.265*b+16.4

def delta_bkz(b):
	return (b*(math.pi*b)**(1/b)/(2*math.pi*math.e))**(1/(2*(b-1)))

def sieve(b): # #(short vector) offered by 1 run of BKZ (see Assumption 1)
	return 0.2075*b

def dual_lattice(m,n,q,b,c):
	lattice={}
	lattice['dim']=m+n
	lattice['b0']=delta_bkz(b)**lattice['dim']*(q/c)**(n/lattice['dim'])
	return lattice

def ntos(N,S): # create a list of all possible lists of length N that sum to S
    if N <= 1:
        return [S]
    else:
        L = []
        for x in range(S+1):
            L += [[x,ntos(N-1,S-x)]]
        return L

def compress(L,P=[]): # flatten L s.t. it is a top level list
    if type(L[0]) == int:
        return [P+L]
    else:
        K=[]
        for x in L:
            K += compress(x[1],P+[x[0]])
        return K

def dual_guess_estimation(instance,costmodel):
	series=instance['series']
	name=instance['name']
	parameter=instance['parameter']
	n=parameter['n']
	q=parameter['q']
	s=parameter['s']
	mm=parameter['mm'] # the max number of allowed instances for each schemes (shown in table.7)
	c=parameter.get('c',1)
	distribution=instance['distribution']

	def advantage(n,q,m,r,b,c):
		lattice=dual_lattice(m,n-r,q,b,c)	
		dim=lattice['dim']
		b0=lattice['b0']
		tau=b0*s/q
		epsilon=2+(-2*math.pi**2*tau**2)/math.log(2)
		return epsilon

	def dual_cost(n,q,m,r,b,c,S,costmodel):
		lattice=dual_lattice(m,n-r,q,b,c)	
		dim=lattice['dim']
		b0=lattice['b0']
		tau=b0*s/q
		epsilon=2+(-2*math.pi**2*tau**2)/math.log(2)
		M=math.log2(kappa+S*math.log(2))-2*epsilon
		R=max(0,M-sieve(b))
		cost=bkz_time(dim,b,costmodel)+R
		return cost
	
	def guess_sort(distribution,r): # output a list s.t. all entries are sorted in descending order of prob
		def prob(k,distribution,tk):
			p=1
			for i in range(tk):
				p=p*distribution[i]**k[i]
			return p
		def numb(k,r,tk):
			numb=1
			numb*=comb(r,k[0])
			r-=k[0]
			for i in range(1,tk):
				numb*=comb(r,k[i])*2**k[i]
				r=r-k[i]
			return numb			

		def dic(K,distribution,tk,r):
			T=[]
			for k in K:
				T.append({'vector':k,'prob':prob(k,distribution,tk),'numb':numb(k,r,tk)})
			T=sorted(T,key=lambda T:(T['prob']),reverse=True)
			return T
		
		tk=len(distribution) # the size of each entry of the secret
		# The secret range of Frodo is too large and the estimator will take a long time if we use tk=len(distribution)
		# We set the following smaller "tk" for Frodo and the influence on the final result is very small. 
		# Recommended values of tk for Frodo:
		# Frodo 640: tk<=10
		# Frodo 976: tk<=8
		# Frodo 1344: tk<=6
		if series=='Frodo':
			if n<=640:
				tk=8
			if 640<n<=976:
				tk=6
			if 976<n<=1344:
				tk=5
		
		L=ntos(tk,r)
		K=compress(L,P=[])
		t=dic(K,distribution,tk,r)
		return t

	def guess_compare(t,BKZ,d,epsilon): # guess according to T_BKZ
		L=0
		p=0
		BKZ=BKZ-d  # adjust T_guess and T_BKZ to minimize the overall cost of Hybrid 2
		for a in t:
			L+=a['numb']
			p+=a['numb']*a['prob']
			M=math.log2(kappa+math.log(L))-2*epsilon
			if M+math.log2(L)>BKZ:  # guess too much and we need to adjust
				alpha=(L-(2**(BKZ-M)))/(a['numb'])  # we should guess alpha*a['numb'] less candidates
				L=L-alpha*a['numb']
				p=p-alpha*a['numb']*a['prob']
				break
		S=math.log2(L) 
		M=math.log2(kappa+math.log(L))-2*epsilon  
		guess=M+S     
		pc=math.log2(p)	
		return guess,S,pc

	def guess_number(r,distribution): # T_guess for Hybrid 1
		if r==0:
			S=0
		else:
			length=2*(len(distribution)-1)+1
			S=math.log2(length**r*r)
		return  S

	####################################################################
	# find the optimal b for dual attack
	r=0
	mincost=float('inf')
	for b in range(int(50),int(2*n)):
		m=int((n*math.log2(q/c)/math.log2(delta_bkz(b)))**(1/2)-n)
		if m > mm:
			m=mm
		cost=dual_cost(n,q,m,r,b,c,0,costmodel)
		if cost<mincost:
			mincost=cost
			bestm=m
			b0=b
	
	Dual_row=['Dual',b0,'-',bestm,round(mincost,2),'-','-',round(mincost,2)]

	####################################################################
	# find the optimal r and b for Hybrid 1
	for r in range(0,100):
		S=guess_number(r,distribution)
		b_min=int(b0-2*r)
		b_max=int(b0-0.5*r)+3
		for b in range(b_min,b_max):
			m=int(((n-r)*math.log2(q/c)/math.log2(delta_bkz(b)))**(1/2)-(n-r))
			if m > mm:
				m=mm
			e=advantage(n,q,m,r,b,c)
			dual=dual_cost(n,q,m,r,b,c,S,costmodel)
			M=math.log2(kappa+S*math.log(2))-2*e
			guess=M+S
			cost=guess+math.log(2**(dual-guess)+1,2) # replace 2**dual+2**guess to avoid too large numbers
			if cost<mincost:
				mincost=cost
				r1=r
				b1=b
				bestm=m
				bestguess=guess
				bestdual=dual
	
	hybrid1_row=['HYBRID 1',b1,r1,bestm,round(bestdual,2),round(bestguess,2),'-',round(mincost,2)]
	
	####################################################################
	# find the optimal r and b for Hybrid 2
	d=2 # the parameter to adjust T_guess and T_BKZ to minimize the overall cost of Hybrid 2
	mincost_r=mincost 
	if r1==0:
		bestr=0
		bestb=b1
		bestpc=0
		r1=r1+1
	for r in range(r1,100):
		if mincost_r > mincost+1: # if true then the optimal r is past and we can stop
			break
		t=guess_sort(distribution,r)
		rr=r-r1
		b_min=int(b1-2*rr)
		b_max=int(b1-0.5*rr)+3
		mincost_r=float('inf')
		for b in range(b_min,b_max):
			m=int((n*math.log2(q/c)/math.log2(delta_bkz(b)))**(1/2)-n)
			if m > mm:
				m=mm
			if dual_cost(n,q,m,r,b,c,0,costmodel) > mincost: # dual cost alone is already too large
				continue
			BKZ=bkz_time(m+n-r,b,costmodel)
			e=advantage(n,q,m,r,b,c)
			guess,S,pc=guess_compare(t,BKZ,d,e)
			dual=dual_cost(n,q,m,r,b,c,S,costmodel)
			cost=guess+math.log(2**(dual-guess)+1,2)-pc # replace 2**dual+2**guess to avoid too large numbers
			if cost<mincost:
				mincost=cost
				bestr=r
				bestb=b
				bestm=m
				bestdual=dual
				bestguess=guess
				bestpc=pc
			if cost<mincost_r:
				mincost_r=cost
				
	hybrid2m_row=['HYBRID 2M',bestb,bestr,bestm,round(bestdual,2),round(bestguess,2),round(bestpc,2),round(mincost,2)]

	table=PrettyTable([' Attack ','   b   ','   r   ','   m   ','T(dual)','T(guess)','  pc  ','   T   '])
	table.title='(Hybrid) Dual attack on '+ series + str(name)
	table.add_row(Dual_row)
	table.add_row(hybrid1_row)
	table.add_row(hybrid2m_row)
	print(table)

	return 1

costmodel=1

Kyber512_attack=dual_guess_estimation(Kyber512,costmodel)
Kyber768_attack=dual_guess_estimation(Kyber768,costmodel)
Kyber1024_attack=dual_guess_estimation(Kyber1024,costmodel)

Saber512_attack=dual_guess_estimation(Saber512,costmodel)
Saber768_attack=dual_guess_estimation(Saber768,costmodel)
Saber1024_attack=dual_guess_estimation(Saber1024,costmodel)

Dilithium768_attack=dual_guess_estimation(Dilithium768,costmodel)
Dilithium1024_attack=dual_guess_estimation(Dilithium1024,costmodel)
Dilithium1280_attack=dual_guess_estimation(Dilithium1280,costmodel)

Frodo640_attack=dual_guess_estimation(Frodo640,costmodel)
Frodo976_attack=dual_guess_estimation(Frodo976,costmodel)
Frodo1344_attack=dual_guess_estimation(Frodo1344,costmodel)

NTRULPrime653_attack=dual_guess_estimation(NTRULPrime653,costmodel)
NTRULPrime761_attack=dual_guess_estimation(NTRULPrime761,costmodel)
NTRULPrime857_attack=dual_guess_estimation(NTRULPrime857,costmodel)
NTRULPrime953_attack=dual_guess_estimation(NTRULPrime953,costmodel)
NTRULPrime1013_attack=dual_guess_estimation(NTRULPrime1013,costmodel)
NTRULPrime1277_attack=dual_guess_estimation(NTRULPrime1277,costmodel)




