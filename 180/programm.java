import java.util.Random;

public class Main {
    public static void main(String[] args) {
//        1. Выбросить случайное целое число в диапазоне от 0 до 2000 и сохранить в i
        int i = randomInt(0, 2001);
        System.out.println(i);
//        2. Посчитать и сохранить в n номер старшего значащего бита выпавшего числа
        System.out.println(Integer.toBinaryString(i));
        int n = numberHighOrderBit(i);
        System.out.println(n);
//        3. Найти все кратные n числа в диапазоне от i до Short.MAX_VALUE сохранить в массив m1
        int[] m1 = getMultiples(n, i, Short.MAX_VALUE);
//        printArray(m1, 24);
//        4. Найти все некратные n числа в диапазоне от Short.MIN_VALUE до i и сохранить в массив m2
        int[] m2 = getNonMultiples(n, Short.MIN_VALUE, i);
//        printArray(m2, 24);
    }

    //    1. Выбросить случайное целое число в диапазоне от 0 до 2000 и сохранить в i
    static int randomInt(int min, int max) {
        Random random = new Random();
        return random.nextInt(min, max);
    }

    //    2. Посчитать и сохранить в n номер старшего значащего бита выпавшего числа
    static int numberHighOrderBit(int number) {
        return Integer.toBinaryString(number).length();
    }

    //    3. Найти все кратные n числа в диапазоне от i до Short.MAX_VALUE сохранить в массив m1
    static int[] getMultiples(int divider, int min, int max) {
        int size = 0;
        for (int i = min; i < max; i++) {
            if (i % divider == 0) size++;
        }
        int[] multiples = new int[size];
        int index = 0;
        for (int i = min; i < max; i++) {
            if (i % divider == 0) multiples[index++] = i;
        }
        return multiples;
    }

    static void printArray(int[] array, int columns) {
        for (int i = 0; i < array.length; i++) {
            if (i != 0 && i % columns == 0) System.out.println();
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    //    4. Найти все некратные n числа в диапазоне от Short.MIN_VALUE до i и сохранить в массив m2
    static int[] getNonMultiples(int divider, int min, int max) {
        int size = 0;
        for (int i = min; i < max; i++) {
            if (i % divider != 0) size++;
        }
        int[] nonMultiples = new int[size];
        int index = 0;
        for (int i = min; i < max; i++) {
            if (i % divider != 0) nonMultiples[index++] = i;
        }
        return nonMultiples;
    }


}
