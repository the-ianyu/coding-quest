#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
    ifstream file("engine-diagnostics.txt");
    string line;
    int content[86400], i = 0, r_av = 0;
    while (getline(file, line)){
        content[i] = stoi(line);
        if (++i >= 60) {
            int sum = 0;
            for (int j = i-60; j < i; j++){
                sum += content[j];
            }
            if (sum < 90000 || sum > 96000) {
                ++r_av;
            }
        }
    }
    file.close();
    cout << r_av; // Answer: 6248
}
