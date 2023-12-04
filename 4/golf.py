# p1 - 240 chars
import itertools as i;print(sum([int(2**(len(m)-1))for m in list(map(lambda g:[n[0]for n in i.product(g[0],g[1])if n[0]==n[1]],[[set(map(int,n.split()))for n in l.split(':')[1].split('|')]for l in set(open('in.txt','r+').readlines())]))]))

# p2 - 331 chars
import itertools as i;import numpy as y;j=0;n=y.ones(len(c:=list(map(len,list(map(lambda g:[n[0]for n in i.product(g[0],g[1])if n[0]==n[1]],[[set(map(int,n.split()))for n in l.split(':')[1].split('|')]for l in list(open('in.txt','r+').readlines())]))))),dtype=y.uint)
for k in c:n[j+1:j+k+1]+=y.full(k,n[j]);j+=1
print(sum(n))
