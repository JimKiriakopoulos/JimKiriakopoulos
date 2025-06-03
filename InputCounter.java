class InputCounter {
    public static void main(String[] args) {
        // Τυπώνουμε το πλήθος των δεδομένων εισόδου
        System.out.println("Πλήθος δεδομένων εισόδου: " + args.length);
        for (String arg : args) {
            System.out.print(arg + " ");
        }
        System.out.println(); // Επιστρέφει στην επόμενη γραμμή μετά την εκτύπωση
    }
}