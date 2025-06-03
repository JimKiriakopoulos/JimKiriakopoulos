class FibonacciArray {
    public static void main(String[] args) {
        // Δημιουργία πίνακα με 15 θέσεις
        int[] fibonacci = new int[15];

        // Αρχικοποιούμε τα δύο πρώτα στοιχεία της ακολουθίας Fibonacci
        fibonacci[0] = 1;
        fibonacci[1] = 1;

        // Υπολογισμός των υπόλοιπων στοιχείων της ακολουθίας Fibonacci
        for (int i = 2; i < fibonacci.length; i++) {
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
        }

        // Εκτύπωση του πίνακα για να επαληθεύσουμε τα στοιχεία
        System.out.print("Ακολουθία Fibonacci: ");
        for (int i = 0; i < fibonacci.length; i++) {
            System.out.print(fibonacci[i] + " ");
        }
    }
}
