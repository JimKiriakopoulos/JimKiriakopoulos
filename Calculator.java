 class Calculator {
    public static void main(String[] args) {
        // Διαβάζουμε τα επιχειρήματα από τη γραμμή εντολών
        if (args.length != 3) {
            System.out.println("Παρακαλώ παρέχετε τρία δεδομένα: δύο ακέραιους και έναν τελεστή.");
            return;
        }

        // Μετατροπή των πρώτων δύο επιχειρημάτων σε ακέραιους
        int num1 = Integer.parseInt(args[0]);
        int num2 = Integer.parseInt(args[2]);

        // Διαβάζουμε το σύμβολο της πράξης
        String operator = args[1];

        // Υπολογισμός του αποτελέσματος με τη χρήση switch
        double result;
        switch (operator) {
            case "+":
                result = num1 + num2;
                System.out.println(result);
                break;
            case "-":
                result = num1 - num2;
                System.out.println(result);
                break;
            case "x":
                result = num1 * num2;
                System.out.println(result);
                break;
            case "/":
                // Έλεγχος διαίρεσης με το μηδέν
                if (num2 != 0) {
                    result = num1 / (double) num2; // Διαιρούμε με double για να έχουμε ακριβή αποτέλεσμα
                    System.out.println((int) result); // Εκτύπωση της ακέραιας τιμής
                } else {
                    System.out.println("Cannot divide by zero");
                }
                break;
            default:
                System.out.println("Invalid operation");
                break;
        }
    }
}
