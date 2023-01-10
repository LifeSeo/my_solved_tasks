// Домашняя работа (Задача 13): Напишите программу, которая выводит третью цифру 
// заданного числа или сообщает, что третьей цифры нет.
// Выполнить с помощью числовых операций (целочисленное деление, остаток от деления).

// 645 -> 5
// 78 -> третьей цифры нет
// 32679 -> 6

Console.Write("Введите целое число: ");
int number = Convert.ToInt32(Console.ReadLine());

int DigitFind(int number)
{
    int result = -1;
    if (number >= 100)
    {
        while (number > 999)
        {
            number = number / 10;
        }
        result = number % 10;
    }
    return result;
}

if (DigitFind(number) == -1)
{
Console.WriteLine("Третьей цифры не существут");
}
else
{
Console.WriteLine($"Третья цифра: {DigitFind(number)}");
}
