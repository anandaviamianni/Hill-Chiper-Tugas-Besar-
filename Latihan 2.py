#key matrix: 
 #a,b,c
 #d,e,f
 #g,h,i
#Modulus 26 stuff so that I get a number between 0-25, so I can convert it to a letter later.  0=A, 1=B,2=C,...25=Z

a = 00 #A
b = 11 #L
c = 15 #P
d = 7 #H
e = 00 #A
f = 1 #B
g = 4 #E
h = 19 #T
i = 00 #A Not enough letters in key.  This is a filler.

determinant = (a*e*i + b*f*g + c*d*h) - (a*f*h + b*d*i + c*e*g)
#Modulus 26 the determinant to make certain that it is only a number between 0-25
determinantmod26 = determinant % 26

#Trial and Error Multiplicative Inverse:May have to add more if number is large enough.
#Need to find formula to solve this.
for x in range(0,1500):
    multiplicativeinversetest = determinantmod26 * x
    if (multiplicativeinversetest % 26) == 1:
        break
multiplicativeinverse = x
#adjugate matrix of key matrix 
 #j,k,l
 #m,n,o
 #p,q,r
j = (e*i) - (f*h)
k = (d*i) - (f*g)
l = (d*h) - (e*g)
m = (b*i) - (c*h)
n = (a*i) - (c*g)
o = (a*h) - (b*g)
p = (b*f) - (c*e)
q = (a*f) - (c*d)
r = (a*e) - (b*d)
#switch signs to find co-factor matrix.
k=-k
m=-m
o=-o
q=-q
#reflect matrix to fix adjugate matrix
reflectk = k
k = m
m = reflectk
reflectl = l
l = p
p = reflectl
reflecto = o
o = q
q = reflecto
#modulus 26 adjugate matrix to be certain we only get numbers from 0-25
j = j % 26
k = k % 26
l = l % 26
m = m % 26
n = n % 26
o = o % 26
p = p % 26
q = q % 26
r = r % 26
#inverse key matrix
 #inversej inversek inversel
 #inversem inversen inverseo
 #inversep inverseq inverser
inversej = j * multiplicativeinverse
inversek = k * multiplicativeinverse
inversel = l * multiplicativeinverse
inversem = m * multiplicativeinverse
inversen = n * multiplicativeinverse
inverseo = o * multiplicativeinverse
inversep = p * multiplicativeinverse
inverseq = q * multiplicativeinverse
inverser = r * multiplicativeinverse
#modulus 26 inverse key matrix to get only numbers 0-25
inversej = inversej % 26
inversek = inversek % 26
inversel = inversel % 26
inversem = inversem % 26
inversen = inversen % 26
inverseo = inverseo % 26
inversep = inversep % 26
inverseq = inverseq % 26
inverser = inverser % 26
#cipher text matrix 
 #aa,bb,cc 
 #dd,ee,ff 
 #gg,hh,ii
aa = 18 #S
dd = 24 #Y
gg = 8  #I
bb = 2 #C
ee = 7 #H
hh = 14 #O
cc = 11 #L
ff = 4 #E
ii = 17 #R
#decode cipher matrix using inverse key matrix. (cipher column*corresponding inverse key matrix row.)  Get plain text matrix
#Plain Text Matrix
 #decodeaa decodebb decodecc
 #decodedd decodeee decodeff
 #decodegg decodehh decodeii
decodeaa = (inversej*aa)+(inversek*dd)+(inversel*gg)
decodedd = (inversem*aa)+(inversen*dd)+(inverseo*gg)
decodegg = (inversep*aa)+(inverseq*dd)+(inverser*gg)
decodebb = (inversej*bb)+(inversek*ee)+(inversel*hh)
decodeee = (inversem*bb)+(inversen*ee)+(inverseo*hh)
decodehh = (inversep*bb)+(inverseq*ee)+(inverser*hh)
decodecc = (inversej*cc)+(inversek*ff)+(inversel*ii)
decodeff = (inversem*cc)+(inversen*ff)+(inverseo*ii)
decodeii = (inversep*cc)+(inverseq*ff)+(inverser*ii)
#modulus 26 plain text to get numbers 0-25, which correspond to letters.
decodeaa = decodeaa % 26
decodedd = decodedd % 26
decodegg = decodegg % 26
decodebb = decodebb % 26
decodeee = decodeee % 26
decodehh = decodehh % 26
decodecc = decodecc % 26
decodeff = decodeff % 26
decodeii = decodeii % 26
print("\n")
print(decodeaa) #22-W
print(decodedd) #04-E
print(decodegg) #00-A
print(decodebb) #17-R
print(decodeee) #04-E
print(decodehh) #18-S
print(decodecc) #00-A
print(decodeff) #05-F
print(decodeii) #04-E