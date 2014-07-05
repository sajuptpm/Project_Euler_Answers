#!/usr/bin/env python
#coding:utf-8

"""
Convergents of e

The square root of 2 can be written as an infinite continued fraction.

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].
It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.

Hence the sequence of the first ten convergents for √2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

"""
def i_add_f(i,f):
    return [f[0]+i*f[1],f[1]]

def anti_Continued_Fractions(arr):
    if len(arr)==1: return [arr[0],1]
    return i_add_f(arr[0],anti_Continued_Fractions(arr[1:])[::-1])

def anwser():
    e=[2]
    for i in xrange(33):
        e.extend([1,2*(i+1),1])
    print sum([int(i) for i in list(str(anti_Continued_Fractions(e)[0]))])

import time
tStart=time.time()
anwser()
print 'run time=',time.time()-tStart
# 272
# run time= 0.000308990478516