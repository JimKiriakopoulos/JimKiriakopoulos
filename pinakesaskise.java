class PinakesAskise {
    public static void main(String[] args) {
        // Ελέγχουμε αν υπάρχουν δεδομένα στην είσοδο
        if (args.length == 0) {
            System.out.println("Δεν έχουν εισαχθεί δεδομένα.");
            return;
        }

        // Δημιουργούμε έναν πίνακα από τα δεδομένα εισόδου
        int[] myArray = new int[args.length];

        // Γεμίζουμε τον πίνακα με τα δεδομένα εισόδου
        for (int i = 0; i < args.length; i++) {
            try {
                myArray[i] = Integer.parseInt(args[i]);
            } catch (NumberFormatException e) {
                System.out.println("Μη έγκυρο δεδομένο: " + args[i]);
                return; // Αν δεν είναι ακέραιο, σταματάμε την εκτέλεση
            }
        }

        // Εκτύπωση των στοιχείων του πίνακα
        System.out.print("Τα στοιχεία του πίνακα: ");
        for (int number : myArray) {
            System.out.print(number + " ");
        }
        System.out.println();

        // Υπολογισμός του μέσου όρου
        int sum = 0;
        for (int number : myArray) {
            sum += number;
        }
        double average = (double) sum / myArray.length;
        System.out.println("Ο μέσος όρος των ακεραίων είναι: " + average);

        // Υπολογισμός του πλήθους των αρνητικών ακεραίων
        int negativeCount = 0;
        for (int number : myArray) {
            if (number < 0) {
                negativeCount++;
            }
        }
        System.out.println("Πλήθος αρνητικών ακεραίων: " + negativeCount);
    }
}
