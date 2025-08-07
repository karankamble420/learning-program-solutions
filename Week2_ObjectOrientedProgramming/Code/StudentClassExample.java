public class StudentClassExample {
    String name;
    int age;

    public StudentClassExample(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    public static void main(String[] args) {
        StudentClassExample s1 = new StudentClassExample("Karan", 22);
        s1.display();
    }
}
