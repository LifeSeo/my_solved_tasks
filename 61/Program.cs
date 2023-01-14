// Задача 41: (ВАРИАНТ 1) Пользователь вводит с клавиатуры M чисел.
// Посчитайте, сколько чисел больше 0 ввёл пользователь
// 0, 7, 8, -2, -2 -> 2
// -1, -7, 567, 89, 223-> 3


Console.Write("Введите элементы(через пробел): ");
int[] arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

int Elements(int[] arr)
{
int numbers = 0;
 
for (int i = 0; i < arr.Length; i++)
{
    if (arr[i] > 0) numbers++;
}
return numbers;
}

int numbers = Elements(arr);
Console.WriteLine($"Количество элементов больше нуля ----> {numbers}");
