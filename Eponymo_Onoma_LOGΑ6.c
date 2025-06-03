#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Πρωτότυπα συναρτήσεων
void inputNumbers(int *array, int size);
void printNumbers(const int *array, int size);
long long calculateProduct(const int *array, int size);
void checkProductSign(long long product);
bool validateName(char *name);

int main() {
    int N;
    char userName[100]; // Πίνακας για την αποθήκευση του ονόματος του χρήστη
    bool validInput = false;

    // Εισαγωγή ονόματος χρήστη με έλεγχο εγκυρότητας
    printf("Εισάγετε το όνομά σας: ");
    do {
        fgets(userName, sizeof(userName), stdin);
        userName[strcspn(userName, "\n")] = 0; // Αφαίρεση του newline χαρακτήρα
        if(validateName(userName)) {
            validInput = true;
        } else {
            printf("Λάθος εισαγωγή. Παρακαλώ εισάγετε ένα έγκυρο όνομα.\n");
        }
    } while(!validInput);

    // Εισαγωγή αριθμού στοιχείων με έλεγχο εγκυρότητας
    validInput = false;
    while(!validInput) {
        printf("Εισάγετε τον αριθμό των ακεραίων που θέλετε να εισάγετε: ");
        if(scanf("%d", &N) == 1 && N > 0) {
            validInput = true;
        } else {
            printf("Λάθος εισαγωγή. Παρακαλώ εισάγετε έναν θετικό ακέραιο αριθμό.\n");
            // Καθαρισμός του buffer εισόδου
            while(getchar() != '\n');
        }
    }

    // Δημιουργία πίνακα με μέγεθος N
    int numbers[N];

    // Εισαγωγή αριθμών
    inputNumbers(numbers, N);

    // Εμφάνιση αριθμών
    printNumbers(numbers, N);

    // Υπολογισμός γινομένου
    long long product = calculateProduct(numbers, N);

    // Έλεγχος και εμφάνιση προσήμου γινομένου
    checkProductSign(product);

    return 0;
}

// Συνάρτηση για εισαγωγή αριθμών
void inputNumbers(int *array, int size) {
    for(int i = 0; i < size; i++) {
        while(true) {
            printf("Αριθμός %d: ", i + 1);
            if(scanf("%d", &array[i]) == 1) {
                break; // Έξοδος από την επανάληψη αν η εισαγωγή είναι επιτυχής
            } else {
                printf("Λάθος εισαγωγή. Παρακαλώ εισάγετε έναν ακέραιο αριθμό.\n");
                // Καθαρισμός του buffer εισόδου
                while(getchar() != '\n');
            }
        }
    }
}

// Συνάρτηση για εμφάνιση αριθμών
void printNumbers(const int *array, int size) {
    printf("Οι ακέραιοι αριθμοί είναι:\n");
    for(int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// Συνάρτηση για υπολογισμό γινομένου
long long calculateProduct(const int *array, int size) {
    long long product = 1;
    for(int i = 0; i < size; i++) {
        product *= array[i];
    }
    return product;
}

// Συνάρτηση για έλεγχο προσήμου γινομένου
void checkProductSign(long long product) {
    if(product > 0) {
        printf("Το γινόμενο είναι θετικό.\n");
    } else if(product < 0) {
        printf("Το γινόμενο είναι αρνητικό.\n");
    } else {
        printf("Το γινόμενο είναι μηδενικό.\n");
    }
}

// Συνάρτηση για έλεγχο εγκυρότητας ονόματος χρήστη
bool validateName(char *name) {
    // Έλεγχος αν το όνομα είναι κενό ή περιέχει μη-αλφαβητικούς χαρακτήρες
    if(strlen(name) == 0) {
        return false;
    }
    for(int i = 0; name[i] != '\0'; i++) {
        if(!isalpha(name[i]) && name[i] != ' ') {
            return false;
        }
    }
    return true;
}
