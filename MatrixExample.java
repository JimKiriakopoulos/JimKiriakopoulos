class MatrixExample {
    public static void main(String[] args) {
        // Δημιουργία του πίνακα 2D με 2341 γραμμές και 445 στήλες
        int[][] matrix = new int[2341][445];

        // Διπλός βρόχος για να περάσουμε από όλα τα κελιά του πίνακα
        for (int i = 0; i < matrix.length; i++) {  // Διατρέχουμε τις γραμμές
            for (int j = 0; j < matrix[i].length; j++) {  // Διατρέχουμε τις στήλες
                matrix[i][j] = 5;  // Ανάθεση της τιμής 5 σε κάθε κελί
            }
        }

        // (Προαιρετικό) Εκτύπωση των πρώτων 5 στοιχείων για επαλήθευση
        System.out.println("First element: " + matrix[0][0]);
        System.out.println("Last element: " + matrix[2340][444]);
    }
}