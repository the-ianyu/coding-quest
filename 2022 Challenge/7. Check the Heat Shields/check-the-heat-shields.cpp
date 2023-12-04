// #include <iostream>
// #include <fstream>
// #include <sstream>
// #include <string>
// #include <set>
// using namespace std;
// typedef pair<int, int> pairs;

// int main(){
//     int arr[10000][4];
//     int grid_size[2] = {20000, 100000};
//     // --------------------
//     ifstream file("check-the-heat-shields.txt");
//     int i = 0;
//     string line, num;
//     while (getline(file, line)) {
//         int j = 0;
//         stringstream ssin(line);
//         while (getline(ssin, num, ' ')){
//             arr[i][j] = stoi(num);
//             j++;
//         }
//         i++;
//     }
//     file.close();
//     set<pair<int, int>>final;
//     for (int i = 0; i < (sizeof(arr)/sizeof(arr[0])); i++) {
//         for (int j = arr[i][0]; j < arr[i][0]+arr[i][2]; j++) {
//             for (int k = arr[i][1]; k < arr[i][1]+arr[i][3]; k++) {
//                 pairs x = make_pair(j, k);
//                 final.insert(x);
//             }
//         }
//         cout << "Line " << i+1 << " processed." << endl; // DEBUG LINE
//     }
//     cout << "Answer: " << grid_size[0]*grid_size[1]-final.size();
// }
