#include <iostream>
using namespace std;

int main() {
    // Δημιουργία δύο 2x2 πινάκων
    int A[2][2], B[2][2], result[2][2];

    // Εισαγωγή των στοιχείων του πίνακα A
    cout << "Eisage stoixeia ston pinaka a:" << endl;
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            cin >> A[i][j];
        }
    }

    // Εισαγωγή των στοιχείων του πίνακα B
    cout << "Eisage stoixeia ston pinaka b:" << endl;
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            cin >> B[i][j];
        }
    }

    // Υπολογισμός του προϊόντος των δύο πινάκων
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            result[i][j] = 0; // Αρχικοποίηση του αποτελέσματος
            for(int k = 0; k < 2; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // Εμφάνιση του αποτελέσματος
    cout << "To apotelesma tvn praseon einai:" << endl;
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}