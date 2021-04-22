############### compare version numbers ################


def compareVersion(self, A, B):
	A=input()
	B=input()
    A=A.split(".")
    B=B.split(".")
    if len(A)>len(B):
        max1=len(A)
    else:
        max1=len(B)
    for j in range(max1):
        if j <len(A):
            v1=int(A[j])
        else:
            v1=0
        if j<len(B):
            v2=int(B[j])
        else:
            v2=0
        if v1>v2:
            return 1
        elif v1<v2:
            return -1
    return 0

compareVersion(A,B)

########################################################