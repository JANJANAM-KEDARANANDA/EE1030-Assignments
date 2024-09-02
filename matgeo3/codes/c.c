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

    
    
    	double **A,**B,**C;
	A = createMat(2,1);
	B = createMat(2,1);
	C = createMat(2,1);
	A[0][0] = point1[0];
	A[1][0] = point1[1];
	B[0][0] = point2[0];
	B[1][0] = point2[1];
        C[0][0] = point3[0];
        C[1][0] = point3[1];
	//dat file code begins
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x y\n");
	fprintf(file, "%.02f %.02f\n", A[0][0],A[1][0]);
	fprintf(file, "%.02f %.02f\n", B[0][0],B[1][0]);
	fprintf(file, "%.02f %.02f\n", C[0][0],C[1][0]);

	fclose(file);
	// end
	printf("Results have been written to values.dat\n");

	freeMat(A,2);
	freeMat(B,2);
	freeMat(C,2);
	return 0;
}

