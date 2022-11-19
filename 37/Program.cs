// Пользователь вводит натуральное число. Определить:
// а) является ли оно четным;
// б) оканчивается ли оно цифрой 7


Console.WriteLine("Введите натуральное число --> ");
int number = Convert.ToInt32(Console.ReadLine());

// if (number % 2 == 0) 
// {
// Console.WriteLine($"Число {number} четное");
// }
// else
// {
// Console.WriteLine($"Число {number} нечетное");
// }

// if (number % 10 == 7)
// {
// Console.WriteLine($"Число {number} оканчивается на 7");
// }
// else
// {
// Console.WriteLine($"Число {number} не оканчивается на 7");
// }

string CheckNumber(int num)
{
    if (num / 10 == 0) return "Не верно введенные данные";
    if (num == 0) return "0 --> не является натуральным числом";
    if (num % 10 == 7) return "Число не четное и оканчивается на 7";
    if (num % 2 == 0) return "Число четное и не оканчивается на 7";
    if (num % 2 == 1) return "Число не четное и не оканчивается на 7";
    return "Неверно введенные данные";
}

string result = CheckNumber(number);
Console.WriteLine(result);




