#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[83]:


import datetime
import argparse

#parser
parser = argparse.ArgumentParser()
parser.add_argument("-i")
parser.add_argument("-o")
parser.add_argument("-a")

args = parser.parse_args()
file1Name = args.i
file2Name = args.o
AlgorithmSelect = args.a

#take T
file1 = open(file1Name, 'r')
Lines = file1.readlines()
T=""
count = 0
for line in Lines[1:]:
    count += 1
    T=T+line.strip()
#TAKE P
file1 = open(file2Name, 'r')
Lines = file1.readlines()
P=""
count = 0
for line in Lines[1:]:
    count += 1
    P=P+line.strip()

#take T

count = 0
for line in Lines[1:]:
    count += 1
    T=T+line.strip()

P=""
count = 0
for line in Lines[1:]:
    count += 1
    P=P+line.strip()


def BruteForceMethod(Tsegment,Psegment):
    lengthofT=len(Tsegment)
    lengthofP=len(Psegment)
    isthere=False
    compare=0

    for i in range (0,lengthofT-lengthofP+1):
        y=0
        if(isthere==False):
            for k in range(0,lengthofP):
                compare=compare+1
                if(Psegment[k]==Tsegment[i+k]):
                    y=y+1

                else:
                    break
                if(y==lengthofP):
                    isthere=True
                    s=i
                    break
    if(isthere==False):
        s=("there is none")

    return s + 1,compare


def FailureFunctionKMP(motiv):
    F=[]
    for j in range(0,len(motiv)):
        F.append(0)

    F[0]=0
    j=0
    i=1
    while i<len(motiv):
        if (motiv[i]==motiv[j]):
            F[i]=j+1
            j=j+1
            i=i+1
        elif(j>0):
            j=F[j-1]

        else:
            F[i]=0
            i=i+1
    return F

def KMP(Tsegment,Psegment):
    lengthofT=len(Tsegment)
    lengthofP=len(Psegment)
    F=FailureFunctionKMP(Psegment)
    compare=0
    j=0
    i=0
    while i<lengthofT:
        compare=compare+1
        if (Tsegment[i]==Psegment[j]):
            if(j==lengthofP-1):
                s=i-j
                return s + 1,compare
            else:
                j=j+1
                i=i+1
        else:
            if(j>0):
                j=F[j-1]

            else:
                i=i+1
                j=0
    s="no match"
    return s+1,compare

def BadCharMatrix(motiv):
    rows,cols = (len(motiv), 4)
    badmatrix = [[-1 for i in range(cols)] for j in range(rows)]


    for i in range(0,len(motiv)):
        A=True
        C=True
        G=True
        T=True
        motiveinterval=motiv[0:i+1]
        for j in range(0,len(motiveinterval)):

            if(motiveinterval[len(motiveinterval)-j-1]=="A" and A):
                badmatrix[i][0]=len(motiveinterval)-j-1
                A=False

            if(motiveinterval[len(motiveinterval)-j-1]=="C" and C):
                badmatrix[i][1]=len(motiveinterval)-j-1
                C=False
            if(motiveinterval[len(motiveinterval)-j-1]=="G" and G):
                badmatrix[i][2]=len(motiveinterval)-j-1
                G=False
            if(motiveinterval[len(motiveinterval)-j-1]=="T" and T):
                badmatrix[i][3]=len(motiveinterval)-j-1
                T=False

    return badmatrix

def GoodSuffixRule(motiv):
    rows, cols = (3, len(motiv))
    goodsuffix = [[0 for i in range(cols)] for j in range(rows)]
    length=len(motiv)
    #GOOD SUUFİX RULE 1
    for j in range(0,length):
        init=0
        search=motiv[j+1:length]

        for k in range(0,length):
            if(search==motiv[k-len(search):k] and motiv[k-length+j]!=motiv[j]and (length-j)<=k and k<length and k>init and j!=length-1):
                goodsuffix[0][j]=k
                init=k

    #GOOD SUUFİX RULE 2
    for j in range(0,length):
        init=0
        for k in range(0,length):
            search2=motiv[0:k]
            if(motiv[length-len(search2):length]==search2 and 1<=k and k<=length-j-1 and j!=length-1 and k>init):

                goodsuffix[1][j]=k
                init=k

    #good suffix rule 3 GS
    for x in range(0,length):
        goodsuffix[2][x]=length-max(goodsuffix[0][x],goodsuffix[1][x])
    goodsuffix[2][length-1]=1

    return goodsuffix[2]
#Boyer--------
def Boyer(T,P):
    GS=GoodSuffixRule(P)
    j=0
    jbad=0
    jgood=0
    BC=BadCharMatrix(P)

    compare=0
    isthere=False
    control=True
    while j<len(T)-len(P)+1 and not(isthere) and control:
        tocompare=T[j:j+len(P)]
        k=len(P)-1
        while k>=0:
            compare=compare+1
            if(P[k]==tocompare[k]):
                k=k-1

            else:


                if(tocompare[k]=="A"):
                    col=0
                if(tocompare[k]=="C"):
                    col=1
                if(tocompare[k]=="G"):
                    col=2
                if(tocompare[k]=="T"):
                    col=3

                jbad=k-BC[k][col]
                jgood=GS[k]
                if(jbad>jgood):
                    j=j+jbad
                else:
                    j=j+jgood
                break

            if(k==-1):
                s=j
                isthere=True

    if(isthere==False):
        s="there is none"
    return s+1,compare














if(AlgorithmSelect=="BF"):
    start_time = datetime.datetime.now()
    result=BruteForceMethod(T,P)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.microseconds
    print("pattern was found in query file at position ",result[0],".")
    print(result[1]," character comparisons performed .")
    print("Run time was ",execution_time,"ms.")
elif(AlgorithmSelect=="KMP"):
    start_time = datetime.datetime.now()
    result=KMP(T,P)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.microseconds
    print("pattern was found in query file at position ",result[0],".")
    print(result[1]," character comparisons performed .")
    print("Run time was ",execution_time,"ms.")
elif(AlgorithmSelect=="BM"):
    start_time = datetime.datetime.now()
    result=Boyer(T,P)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.microseconds
    print("pattern was found in query file at position ",result[0],".")
    print(result[1]," character comparisons performed .")
    print("Run time was ",execution_time,"ms.")
elif(AlgorithmSelect=="A"):
    print("Brute Force :")
    start_time = datetime.datetime.now()
    result=BruteForceMethod(T,P)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.microseconds
    print("pattern was found in query file at position ",result[0],".")
    print(result[1]," character comparisons performed .")
    print("Run time was ",execution_time,"ms.")
    BFResult=execution_time
    print("")

    print("Knuth - Morris - Pratt :")
    start_time = datetime.datetime.now()
    result=KMP(T,P)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.microseconds
    print("pattern was found in query file at position ",result[0],".")
    print(result[1]," character comparisons performed .")
    print("Run time was ",execution_time,"ms.")
    KMPResult=execution_time
    print("")

    print("Boyer - Moore:")
    start_time = datetime.datetime.now()
    result=Boyer(T,P)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.microseconds
    print("pattern was found in query file at position ",result[0],".")
    print(result[1]," character comparisons performed .")
    print("Run time was ",execution_time,"ms.")
    BoyerResult=execution_time
    complist=[BFResult,KMPResult,BoyerResult]
    complist=sorted(complist)
    if(BFResult==complist[0]):
        print("BruteForce was the best method")
    elif(KMPResult==complist[0]):
        print("Knuth - Morris - Pratt was the best method")
    elif(BoyerResult==complist[0]):
        print("Boyer - Moore was the best method")


# In[ ]:
