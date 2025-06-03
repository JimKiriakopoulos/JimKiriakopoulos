#include <stdio.h>

// Υλοποίηση του Bubble Sort
void bubbleSort(int array[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                // Ανταλλαγή στοιχείων
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

int main() {
    int data[] = { -2, 45, 0, 11, -9 };
    int n = sizeof(data) / sizeof(data[0]);
    bubbleSort(data, n);
    
    printf("Ταξινομημένος πίνακας σε αύξουσα σειρά:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");
    return 0;
}
