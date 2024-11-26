#include <iostream>
#include <vector>
using namespace std;

vector<float> sem; // To store SPI for each semester

// Function to calculate SPI for a semester
float SPI(const vector<int>& grades, const vector<int>& credits) {
    float spi = 0;
    int totalCredits = 0;
    for (int i = 0; i < grades.size(); ++i) {
        spi += grades[i] * credits[i];
        totalCredits += credits[i];
    }
    spi = spi / totalCredits;
    sem.push_back(spi);
    return spi;
}

// Function to calculate CPI from all SPIs
float CPI() {
    float cpi = 0;
    int count = sem.size();
    for (float value : sem) {
        cpi += value;
    }
    return cpi / count; // Return the average of all SPIs
}

int main() {
    // Example: Two semesters of grades and credits
    vector<vector<int>> allGrades = {
        {8, 8, 9, 8, 7}, // Semester 1
        {9, 7, 8, 8, 6}  // Semester 2
    };

    vector<vector<int>> allCredits = {
        {2, 2, 1, 3, 2}, // Semester 1
        {3, 2, 2, 3, 1}  // Semester 2
    };

    // Calculate and display SPI for each semester
    for (int i = 0; i < allGrades.size(); ++i) {
        float spi = SPI(allGrades[i], allCredits[i]);
        cout << "The Semester Performance Index (SPI) for semester " << i + 1 << " is " << spi << endl;
    }

    // Calculate and display CPI
    float cpi = CPI();
    cout << "The Cumulative Performance Index (CPI) is " << cpi << endl;

    return 0;
}
