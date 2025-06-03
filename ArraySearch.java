class ArraySearch {
    public static void main(String[] args) {
        // Ορισμός του πίνακα
        int[] myArray = {6, -1, -2, 15, 22, 0, -10, 7};

        // Ελέγχουμε αν υπάρχει δεδομένο στην είσοδο
        if (args.length == 0) {
            System.out.println("Δεν δόθηκε αριθμός.");
            return;
        }

        // Παίρνουμε τον ακέραιο αριθμό από την είσοδο
        int num = Integer.parseInt(args[0]);

        // Αναζητούμε τον αριθμό στον πίνακα
        int position = -1;  // Αν ο αριθμός δεν υπάρχει, θα παραμείνει -1
        for (int i = 0; i < myArray.length; i++) {
            if (myArray[i] == num) {
                position = i;  // Εάν βρούμε τον αριθμό, αποθηκεύουμε τη θέση του
                break;
            }
        }

        // Εκτυπώνουμε το αποτέλεσμα
        System.out.println(position);
    }
}

