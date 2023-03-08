public class Main {
    public static void main(String[] args) {
//        1. Напишите программу, чтобы найти вхождение в строке (содержащей все символы другой строки).
        String str1 = "Hello World!";
        String str2 = "World";
        System.out.println(str1.contains(str2));
//        2. Напишите программу, чтобы проверить, являются ли две данные строки вращением друг друга (вхождение в обратном порядке).
        String str3 = "!dlroW olleH";
        System.out.println(str1.equals(new StringBuilder(str3).reverse().toString()));
//        3. *Напишите программу, чтобы перевернуть строку с помощью рекурсии.
        System.out.println(recursionReverse(str1, str1.length() - 1));
//        4. Дано два числа, например 3 и 56, необходимо составить следующие строки: 3 + 56 = 59 3 – 56 = -53 3 * 56 = 168 Используем метод StringBuilder.append().
        int numb1 = 3;
        int numb2 = 56;
        StringBuilder str4 = new StringBuilder().append(numb1).append(" + ").append(numb2).append(" = ").append(numb1 + numb2);
        StringBuilder str5 = new StringBuilder().append(numb1).append(" - ").append(numb2).append(" = ").append(numb1 - numb2);
        StringBuilder str6 = new StringBuilder().append(numb1).append(" * ").append(numb2).append(" = ").append(numb1 * numb2);
        System.out.println(str4 + "\n" + str5 + "\n" + str6);
//        5. Замените символ “=” на слово “равно”. Используйте методы StringBuilder.insert(),StringBuilder.deleteCharAt().
//        str4.insert(str4.indexOf("="),"равно").deleteCharAt(str4.indexOf("="));
//        str5.insert(str5.indexOf("="),"равно").deleteCharAt(str5.indexOf("="));
//        str6.insert(str6.indexOf("="),"равно").deleteCharAt(str6.indexOf("="));
//        System.out.println(str4 + "\n" + str5 + "\n" + str6);
//        6. Замените символ “=” на слово “равно”. Используйте методы StringBuilder.replace().\
        str4.replace(str4.indexOf("="), str4.indexOf("=") + 1, "равно");
        str5.replace(str5.indexOf("="), str5.indexOf("=") + 1, "равно");
        str6.replace(str6.indexOf("="), str6.indexOf("=") + 1, "равно");
        System.out.println(str4 + "\n" + str5 + "\n" + str6);
//        7. *Сравнить время выполнения пункта 6 со строкой содержащей 10000 символов "=" средствами String и StringBuilder.
        String str7 = "=".repeat(10000);
        StringBuilder str8 = new StringBuilder("=".repeat(10000));
        long begin = System.currentTimeMillis();
        str7 = str7.replace("=", "равно");
        long end = System.currentTimeMillis();
        System.out.println("String: " + (end - begin));
        begin = System.currentTimeMillis();
        while (str8.indexOf("=") != -1)
            str8.replace(str8.indexOf("="), str8.indexOf("=") + 1, "равно");
        end = System.currentTimeMillis();
        System.out.println("StringBuilder: " + (end - begin));
    }

    static String recursionReverse(String str, int index) {
        if (index >= 0) {
            return str.charAt(index) + recursionReverse(str, index - 1);
        }
        return "";
    }
}