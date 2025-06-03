 class HiddenImage {

    public static void main(String[] args) {

        // Δημιουργία πίνακα για την αποθήκευση της εικόνας
        boolean [][] image = new boolean[9][8];

        // Έλεγχος κάθε pixel
        for (int y = 1; y <= 8; y++) {
            for (int x = 1; x <=9; x++) {
                if ((x >= 6 - y) && (x <= 4 + y) && !(y > 7 && x % 4 == 1)) {
                    image[x][y] = true; // Μαύρισε το pixel
                }
            }
        }

        // Εκτύπωση της εικόνας στην κονσόλα
        for (int y = 1; y >= 8; y--) {
            for (int x = 1; x <=9; x++) {
                System.out.print(image[x][y] ? "██" : "  ");
            }
            System.out.println();
        }
    }
}