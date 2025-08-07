interface Drawable {
    void draw();
}

class Circle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing a Circle");
    }
}

class Rectangle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing a Rectangle");
    }
}

public class InterfaceAbstractionExample {
    public static void main(String[] args) {
        Drawable d1 = new Circle();
        Drawable d2 = new Rectangle();

        d1.draw();
        d2.draw();
    }
}
