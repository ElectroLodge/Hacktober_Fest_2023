#include <iostream>
#include <cmath>

const double PI = 3.14159;

double calculateArea(double radius) {
    return PI * pow(radius, 2);
}

int main() {
    double radius;

    std::cout << "Enter the radius of the circle: ";
    std::cin >> radius;

    double area = calculateArea(radius);

    std::cout << "The area of the circle is: " << area << std::endl;

    return 0;
}
