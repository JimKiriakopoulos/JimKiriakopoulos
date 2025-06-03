class pinakes {
    public static void main(String[] args) {
        int[] thrirties = new int[38563847];
        
        // Γεμίζουμε τον πίνακα με τιμές
        for (int i = 0; i < thrirties.length; i++) {
            thrirties[i] = 30;
        }
        
        // Εκτυπώνουμε το τελευταίο στοιχείο του πίνακα
        System.out.println(thrirties[thrirties.length - 1]);
    }
}