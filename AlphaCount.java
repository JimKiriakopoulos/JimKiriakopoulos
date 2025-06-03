 class AlphaCount {
    public static void main(String[] args) {
        // Διαβάζουμε το αλφαριθμητικό από την είσοδο
        String input = args[0];  // Μπορείτε να εισάγετε το αλφαριθμητικό μέσω args[]

        // Μετράμε τους αλφαβητικούς χαρακτήρες
        int alphaCount = 0;
        StringBuilder upperCaseString = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (Character.isLetter(c)) {  // Ελέγχουμε αν ο χαρακτήρας είναι αλφαβητικός
                alphaCount++;
                upperCaseString.append(Character.toUpperCase(c)); // Προσθέτουμε το κεφαλαίο χαρακτήρα
            }
        }
        
         for (int i = 'A'; i <= 'Z'; i++) {
              char c = (char)i;
              System.out.print(c);
              System.out.println(Character.toLowerCase(c));
         }

        // Εκτύπωση αποτελέσματος
        System.out.println("Πλήθος αλφαβητικών χαρακτήρων: " + alphaCount);
        System.out.println("Αλφαριθμητικό με κεφαλαία αλφαβητικά: " + upperCaseString.toString());
    }
}