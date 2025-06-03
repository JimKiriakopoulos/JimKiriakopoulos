class Animal {
    private String name;
    private int age;
    private String species;

    /**
     * @param name
     * @param age
     * @param species
     */
    public Animal(String name, int age, String species) {
        this.name = name;
        this.age = age;
        this.species = species;
    }

    public void displayInfo() {
        System.out.println("Animal Name: " + name);
        System.out.println("Age: " + age + " years");
        System.out.println("Species: " + species);
    }

    public static void main(String[] args) {
        Animal myAnimal = new Animal("Leo", 5, "Lion");
        myAnimal.displayInfo();
    }
}