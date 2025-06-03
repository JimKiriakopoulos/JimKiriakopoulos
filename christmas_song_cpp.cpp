
#include <iostream>
using namespace std;

class ChristmasSong {
public:
    void sing() {
        cout << "Καλά Χριστούγεννα και χρόνια πολλά!" << endl;
        cout << "Υγεία, χαρά και ευτυχία!" << endl;
        cout << "Το νέο έτος να φέρει ειρήνη και αγάπη!" << endl;
        cout << "Καλά Χριστούγεννα και χρόνια πολλά!" << endl;
    }
};

int main() {
    ChristmasSong song;
    song.sing();
    return 0;
}
