// Вам необходимо сделать несколько блоков кода, которые делают следующее:
// Блок 1. Выводит все элементы массива.
// Блок 2. Выводит все элементы массива в обратном порядке.
// Блок 3. Выводит чётные элементы массива.
// Блок 4. Выводит все элементы массива через 1.
// Блок 5. Выводит все элементы массива пока не встретится элемент -1.

int[] array = new int[] { 6, 8, 89, 12, 11, -4, 7, 123, -1, 0, -99 };

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

void ReversMassiv(int[] arr)
{
    for (int i = 0; i < arr.Length / 2; i++)
    {
        int temporal = array[i];
        array[i] = array[array.Length - 1 - i];
        array[array.Length - 1 - i] = temporal;
    }
}

void EvenElements(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] % 2 == 0 && i < arr.Length)
            Console.Write($"[{arr[i]}]");
    }
}

void ViaOneElements (int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (i % 2 == 0) Console.Write($"[{arr[i]}]");
    }
}

void MinusOneElements(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] == -1)
        break;
        else Console.Write($"[{arr[i]}]");
    }
}

ArrayAllPrint(array);
ReversMassiv(array);
Console.WriteLine();
ArrayAllPrint(array);
Console.WriteLine();
EvenElements(array);
Console.WriteLine();
ViaOneElements(array);
Console.WriteLine();
MinusOneElements(array);