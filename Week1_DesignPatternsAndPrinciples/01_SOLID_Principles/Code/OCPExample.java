abstract class Shape {
    public abstract double area();
}

class Rectangle extends Shape {
    double length, width;

    public Rectangle(double l, double w) {
        this.length = l;
        this.width = w;
    }

    @Override
    public double area() {
        return length * width;
    }
}

class Circle extends Shape {
    double radius;

    public Circle(double r) {
        this.radius = r;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

public class OCPExample {
    public static void main(String[] args) {
        Shape s1 = new Rectangle(5, 3);
        Shape s2 = new Circle(4);

        System.out.println("Rectangle Area: " + s1.area());
        System.out.println("Circle Area: " + s2.area());
    }
}
