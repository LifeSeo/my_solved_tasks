import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, ArrayList<String[]>> data = new HashMap<>();
        int index = 0;
        String[] names, numbers, popularity;
        ArrayList<String[]> data2;
        String input = "start input";
        while (!input.equals("q")) {
            System.out.println("Введите имя и фамилию, или q для остановки ввода: ");
            data2 = new ArrayList<>();
            input = sc.nextLine();
            if (!input.equals("q")) {
                names = input.split(" ");
                System.out.println("Введите номера телефонов через пробел");
                input = sc.nextLine();
                numbers = input.split(" ");
                popularity = new String[]{Integer.toString(new Random().nextInt(10))};
                data2.add(names);
                data2.add(numbers);
                data2.add(popularity);

                data.put(index++, data2);
            }
        }

        int[] orderIndexes = getDefaultOrderIndexes(data);

        hashMapSpecialPrint(orderIndexes, data);

        HashMap<String, Integer> namesRepeatCount = getRepeatedElements(data);
        System.out.println("Повторяющиеся имена:");

        String[] keysOrder = getSortedNamesCount(namesRepeatCount, true);

        namesCountPrint(namesRepeatCount, keysOrder);

        orderIndexes = getSortedArrayIndexesByNamesRepeatCount(namesRepeatCount, data, orderIndexes, true);
        System.out.println("Сортировка по популярности имён: ");
        hashMapSpecialPrint(orderIndexes, data);

        orderIndexes = getDefaultOrderIndexes(data);

        orderIndexes = getSortedArrayIndexes(data, 2, orderIndexes, true);
        System.out.println("Сортировка по популярности номеров:");
        hashMapSpecialPrint(orderIndexes, data);

    }

    static int[] getDefaultOrderIndexes(HashMap<Integer, ArrayList<String[]>> data) {
        int[] orderIndexes = new int[data.size()];

        for (int i = 0; i < orderIndexes.length; i++) {
            orderIndexes[i] = i;
        }

        return orderIndexes;
    }

    static void hashMapSpecialPrint(int[] orderIndexes, HashMap<Integer, ArrayList<String[]>> data) {
        for (int k : orderIndexes) {
            for (String[] array : data.get(k)) {
                for (String element : array) {
                    System.out.print(element + " ");
                }
            }
            System.out.println();
        }
    }

    static int[] getSortedArrayIndexes(HashMap<Integer, ArrayList<String[]>> data, int column, int[] orderIndexes, boolean desc) {
        String[][] array = new String[data.size()][2];
        int index = 0;
        for (int i : orderIndexes) {
            array[index][0] = Integer.toString(i);
            array[index][1] = data.get(i).get(column)[0];
            index++;
        }
        if (desc)
            return bubbleIndexesDescSort(array);
        Arrays.sort(array, Comparator.comparing(arr -> arr[1]));
        return getIndexesArray(array);
    }

    static HashMap<String, Integer> getRepeatedElements(HashMap<Integer, ArrayList<String[]>> data) {
        Set<Integer> keys = data.keySet();
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (int i : keys) {
            if (!hashMap.containsKey(data.get(i).get(0)[0])) {
                hashMap.put(data.get(i).get(0)[0], 1);
            } else hashMap.compute(data.get(i).get(0)[0], (k, v) -> (v += 1));
        }
        return hashMap;
    }

    static void namesCountPrint(HashMap<String, Integer> hashMap, String[] keysOrder) {
        for (String i : keysOrder) {
            System.out.println(i + ":" + hashMap.get(i));
        }
    }

    static int[] bubbleIndexesDescSort(String[][] array) {
        int[] indexes = getIndexesArray(array);
        for (int count = 0; count < indexes.length; count++) {
            boolean sorted = true;
            for (int i = 0; i < indexes.length - 1; i++) {
                if (indexes[i] + 1 < indexes.length)
                    if (Integer.parseInt(array[indexes[i + 1]][1]) > Integer.parseInt(array[indexes[i]][1])) {
                        int t = indexes[i + 1];
                        indexes[i + 1] = indexes[i];
                        indexes[i] = t;
                        sorted = false;
                    }
            }
            if (sorted) break;
        }
        return indexes;
    }

    static int[] getIndexesArray(String[][] array) {
        int[] orderIndexes = new int[array.length];
        for (int i = 0; i < orderIndexes.length; i++) {
            orderIndexes[i] = Integer.parseInt(array[i][0]);
        }
        return orderIndexes;
    }

    static String[] getSortedNamesCount(HashMap<String, Integer> data, boolean desc) {
        String[][] array = new String[data.size()][3];
        int index = 0;
        Set<String> keys = data.keySet();
        for (String i : keys) {
            array[index][0] = String.valueOf(index);
            array[index][1] = String.valueOf(data.get(i));
            array[index][2] = i;
            index++;
        }
        if (desc) {
            String[] keysOrder = new String[array.length];
            int[] indexesOrder = bubbleIndexesDescSort(array);
            index = 0;
            for (int i : indexesOrder) {
                keysOrder[index++] = array[i][2];
            }
            return keysOrder;
        }
        Arrays.sort(array, Comparator.comparing(arr -> arr[1]));
        return getKeysOrder(array);
    }

    static String[] getKeysOrder(String[][] array) {
        String[] keysOrder = new String[array.length];
        for (int i = 0; i < keysOrder.length; i++) {
            keysOrder[i] = array[i][2];
        }
        return keysOrder;
    }

    static int[] getSortedArrayIndexesByNamesRepeatCount(HashMap<String, Integer> namesRepeatCount, HashMap<Integer, ArrayList<String[]>> data, int[] orderIndexes, boolean desc) {
        String[][] array = new String[data.size()][3];
        int index = 0;
        for (int i : orderIndexes) {
            array[index][0] = Integer.toString(i);
            array[index][1] = String.valueOf(namesRepeatCount.get(data.get(i).get(0)[0]));
            array[index][2] = data.get(i).get(0)[0];
            index++;
        }
        if (desc)
            return bubbleIndexesDescSort(array);
        Arrays.sort(array, Comparator.comparing(arr -> arr[1]));
        return getIndexesArray(array);
    }

}
