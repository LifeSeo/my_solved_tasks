// Дано натуральное число N(N > 9). Определить сумму цифр
// в первой половине числа (старшие разряды).

Console.WriteLine("Введите натуральное число больше девяти: ");
int n = Convert.ToInt32(Console.ReadLine());

int DigitsAmount(int n)
{
    int digits = 0;
    while (n > 0)
    {
        n = n / 10;
        digits++;
    }
    return digits;
}

int[] ArrayOfDigits(int n)
{
    int digit = DigitsAmount(n);
    int[] array = new int[digit];
    for (int i = 0; i < array.Length; i++)
    {
        int temp = n % 10;
        array[i] = temp;
        n = n / 10;
    }
    return array;
}

void ArrayAllPrint(int[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        if (i < arr.Length - 1)
            Console.Write($"{arr[i]}, ");
        else Console.Write($"{arr[i]}");
    }
    Console.Write("]");
}

int SummaDigits(int[] array)
{
    int sum = 0;
    for (int i = 0; i < array.Length / 2; i++)
    {
        sum += array[i];
    }
    return sum;
}

int digitsamount = DigitsAmount(n);
Console.WriteLine($"Количество цифер в числе ---> {digitsamount}");
int[] arr = ArrayOfDigits(n);
Console.Write("Преобразовываем в массив: ");
Array.Reverse(arr);
ArrayAllPrint(arr);
Console.WriteLine();
int result = SummaDigits(arr);
Console.WriteLine($"Сумма цифр в первой половине числа ----> {result}");


