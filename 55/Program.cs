// Домашняя работа. Задача 38. Задайте массив вещественных чисел.
// Найдите разницу между максимальным и минимальным числами массива

// [3.5, 7.1, 22.9, 2.3, 78.5] -> 76.2

double[] NewRandowDouble(int size, int min, int max)
{
    double[] arr = new double[size];
    Random rnd = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = Math.Round(rnd.NextDouble() * (max - min) + min, 2);
    }
    return arr;
}

void PrintArray(double[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        if (i < arr.Length - 1)
            Console.Write($"{arr[i]}. ");
        else Console.Write($"{arr[i]}");
    }
    Console.WriteLine("]");
}
Console.Write("Выводим массив на печать: ");
double[] array = NewRandowDouble(5, 100, 999);
PrintArray(array);

double MaxDifference(double[] arr)
{
double maxNumber =arr[0];
for (int i = 0; i < arr.Length; i++)
{
    if (arr[i] > maxNumber) maxNumber = arr[i];
}
return maxNumber;
}
double MinDifference(double[] arr)
{
double minNumber = arr[0];
for (int i = 0; i < arr.Length; i++)
{
    if (arr[i] < minNumber) minNumber = arr[i];
}
return minNumber;
}

double differenceMax = MaxDifference(array);
double differenceMin = MinDifference(array);
double result = differenceMax - differenceMin;
Console.Write(@$"Разницу между максимальным и минимальным элементами массива --->
{Math.Round(result, 2)}");
