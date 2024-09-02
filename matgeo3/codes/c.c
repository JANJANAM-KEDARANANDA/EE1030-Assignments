#include <stdio.h>
double det(double a, double b, 
                       double d, double e, 
                       double g, double h) {
    return a * (e * 1 - 1 * h) 
         - b * (d * 1 - 1 * g) 
         + 1 * (d * h - e * g);
}
int main() {
    double a, b;
    double d, e;
    double g, h;
    printf("enter the x coordinate of 1st point : ");
    scanf("%lf",&a);
    printf("enter the x coordinate of 1st point : ");
    scanf("%lf",&b);
    printf("enter the x coordinate of 2nd point : ");
    scanf("%lf",&d);
    printf("enter the x coordinate of 2nd point : ");
    scanf("%lf",&e);
    printf("enter the x coordinate of 3rd point : ");
    scanf("%lf",&g);
    printf("enter the x coordinate of 3rd point : ");
    scanf("%lf",&h);
    double k = det(a, b,d, e, g, h);
    printf("The determinant of the matrix is : %.2f\n", k);

    return 0;
}

