#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"


// Function to calculate the determinant of a matrix given by three points
double det(const double p1[], const double p2[], const double p3[]) {
    return p1[0] * (p2[1] * 1 - 1 * p3[1])
         - p1[1] * (p2[0] * 1 - 1 * p3[0])
         + 1 * (p2[0] * p3[1] - p2[1] * p3[0]);
}
float **calcpoints(double **A, double **B, double **AB){
	AB[0][0]= A[0][0]; AB[1][0]= A[1][0]; AB[2][0] = A[2][0];
	AB[0][51]= B[0][0]; AB[1][51]= B[1][0]; AB[2][51] = B[2][0];
        for(int i = 1; i<=50; i+=1){
          float j = (float) i/50;
          AB[0][i]= AB[0][0] + j*(AB[0][51]- AB[0][0]);
          AB[1][i]= AB[1][0] + j*(AB[1][51]- AB[1][0]);
          AB[2][i]= AB[2][0] + j*(AB[2][51]- AB[2][0]);
	}
}
int main() {
    double point1[2], point2[2], point3[2]; //using arrays

    // Input for the first point
    printf("Enter the x coordinate of 1st point: ");
    scanf("%lf", &point1[0]);
    printf("Enter the y coordinate of 1st point: ");
    scanf("%lf", &point1[1]);

    // Input for the second point
    printf("Enter the x coordinate of 2nd point: ");
    scanf("%lf", &point2[0]);
    printf("Enter the y coordinate of 2nd point: ");
    scanf("%lf", &point2[1]);

    // Input for the third point
    printf("Enter the x coordinate of 3rd point: ");
    scanf("%lf", &point3[0]);
    printf("Enter the y coordinate of 3rd point: ");
    scanf("%lf", &point3[1]);

    // Calculate the determinant using the points
    double k = det(point1, point2, point3);

    // Output the result
    printf("The determinant of the matrix is: %.2f\n", k);

    
    
    	double **A,**B,**C,**AB,**CA,**BC;
	A = createMat(3,1);
	B = createMat(3,1);
	C = createMat(3,1);
	AB = createMat(3,52);
	BC = createMat(3,52);
	CA = createMat(3,52);
	A[0][0] = point1[0];
	A[1][0] = point1[1];
	A[2][0] = 0;
	B[0][0] = point2[0];
	B[1][0] = point2[1];
	B[2][0] = 0;
        C[0][0] = point3[0];
        C[1][0] = point3[1];
        C[2][0] = 0;
	//dat file code begins
	calcpoints(A,B,AB);
        calcpoints(B,C,BC);
	calcpoints(C,A,CA);
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "xab yab zab xbc ybc zbc xca yca zca\n");
	
	for(int i=0; i<=51; i+=1){
  	  fprintf(file, "%.02lf %.02lf %.02lf %.02lf %.02lf %.02lf %.02lf %.02lf %.02lf\n", AB[0][i],AB[1][i],AB[2][i], BC[0][i],BC[1][i],BC[2][i],CA[0][i],CA[1][i],CA[2][i]);
	}

	fclose(file);
	printf("Results have been written to values.dat\n");

	freeMat(AB,3);
	freeMat(A,3);
	return 0;
}

