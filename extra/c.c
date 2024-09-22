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
    float rain_velocity, bike_velocity, angle;
    FILE *file;

    // Prompt the user for inputs
    printf("Enter the rain velocity (m/s): ");
    scanf("%f", &rain_velocity);
    printf("Enter the bicycle velocity (m/s): ");
    scanf("%f", &bike_velocity);

    // Open the file for writing
    file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    // Write the results to the file
    fprintf(file, "Rain Velocity: %.2f m/s\n", rain_velocity);
    fprintf(file, "Bicycle Velocity: %.2f m/s\n", bike_velocity);
    // Close the file
    fclose(file);
    printf("Results written to output.dat\n");
    return 0;
}

