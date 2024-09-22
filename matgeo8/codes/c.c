#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

// Include your library headers if necessary
#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double a, A; // Using double variables

    printf("Enter the side value of the rhombus in cm: ");
    scanf("%lf", &a); // Use & to store the input value in the variable
    printf("Enter one of the angles A of the rhombus in degrees: ");
    scanf("%lf", &A); // Use & to store the input value in the variable

    FILE *file = fopen("values.txt", "w"); // Change to .txt file

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the values to the file
    fprintf(file, "side: %.2f cm\n", a);
    fprintf(file, "Angle_1: %.2f degrees\n", A);

    // Close the file
    fclose(file);

    printf("Values have been written to values.txt\n"); // Update message

    return 0;
}

