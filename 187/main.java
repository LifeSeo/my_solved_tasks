import java.util.*;

public class Main {
    public static void main(String[] args) {
        MySet set1 = new MySet();
        for (int i = 0; i < 10; i++) {
            set1.add(i + 10);
        }
        set1.add(2);
        set1.add(4);
        set1.add(6);
        System.out.println("Добавление\n" + set1);
        System.out.println("Содержит");
        System.out.println(set1.contains(-1));
        System.out.println(set1.contains(1));
        set1.remove(2);
        System.out.println("Удаление");
        System.out.println(set1);
        System.out.println("Размер");
        System.out.println(set1.size());

        System.out.println("Возвращение ключа по индексу");
        System.out.println(set1.returnKey(0));
//        System.out.println(set1.returnKey(-1));

        System.out.println("Преобразование в список");
        ArrayList<Integer> list1 = set1.toList();
        System.out.println(list1 + " type=" + list1.getClass().getSimpleName());

        System.out.println("Очистка");
        set1.clear();
        System.out.println(set1);

    }
}

class MySet {
    private HashMap<Integer, Object> numbers = new HashMap<>();

    private static final Object OBJECT = new Object();

    public void add(int number) {
        numbers.put(number, OBJECT);
    }

    @Override
    public String toString() {
        return numbers.keySet().toString();
    }

    public boolean contains(int num) {
        return numbers.containsKey(num);
    }

    public void clear() {
        numbers.clear();
    }

    public void remove(int num) {
        numbers.remove(num);
    }

    public int size() {
        return numbers.size();
    }

    public int returnKey(int index) {
        return (int) numbers.keySet().toArray()[index];
//        if (index > numbers.size() - 1 || index < 0) {
//            throw new IndexOutOfBoundsException();
//        }
//        int index1 = 0;
//        int res = 0;
//        for (int i : numbers.keySet()) {
//            if (index1 == index) {
//                res = i;
//                break;
//            }
//            index1++;
//        }
//        return res;
    }

    public ArrayList<Integer> toList() {
        return new ArrayList<>(numbers.keySet());
//        return (ArrayList<Integer>) numbers.keySet().stream().toList();
    }

}
