# 242 chars
from math import prod;p=[]
for l in set(open('in.txt','r+').readlines()):
    c=','.join(' '.join(l.split()[2:]).split(';')).split(',');m=[0]*3
    for s in c:s=s.split();m[i]=max(m[i:=ord(s[1][0])%3],int(s[0]))
    p+=[prod(m)]
print(sum(p))

# im angry this isn't actually shorter, but it has less whitespace (255 chars)
from math import prod;p=[]
for l in set(open('in.txt','r+').readlines()):c=[s.split()for s in','.join(' '.join(l.split()[2:]).split(';')).split(',')];m=[[],[],[]];set(map(lambda s:m[ord(s[1][0])%3].append(int(s[0])),c));p+=[prod(map(max,m))]
print(sum(p))
