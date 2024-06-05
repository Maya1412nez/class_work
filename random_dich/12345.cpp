#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int n, x;
    int count62 = 0;
    int countnot62 = 0;
    int count31_not2 = 0;
    int count2_not31 = 0;

    ifstream in("27.txt");
    in >> n;
    for (int i=0; i <n; i++) {
        in >> x;
        if (x % 62 == 0)
            count62 += 1;
        if (x % 62 != 0)
            countnot62 += 1;
        if (x % 31 == 0 and x % 2 != 0)
            count31_not2 += 1;
        if (x % 2 == 0 and x % 31 != 0)
            count2_not31 += 1;
    }
   cout << count62 * countnot62 + count31_not2 * count2_not31 + count62 * (count62 - 1) / 2;

    return 0;
}
