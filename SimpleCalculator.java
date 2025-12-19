public class SimpleCalculator {

    // Add two integers
    public static int add(int a, int b) {
        return a + b;
    }

    // Multiply two integers
    public static int multiply(int a, int b) {
        return a * b;
    }

    // Entry point
    public static void main(String[] args) {
        int x = 5;
        int y = 7;

        int sum = add(x, y);
        int product = multiply(x, y);

        System.out.println("x = " + x + ", y = " + y);
        System.out.println("Sum = " + sum);
        System.out.println("Product = " + product);
    }
}
