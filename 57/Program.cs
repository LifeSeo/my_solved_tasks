// В одномерном массиве хранится информация о зарплате 15 человек,
// работающих в отделе. Составить программу для определения:
// а) итоговой суммы по всему отделу;
// б) порядкового номера человека, получившего наименьшую зарплату;
// в) средней зарплаты по отделу

Console.WriteLine("Выводим все зарплаты сотрудников: ");
int[] arr = NewRandomMassiv(15, 1000, 10000);
ArrayPrint(arr);
int amount = FullAmount(arr);
Console.WriteLine($"Общая сумма всех зарплат -----> {amount}");
int midAmount = MiddleAmount(amount);
Console.WriteLine($"Средняя зарплата -----> {midAmount}");
int minSolario = MinSolario(arr);
Console.WriteLine($"Минимальная зарплата -----> {minSolario}");

int[] NewRandomMassiv(int size, int min, int max)
{
    int[] arr = new int[size];
    Random rnd = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rnd.Next(min, max + 1);
    }
    return arr;
}

void ArrayPrint(int[] arr)

{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        if (i < arr.Length - 1)
            Console.Write($"{arr[i]}, ");
        else Console.Write($"{arr[i]}");
    }
    Console.WriteLine("]");
}

int FullAmount(int[] arr)
{
    int resultAmount = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        resultAmount += arr[i];
    }
    return resultAmount;
}

int MiddleAmount(int middleAmount)
{
    int midAmount = amount / arr.Length + 1;
    return midAmount;
}

int MinSolario(int[] arr)
{
    int minSolario = arr[0];
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] < minSolario) minSolario = arr[i];
    }
    return minSolario;
}

int MinSolarioElement(int minElement)
{
    int minResultElement = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (minSolario == arr[i]) minResultElement = i;
    }
    return minResultElement;
}

int minResultElement = MinSolarioElement(minSolario);

Console.WriteLine($"Порядковый номер елемента с минимальной зарплатой -----> {minResultElement}");