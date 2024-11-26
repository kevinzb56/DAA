#include <iostream>
#include <vector>
using namespace std;

vector<float> sem; // Vector to store SPI values of each semester

// Function to calculate SPI (Semester Performance Index)
float SPI(int grades[], int credits[], int size) {
    float spi = 0;
    int totalCredits = 0;

    for (int i = 0; i < size; ++i) {
        spi += grades[i] * credits[i];
        totalCredits += credits[i];
    }

    spi = spi / totalCredits;
    sem.push_back(spi); // Store SPI in the vector
    return spi;
}

// Function to calculate CPI (Cumulative Performance Index)
float CPI() {
    float cpi = 0;
    int count = sem.size();

    for (float value : sem) {
        cpi += value;
    }

    return cpi / count;
}

int main() {
    // Data for Semester 1
    int grades1[] = {8, 8, 9, 8, 7};
    int credits1[] = {2, 2, 1, 3, 2};
    int size1 = sizeof(grades1) / sizeof(grades1[0]);

    // Calculate SPI for Semester 1
    float spi1 = SPI(grades1, credits1, size1);
    cout << "The SPI for Semester 1 is " << spi1 << endl;

    // Data for Semester 2
    int grades2[] = {7, 9, 8, 7, 8};
    int credits2[] = {3, 3, 2, 1, 3};
    int size2 = sizeof(grades2) / sizeof(grades2[0]);

    // Calculate SPI for Semester 2
    float spi2 = SPI(grades2, credits2, size2);
    cout << "The SPI for Semester 2 is " << spi2 << endl;

    // Calculate CPI (Cumulative Performance Index)
    float cpi = CPI();
    cout << "The Cumulative Performance Index (CPI) is " << cpi << endl;

    return 0;
}
