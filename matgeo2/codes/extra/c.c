#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
	double **A,**B,**P,**M,**Q,**D;
	int x1=2,x2=-7,y1=-2,y2=4;
	M = createMat(2,2);
	A = createMat(2,1);
	B = createMat(2,1);
	P = createMat(2,1);
	Q = createMat(2,1);
	M[0][1] = x1;
	M[1][1] = y1;
	M[0][0] = x2;
	M[1][0] = y2;
	A[0][0] = (float)1/3;
	A[1][0] = (float)2/3;
	B[0][0] = (float)2/3;
	B[1][0] = (float)1/3;
	P = Matmul(M,A,2,2,1);
	Q = Matmul(M,B,2,2,1);
	printf("X coordinate of P: %.02f\n", P[0][0]);
	printf("Y coordinate of P: %.02f\n", P[1][0]);
	printf("X coordinate of Q: %.02f\n", Q[0][0]);
	printf("Y coordinate of Q: %.02f\n", Q[1][0]);
	
	freeMat(M,2);
	freeMat(A,2);
	freeMat(B,2);
	freeMat(P,2);
	freeMat(Q,2);
	return 0;
}
