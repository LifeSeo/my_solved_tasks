// Задача 56. Домашняя работа. Задайте прямоугольный двумерный массив.
// Напишите программу, которая будет находить строку с наименьшей суммой элементов.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 5 2 6 7
// Программа считает сумму элементов в каждой строке и
// выдаёт номер строки с наименьшей суммой элементов: 1 строка

int[,] NewRndMatrix(int rows, int columns, int minElement, int maxElement)
{
    int[,] matrix = new int[rows, columns];
    Random rnd = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = rnd.Next(minElement, maxElement + 1);
        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix)

{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        Console.Write("[");
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (j < matrix.GetLength(1) - 1)
                Console.Write($"{matrix[i, j],4}, ");
            else Console.Write($"{matrix[i, j],4}");
        }
        Console.WriteLine("]");
    }
}

int[] SummaElementsRow(int[,] matrix)
{
    int[] summaElements = new int[matrix.GetLength(0)];
    int summa = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            summa += matrix[i, j];
            summaElements[i] = summa;
        }
        summa = 0;
    }
    return summaElements;
}

void PrintArray(int[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        if (i < arr.Length - 1) Console.Write($"{arr[i]}, ");
        else Console.Write($"{arr[i]}");
    }
    Console.WriteLine("]");
}

(int, int) TheSmallestSummaRow(int[] array)
{
    int resultSumma = array[0];
    int resultRow = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] < resultSumma)
        {
            resultSumma = array[i];
            resultRow = i;
        }
    }
    return (resultSumma, resultRow);
}

int[,] matrix = NewRndMatrix(10, 10, 1, 9);
PrintMatrix(matrix);
Console.WriteLine();
int[] summaElementsRow = SummaElementsRow(matrix);
PrintArray(summaElementsRow);
Console.WriteLine();
(int, int) theSmallestSummaRow = TheSmallestSummaRow(summaElementsRow);
Console.WriteLine($"Минимальная сумма, строка ----> {theSmallestSummaRow}");