// Домашняя работа. Задача 36. Задайте одномерный массив, заполненный случайными числами.
// Найдите сумму элементов, стоящих на нечётных позициях.

// [3, 7, 23, 12] -> 19
// [-4, -6, 89, 6] -> 0

int[] NewArrowRandom(int size, int min, int max)
{
    int[] arr = new int[size];
    Random rnd = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rnd.Next(min, max + 1);
    }
    return arr;
}

void ArrowPrint(int[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        if(i < arr.Length -1)
        Console.Write($"{arr[i]}, ");
        else Console.Write($"{arr[i]}");
    }
    Console.Write("]");
}
Console.Write("Выводим массив на печать ----> ");
int[] array = NewArrowRandom(10, 10, 999);
ArrowPrint(array);

int OddNumber(int[] arr)
{
    int result = 0;
    for (int i = 0; i < arr.Length; i++)
    {
    if (arr[i] % 2 == 1)
    result += arr[i];
    }
    return result;
}

int oddNumber = OddNumber(array);
Console.WriteLine($" Сумма нечетных элементов массива равна ----> {oddNumber}");