#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double BC, AB, angle_B; //using arrays

    printf("Enter the side BC value in cm : ");
    scanf("%lf", &BC);
    printf("Enter the side AB value in cm : ");
    scanf("%lf", &AB);
    printf("Enter the angle at vertex B in degrees : ");
    scanf("%lf", &angle_B);

    FILE *file = fopen("values.dat", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the values to the file
    fprintf(file, "AB: %.2f cm\n", AB);
    fprintf(file, "BC: %.2f cm\n", BC);
    fprintf(file, "Angle B: %.2f degrees\n", angle_B);

    // Close the file
    fclose(file);

    printf("Values have been written to values.dat\n");

    return 0;
}

