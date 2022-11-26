// В массиве хранятся цены на 10 видов мороженого. С помощью датчика
// случайных чисел заполнить массив целыми значениями, лежащими в диапазоне
// от 3 до 20 включительно. Определить порядковый номер самого дорогого
// мороженого.

int[] NewRandomMassiv(int size, int min, int max)
{
    int[] arr = new int[size];
    Random rnd = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rnd.Next(min, max + 1);
    }
    return arr;
}

void ArrayPrint(int[] arr)
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

int MaxPrice(int[] arr)
{
    int maxPrice = arr[0];
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] > maxPrice) maxPrice = arr[i];
    }
    return maxPrice;
}

int PriceElementNumber(int[] arr, int maxPriceElement)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] == maxPriceElement) maxPriceElement = i;
    }
    return maxPriceElement;
}

Console.Write("Выводим массив на печать ----> ");
int[] array = NewRandomMassiv(10, 3, 20);
ArrayPrint(array);
int maxPrice = MaxPrice(array);
Console.WriteLine($" Номер максимального числа ----> {maxPrice}");
int maxPriceElement = PriceElementNumber(array, maxPrice);
Console.Write($"Номер максимального элемента ----> {maxPriceElement}");