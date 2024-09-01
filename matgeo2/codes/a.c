#include <stdio.h>

// Function to find the points of trisection of a line segment
void find_trisection_points(double x1, double y1, double x2, double y2, double *x1_t, double *y1_t, double *x2_t, double *y2_t) {
    *x1_t = x1 + (x2 - x1) / 3.0;
    *y1_t = y1 + (y2 - y1) / 3.0;
    *x2_t = x1 + 2 * (x2 - x1) / 3.0;
    *y2_t = y1 + 2 * (y2 - y1) / 3.0;
}

