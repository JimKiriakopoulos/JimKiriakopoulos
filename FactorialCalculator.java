public class FactorialCalculator {
    public static void main(String[] args) {
        // Διαβάζουμε τον αριθμό από τα επιχειρήματα
        if (args.length < 1) {
            System.out.println("Παρακαλώ παρέχετε έναν αριθμό.");
            return; // Τερματίζουμε την εκτέλεση του προγράμματος αν δεν υπάρχουν επιχειρήματα
        }
        
        int n = Integer.parseInt(args[0]);  // Μετατροπή του πρώτου επιχειρήματος σε ακέραιο αριθμό

        // Έλεγχος αν ο αριθμός είναι αρνητικός
        if (n < 0) {
            System.out.println("Undefined");
        } else {
            // Υπολογισμός παραγοντικού για n >= 0
            long factorial = 1;
            for (int i = 1; i <= n; i++) {
                factorial *= i;  // Ενημερώνουμε το παραγοντικό
            }

            // Εμφάνιση του παραγοντικού
            System.out.println("Το παραγοντικό του " + n + " είναι: " + factorial);
            
            // Εμφάνιση πολλαπλασίων του 5 από το 5 έως το 100
            for (int i = 5; i <= 100; i += 5) {
                System.out.println(i);
            }

            // Εμφάνιση πολλαπλασίων του 5 ξεκινώντας από το παραγοντικό
            int start = (int) factorial;  // Χρησιμοποιούμε την τιμή του παραγοντικού για την αρχική τιμή του i
            while (start <= 100) {
                System.out.println(start);
                start += 5; // Αύξηση κατά 5 για το επόμενο πολλαπλάσιο
            }

            // Εμφάνιση των πολλαπλασίων του 5 με τη χρήση do-while
            do {
                System.out.println(start);
                start += 5; // Αύξηση κατά 5 για το επόμενο πολλαπλάσιο
            } while (start <= 100);

            // Ελέγχουμε την ακτίνα για την υπολογισμό της περιμέτρου και του εμβαδού
            double radius = 10.0;  // Μπορείτε να αλλάξετε αυτήν την τιμή
            if (radius < 0) {
                System.out.println("Invalid radius");
            } else {
                // Υπολογισμός της περιμέτρου και του εμβαδού
                double perimeter = 2 * Math.PI * radius;
                double area = Math.PI * radius * radius;

                // Εκτύπωση των αποτελεσμάτων
                System.out.println("Perimeter: " + perimeter);
                System.out.println("Area: " + area);
            }

            // Υπολογισμός του sum και εκτύπωση με ακρίβεια
            double sum = 0.0;
            while (sum < 4.0) {
                sum += 0.1;
            }
            System.out.printf("%.1f\n", sum);

            // Διόρθωση για την ακριβή εκτύπωση του sum με μικρό σφάλμα
            sum = 0.0;
            while (Math.abs(sum - 4.0) > 0.0000001) { // Σταματάει όταν το sum είναι πολύ κοντά στο 4.0
                sum += 0.1;
            }
            System.out.println(sum);

            // Εμφάνιση του πίνακα πολλαπλασίων του 7
            for (int j = 1; j <= 10; j++) {
                System.out.printf("7 x %d = %d\n", j, 7 * j);
            }

            // Εμφάνιση των αριθμών από 1 έως 10
            for (int k = 1; k <= 10; k++) {
                System.out.print(k + " ");
            }
            System.out.println(); // Επιστροφή στην επόμενη γραμμή

            // Εμφάνιση αριθμών από 1 έως 50 με αλλαγή γραμμής κάθε 10 αριθμούς
            for (int m = 1; m <= 50; m++) {
                System.out.print(m + " ");
                if (m % 10 == 0) {
                    System.out.println();
                }
            }

            // Εκτύπωση αριθμών σε γραμμές με αύξηση από 1 έως 5
            int count = 1;
            for (int i = 1; i <= 5; i++) {
                for (int j = 0; j < i; j++) {
                    if (count <= 50) {
                        System.out.print(count + " ");
                        count++;
                    }
                }
                System.out.println(); // Νέα γραμμή μετά από κάθε σειρά
            }

            // Υπολογισμός του πρώτου αριθμού για τις συνθήκες
            int L = 1;
            while (true) {
                if (L % 18 == 3 && L % 12 == 4 && L % 7 == 5) {
                    System.out.println("Ο αριθμός των λιρών είναι: " + L);
                    break; // Εάν βρούμε την σωστή τιμή, βγαίνουμε από τον βρόχο
                }
                L++; // Αυξάνουμε το L και ελέγχουμε την επόμενη τιμή
            }

            // Υπολογισμός των ριζών μιας εξίσωσης δευτέρου βαθμού
            double a = 1.0, b = -3.0, c = 2.0;  // Παραδείγματα τιμών για το a, b και c
            double discriminant = b * b - 4 * a * c;

            if (discriminant > 0) {
                double x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
                double x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
                System.out.println("Οι ρίζες είναι: x1 = " + x1 + ", x2 = " + x2);
            } else if (discriminant == 0) {
                double x = -b / (2 * a);
                System.out.println("Η ρίζα είναι: x = " + x);
            } else {
                System.out.println("Η εξίσωση δεν έχει πραγματικές ρίζες.");
            }
        }
    }
}
