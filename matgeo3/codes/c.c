#include <stdio.h>
double det(double a, double b, double c, 
                       double d, double e, double f, 
                       double g, double h, double i) {
    return a * (e * i - f * h) 
         - b * (d * i - f * g) 
         + c * (d * h - e * g);
}
int main() {
    double a, b, c;
    double d, e, f;
    double g, h, i;
    a=2,b=0,c=0,d=1,e=2,f=0,g=0,h=4,i=0;
    double k = det(a, b, c, d, e, f, g, h, i);
    printf("The determinant of the matrix is: %.2f\n", k);

    return 0;
}

