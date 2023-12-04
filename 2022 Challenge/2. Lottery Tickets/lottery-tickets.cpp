#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;

int main(){
    ifstream file("lottery-tickets.txt");
    string line;
    int winning[7] = {12, 48, 30, 95, 15, 55, 97};
    int total = 0;
    while (getline(file, line)){
        int winnum = 0;
        string num;
        stringstream ssin(line);
        while (getline(ssin, num, ' ')){
            bool in = (find(begin(winning), end(winning), stoi(num)) != end(winning));
            winnum += int(in);
        }
        switch (winnum){
            case 3:
                total += 1;
                break;
            case 4:
                total += 10;
                break;
            case 5:
                total += 100;
                break;
            case 6:
                total += 1000;
                break;
        }
    }
    file.close();
    cout << total << endl; // Answer: 56
}
