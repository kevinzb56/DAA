#include <iostream>
using namespace std;

float SPI(int grades[], int credits[], int size) {
    float spi = 0;
    int totalCredits = 0;

    for (int i = 0; i < size; ++i) {
        spi += grades[i] * credits[i];
        totalCredits += credits[i];
    }

    return spi / totalCredits;
}

int main() {
    int grades[] = {8, 8, 9, 8, 7};
    int credits[] = {2, -2, 1, 3, 2};
    int size = sizeof(grades) / sizeof(grades[0]);

    float spi = SPI(grades, credits, size);
    cout << "The Semester Performance Index (SPI) is " << spi << endl;

    return 0;
}
