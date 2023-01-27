// За каждый месяц банк начисляет к сумме вклада 7% от суммы.
// Напишите консольную программу, в которую пользователь вводит сумму вклада
// и количество месяцев.
// А банк вычисляет конечную сумму вклада с учетом начисления процентов за каждый месяц

// Для вычисления суммы с учетом процентов используйте цикл for.
// Для ввода суммы вклада используйте
// выражение Convert.ToDecimal(Console.ReadLine())
// (сумма вклада будет представлять тип decimal)


Console.WriteLine("Введите сумму вклада: ");
decimal summa = Convert.ToDecimal(Console.ReadLine());
Console.WriteLine("Введите количество месяцев вклада: ");
int month = Convert.ToInt32(Console.ReadLine());
int percent = 7;

decimal SummaFinal(decimal sum, int mon)
{
    decimal amount = summa;
    for (int i = 0; i < mon; i++)
    {
        amount = amount + sum * percent / 100;
    }
    return amount;
}
if (summa >= 0)
{
    decimal summaFinal = SummaFinal(summa, month);
    Console.WriteLine($"За {month} месяц(ев) конечная сумма вклада составит {summaFinal}");
}
else Console.WriteLine("Введите верную сумму");
