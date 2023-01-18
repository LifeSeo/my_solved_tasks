// Задача 67: Напишите программу, которая будет принимать на вход число и
// возвращать сумму его цифр
// 453 -> 12
// 45 -> 9

Console.WriteLine("Введите целое число: ");
int number = Convert.ToInt32(Console.ReadLine());
Console.WriteLine();
int sumNum = SumNumb(number);
Console.Write(sumNum);
int SumNumb(int num)
{
    int sum = 0;
    if (num % 10 == 0) return sum;
    sum = sum + num % 10 + SumNumb(num/10);
    return sum;
}
