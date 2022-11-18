﻿// Домашняя работа (Задача 13 - РАЦИОНАЛЬНОЕ РЕШЕНИЕ): Напишите программу,
// которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
// Выполнить с помощью числовых операций (целочисленное деление, остаток от деления).

// 645 -> 5
// 78 -> третьей цифры нет
// 32679 -> 6

Console.Write("Введите целое число: ");
int number = Convert.ToInt32(Console.ReadLine());

string digit = Convert.ToString(number);

if (digit.Length > 2)
{
    Console.WriteLine($"Третья цифра: " + digit[2]);
}
else
{
    Console.WriteLine("Третьей цифры нет");
}