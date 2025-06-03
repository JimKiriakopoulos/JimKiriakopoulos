 class Askisi74 {
    public static void main(String[] args) {
        int sum = 0;

        // Εκτύπωση των δεδομένων εισόδου χωρισμένα με κόμμα
        for (int i = 0; i < args.length; i++) {
            // Εκτυπώνουμε το στοιχείο
            System.out.print(args[i]);

            // Αν δεν είναι το τελευταίο στοιχείο, προσθέτουμε κόμμα
            if (i < args.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println(); // Επιστροφή στη νέα γραμμή μετά την εκτύπωση

        // Υπολογισμός του αθροίσματος
        for (int i = 0; i < args.length; i++) {
            int x = Integer.parseInt(args[i]);
            sum = sum + x;  // Αθροίζουμε την τιμή του x στο sum
        }

        // Εκτύπωση του τελικού αθροίσματος
        System.out.println("Sum is " + sum);
    }
}
