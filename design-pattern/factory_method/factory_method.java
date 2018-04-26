// interface
public interface Shape {
    void draw();
}

// 3 class implement Shape interface
public class Circle extends Shape {
    @override
    void draw() {
        System.out.print("Circle class");
    }
}

public class Square extends Shape {
    @override
    void draw() {
        System.out.print("Square class");
    }
}

public class Rectangle extends Shape {
    @override
    void draw() {
        System.out.print("Rectangle class");
    }
}

public enum Shapes {
    CIRCLE,
    SQUARE,
    RECTANGLE
}

// Factory method "sinh ra" class cụ thể dựa trên biến truyền vào
public class ShapeFactory {
    public Shape getShape(String Shape) {
        // TODO: check correctness operation upperCase
        swich (String.upperCase(shape)): {
            case Shapes.CIRCLE:
                return new Circle();
            case Shapes.SQUARE:
                return new Square();
            case Shapes.RECTANGLE:
                return new Rectangle();
            default:
                return null;
        }

    }
}

// Demo
public class Demo {
    public class void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();

        Shape shape = shapeFactory.getShape('circle');
        circle.draw();

        shape = shapeFactory.getShape('square');
        shape.draw();

        shape = shapeFactory.getShape('rectangle');
        shape.draw();
    }
}
