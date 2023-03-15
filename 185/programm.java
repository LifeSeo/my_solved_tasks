import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String[]> data = new ArrayList<>();
        int index = 0;
        System.out.println("Введите фамилию, имя, отчество, пол и возраст, или q для остановки ввода: ");
        String[] data2;
        String input = sc.nextLine();
        if (!input.equals("q")) {
            input = index++ + " " + input;
            data2 = input.split(" ");
            data.add(data2);
        }

        while (!input.equals("q")) {
            System.out.println("Введите фамилию, имя, отчество, пол и возраст, или q для остановки ввода: ");
            input = sc.nextLine();
            if (!input.equals("q")) {
                input = index++ + " " + input;
                data2 = input.split(" ");
                data.add(data2);
            }
        }

        int[] orderIndexes = new int[data.size()];

        for (int i = 0; i < orderIndexes.length; i++) {
            orderIndexes[i] = i;
        }

        specialPrintArrayList(data, orderIndexes);

        System.out.println("Вывести сортированный список по возрасту и полу? y - да, n - нет");
        input = sc.nextLine();
        if (input.equals("y")) {
            String[][] array = getSortedArray(data, 4, orderIndexes, true);
            orderIndexes = getIndexesArray(array);
            array = getSortedArray(data, 5, orderIndexes, true);
            orderIndexes = getIndexesArray(array);
            specialPrintArrayList(data, orderIndexes);
        }
    }

    static void specialPrintArrayList(ArrayList<String[]> data, int[] orderIndexes) {
        for (int i : orderIndexes) {
            for (int j = 1; j < data.get(i).length; j++) {
                if (j != 2 && j != 3) {
                    System.out.print(data.get(i)[j] + " ");
                } else System.out.print(data.get(i)[j].charAt(0) + ". ");
            }
            System.out.println();
        }
    }

    static String[][] getSortedArray(ArrayList<String[]> data, int column, int[] orderIndexes, boolean sort) {
        String[][] array = new String[data.size()][2];
        int index = 0;
        for (int i : orderIndexes) {
            array[index][0] = data.get(i)[0];
            array[index][1] = data.get(i)[column];
            index++;
        }
        if (sort) Arrays.sort(array, Comparator.comparing(arr -> arr[1]));
        return array;
    }

    static int[] getIndexesArray(String[][] array) {
        int[] orderIndexes = new int[array.length];
        for (int i = 0; i < orderIndexes.length; i++) {
            orderIndexes[i] = Integer.parseInt(array[i][0]);
        }
        return orderIndexes;
    }

}
