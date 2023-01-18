// Создать треугольник Паскаля, значение строк задает пользователь

Console.WriteLine("Введите количество строк треугольника Паскаля: ");
double strings = Convert.ToInt32(Console.ReadLine());

double Factorial(double strings)
{
    double result = 1;
    for (int i = 1; i < strings; i++)
    {
        result *= i;
    }
    return result;
}

void PrintTriangle()
{
    for (int i = 0; i < strings; i++)
    {
        for (int j = 0; j <= (strings - i); j++)
        {
            Console.Write(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            Console.Write("   ");
            Console.Write(Factorial(i) / (Factorial(j) * Factorial(i - j)));
        }
        Console.WriteLine();
        Console.WriteLine();
    }
}

PrintTriangle();

