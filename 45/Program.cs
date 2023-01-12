// Домашняя работа. Задача 25. Напишите цикл, который принимает на вход два числа (A и B) и
// возводит число A в натуральную степень B.
// 3, 5 -> 243 (3⁵)
// 2, 4 -> 16

Console.WriteLine("Введите число А: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число B: ");
int b = Convert.ToInt32(Console.ReadLine());

int Exponentiation(int num1, int num2)
{
    int result = 1;
    for (int i = 1; i <= num2; i++)
    {
        result = num1 * result;
    }
    return result;
}
if (b > 0)
{
int exponentiation = Exponentiation(a, b);
Console.WriteLine($"Число {a} в степени {b} ----> {exponentiation}");
}
else Console.WriteLine("Введите вещественное число");
