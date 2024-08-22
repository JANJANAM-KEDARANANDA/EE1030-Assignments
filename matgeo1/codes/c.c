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
	double **k,**M,**C;
	int x1=0,x2=0,y1=9,y2=0;
	M = createMat(2,2);
	k = createMat(2,1);
	C = createMat(2,1);
	M[0][1] = x1;
	M[1][1] = y1;
	M[0][0] = x2;
	M[1][0] = y2;
	k[0][0] = (float)1/3;
	k[1][0] = (float)2/3;
	C = Matmul(M,k,2,2,1);
	//printf("X coordinate of C: %.02f\n", C[0][1]);
	//printf("Y coordinate of C: %.02f\n", C[1][1]);
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x\ty\t of C\n");
	fprintf(file, "%.02lf\t", C[0][0]);
	fprintf(file, "%.02lf", C[1][0]);

	fclose(file);
	printf("Results have been written to values.dat\n");

	freeMat(M,2);
	freeMat(k,2);
	freeMat(C,2);
	return 0;
}
