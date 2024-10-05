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
    FILE *file;
    file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1; // Return error code if file couldn't be opened
    }

    // Ellipse parameters
    double a = 4.0; // semi-major axis
    double b = 2.0; // semi-minor axis

    // Store the parameters
    fprintf(file, "%lf\n%lf\n%lf\n%lf\n", a, b, 0.0, 0.0); // a, b, h, k

    fclose(file); // Close the file
    return 0; // Return success
}

