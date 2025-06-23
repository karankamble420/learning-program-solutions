interface Animal {
    void speak();
}

class Dog implements Animal {
    public void speak() {
        System.out.println("Dog says: Woof!");
    }
}

class Cat implements Animal {
    public void speak() {
        System.out.println("Cat says: Meow!");
    }
}

class AnimalFactory {
    public static Animal getAnimal(String type) {
        if ("dog".equalsIgnoreCase(type)) return new Dog();
        else if ("cat".equalsIgnoreCase(type)) return new Cat();
        else return null;
    }
}

public class FactoryPatternExample {
    public static void main(String[] args) {
        Animal animal1 = AnimalFactory.getAnimal("dog");
        Animal animal2 = AnimalFactory.getAnimal("cat");

        if (animal1 != null) animal1.speak();
        if (animal2 != null) animal2.speak();
    }
}
