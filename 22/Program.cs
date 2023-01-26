int number = new Random().Next(10, 100); 
Console.WriteLine($"Случайное число из отрезка 10 - 99 --> {number}");

int MaxDigit(int num) // int num = number
{
    int firstDigit = num / 10; // 7
    int secondDigit = num % 10; // 8
    if (firstDigit > secondDigit) return firstDigit;
    return secondDigit;
}

int maxDigit = MaxDigit(number);
Console.WriteLine($"Наибольшая цифра числа --> {maxDigit}");
