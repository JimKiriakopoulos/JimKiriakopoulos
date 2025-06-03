class Robot {
    static double[] currentPos = new double[2];
    static double totalDist = 0.0;
    static int stops = 1;

    // Μέθοδος για μετακίνηση του ρομπότ σε μια νέα θέση
    static void moveTo(double[] newPos) {
        // Υπολογισμός της απόστασης από την προηγούμενη θέση στη νέα
        double dist = distance(currentPos, newPos);
        
        // Προσθήκη της απόστασης στο συνολικό άθροισμα της απόστασης
        totalDist += dist;
        
        // Ενημέρωση της θέσης του ρομπότ
        currentPos = newPos;
        
        // Αύξηση των στάσεων
        stops++;
    }

    // Μέθοδος για εκτύπωση της τρέχουσας κατάστασης
    static void printState() {
        System.out.printf("Current position: (%.1f, %.1f)\n", currentPos[0], currentPos[1]);
        System.out.println("Stops: " + stops);
        System.out.printf("Total distance traveled: %.1f\n", totalDist);
    }

    // Μέθοδος για υπολογισμό της απόστασης μεταξύ δύο σημείων
    static double distance(double[] p1, double[] p2) {
        // Υπολογισμός της Ευκλείδειας απόστασης
        return Math.sqrt(Math.pow(p2[0] - p1[0], 2) + Math.pow(p2[1] - p1[1], 2));
    }

    public static void main(String[] args) {
        // Εκτύπωση της αρχικής κατάστασης
        printState();
        
        // Μετακίνηση στο σημείο (5, 6)
        double[] A = {5, 6};
        moveTo(A);
        
        // Εκτύπωση της κατάστασης μετά την κίνηση
        printState();
        
        // Μετακίνηση στο σημείο (0, 0)
        moveTo(new double[] {0, 0});
        
        // Εκτύπωση της κατάστασης μετά τη δεύτερη κίνηση
        printState();
    }
}
