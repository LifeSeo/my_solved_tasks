// Решение через строку и массив. Напишите программу, которая принимает на вход 
// пятизначное число и проверяет, является ли оно палиндромом.

Console.WriteLine("Введите пятизначное число: ");
int number = Convert.ToInt32(Console.ReadLine());
string strNumber = Convert.ToString(number);

// 12345


bool StrNumber(string num)
{
return strNumber[0] == strNumber[4] && strNumber[1] == strNumber[3];
}

Console.WriteLine(StrNumber(strNumber) ? "Является палиндромом" : "Не является палиндромом");
