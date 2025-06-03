#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Δήλωση της δομής για τα βιβλία
typedef struct {
    char title[100];
    char author[100];
    char ISBN[20];
    int loaned; // 0 για διαθέσιμο, 1 για δανεισμένο
} Book;

// Πρωτότυπα συναρτήσεων
void addBook(Book **library, int *count);
void searchBooks(Book *library, int count);
void loanBook(Book *library, int count);
void returnBook(Book *library, int count);
void displayBooks(Book *library, int count);
void saveLibrary(Book *library, int count);
void loadLibrary(Book **library, int *count);

int main() {
    Book *library = NULL;
    int count = 0;
    int choice;

    // Φόρτωση της βιβλιοθήκης από αρχείο
    loadLibrary(&library, &count);

    // Μενού επιλογών
    do {
        printf("1. Προσθήκη βιβλίου\n");
        printf("2. Αναζήτηση βιβλίων\n");
        printf("3. Δανεισμός βιβλίου\n");
        printf("4. Επιστροφή βιβλίου\n");
        printf("5. Εμφάνιση διαθέσιμων βιβλίων\n");
        printf("6. Αποθήκευση και έξοδος\n");
        printf("0. Έξοδος χωρίς αποθήκευση\n");
        printf("Επιλέξτε μια επιλογή: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addBook(&library, &count);
                break;
            case 2:
                searchBooks(library, count);
                break;
            case 3:
                loanBook(library, count);
                break;
            case 4:
                returnBook(library, count);
                break;
            case 5:
                displayBooks(library, count);
                break;
            case 6:
                saveLibrary(library, count);
                // Πτώση μέσω για έξοδο
            case 0:
                break;
            default:
                printf("Μη έγκυρη επιλογή.\n");
        }
    } while (choice != 0);

    // Απελευθέρωση της μνήμης που δεσμεύτηκε για τη βιβλιοθήκη
    free(library);

    return 0;
}

// Υλοποίηση των συναρτήσεων...
// Συνάρτηση για την αναζήτηση βιβλίων
void searchBooks(Book *library, int count) {
    char keyword[100];
    printf("Εισάγετε τον τίτλο, τον συγγραφέα ή το ISBN για αναζήτηση: ");
    scanf("%99s", keyword);
    for (int i = 0; i < count; i++) {
        if (strstr(library[i].title, keyword) || strstr(library[i].author, keyword) || strcmp(library[i].ISBN, keyword) == 0) {
            printf("Βιβλίο βρέθηκε: %s, %s, ISBN: %s\n", library[i].title, library[i].author, library[i].ISBN);
        }
    }
}

// Συνάρτηση για τον δανεισμό βιβλίων
void loanBook(Book *library, int count) {
    char ISBN[20];
    printf("Εισάγετε το ISBN του βιβλίου που θέλετε να δανειστείτε: ");
    scanf("%19s", ISBN);
    for (int i = 0; i < count; i++) {
        if (strcmp(library[i].ISBN, ISBN) == 0 && library[i].loaned == 0) {
            library[i].loaned = 1;
            printf("Το βιβλίο δανείστηκε επιτυχώς.\n");
            return;
        }
    }
    printf("Το βιβλίο δεν είναι διαθέσιμο για δανεισμό.\n");
}

// Συνάρτηση για την επιστροφή βιβλίων
void returnBook(Book *library, int count) {
    char ISBN[20];
    printf("Εισάγετε το ISBN του βιβλίου που επιστρέφετε: ");
    scanf("%19s", ISBN);
    for (int i = 0; i < count; i++) {
        if (strcmp(library[i].ISBN, ISBN) == 0 && library[i].loaned == 1) {
            library[i].loaned = 0;
            printf("Το βιβλίο επιστράφηκε επιτυχώς.\n");
            return;
        }
    }
    printf("Δεν βρέθηκε δανεισμένο βιβλίο με αυτό το ISBN.\n");
}

// Συνάρτηση για την εμφάνιση όλων των διαθέσιμων βιβλίων
void displayBooks(Book *library, int count) {
    printf("Διαθέσιμα βιβλία:\n");
    for (int i = 0; i < count; i++) {
        if (library[i].loaned == 0) {
            printf("%s, %s, ISBN: %s\n", library[i].title, library[i].author, library[i].ISBN);
        }
    }
}

// Συνάρτηση για την αποθήκευση της βιβλιοθήκης σε αρχείο
void saveLibrary(Book *library, int count) {
    FILE *file = fopen("library.dat", "wb");
    if (file == NULL) {
        printf("Σφάλμα κατά το άνοιγμα του αρχείου.\n");
        return;
    }
    fwrite(library, sizeof(Book), count, file);
    fclose(file);
    printf("Η βιβλιοθήκη αποθηκεύτηκε επιτυχώς.\n");
}

// Συνάρτηση για τη φόρτωση της βιβλιοθήκης από αρχείο
void loadLibrary(Book **library, int *count) {
    FILE *file = fopen("library.dat", "rb");
    if (file == NULL)