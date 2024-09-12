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
	double **A,**B,**P,**M,**k;
	A = createMat(3,1);
	B = createMat(3,1);
	int x1=-2,x2=6,y1=0,y2=0,z1=0,z2=0;
	M = createMat(3,2);
	k = createMat(3,1);
	P = createMat(3,1);
	M[0][0] = x1;
	M[1][0] = y1;
	M[2][0] = z1;
	M[0][1] = x2;
	M[1][1] = y2;
	M[2][1] = z2;
	k[0][0] = (float)1/2;
	k[1][0] = (float)1/2;
	k[2][0] = (float)1/2;
	P = Matmul(M,k,3,2,1);
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x\ty\tz\t of P\n");
	fprintf(file, "%.02lf\t", P[0][0]);
	fprintf(file, "%.02lf\t", P[1][0]);
	fprintf(file, "%.02lf\t", P[2][0]);

	fclose(file);
	printf("Results have been written to values.dat\n");

	freeMat(M,2);
	freeMat(k,2);
	freeMat(P,2);
	return 0;
}
