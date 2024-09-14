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
	double **A,**B, **C,**D;
	A = createMat(3,1);
	B = createMat(3,1);
  	C = createMat(3,1);
	A[0][0] = 1;
	A[1][0] = 0;
  	A[2][0] = 0;
	B[0][0] = (double)-1/2;
	B[1][0] = (double)sqrt(3)/2;
  	B[2][0] = 0;
        C = Matscale(Matadd(A,B,3,1),3,1,(double) 1/Matnorm(Matadd(A,B,3,1),3));
        D = Matscale(Matsub(A,B,3,1),3,1,(double) 1/Matnorm(Matadd(A,B,3,1),3));
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x\ty\tz\n");
	fprintf(file, "%.02lf\t%.02lf\t%.02f\n", A[0][0],A[1][0],A[2][0]);
	fprintf(file, "%.02lf\t%.02lf\t%.02f\n", B[0][0],B[1][0],B[2][0]);
    	fprintf(file, "%.02lf\t%.02lf\t%.02f\n", C[0][0],C[1][0],C[2][0]);
    	fprintf(file, "%.02lf\t%.02lf\t%.02f\n", D[0][0],D[1][0],D[2][0]);
	fclose(file);
	printf("Results have been written to values.dat\n");
	printf("%.02lf\t%.02lf\t%.02f\tA+B\n", C[0][0],C[1][0],C[2][0]);
	printf("%.02lf\t%.02lf\t%.02f\tA-B\n", D[0][0],D[1][0],D[2][0]);

	freeMat(A,2);
	freeMat(B,2);
	return 0;
}
