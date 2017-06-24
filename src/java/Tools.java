import java.util.concurrent.ThreadLocalRandom;

public class Tools {
    public static int[] rand_int(int size, int min, int max) {
        if ( size < 1 ) {
            throw new IllegalArgumentException("Size can't be nonpositive");
        }

        // Shift max by one because the random int generator isn't inclusive
        ++max;

        int[] arr = new int[size];
        for ( int i = 0; i < size; ++i ) {
            arr[i] = ThreadLocalRandom.current().nextInt(min, max);
        }

        return arr;
    }

    public static double[] rand_real(int size, double min, double max) {
        if ( size < 1 ) {
            throw new IllegalArgumentException("Size can't be nonpositive");
        }

        double[] arr = new double[size];
        for ( int i = 0; i < size; ++i ) {
            arr[i] = ThreadLocalRandom.current().nextDouble(min, max);
        }

        return arr;
    }

    public static boolean is_sorted(int[] arr) {
        for ( int i = 1; i < arr.length; ++i )
            if ( arr[i-1] > arr[i] )
                return false;

        return true;
    }

    public static boolean is_sorted(double[] arr) {
        for ( int i = 1; i < arr.length; ++i )
            if ( arr[i-1] > arr[i] )
                return false;

        return true;
    }

    public static void print(int[] arr) {
        System.out.print("{" + arr[0]);
        for ( int i = 1; i < arr.length; ++i ) {
            System.out.print(", " + arr[i]);
        }
        System.out.println("}");
    }

    public static void print(double[] arr) {
        System.out.print("{" + arr[0]);
        for ( int i = 1; i < arr.length; ++i ) {
            System.out.print(", " + arr[i]);
        }
        System.out.println("}");
    }
    
    public static void main(String[] args) {
        int[] arr = rand_int(10, 0, 10);
        System.out.println("The Array:");
        print(arr);
        System.out.println("Is the array sorted?" + is_sorted(arr));
    }
}
