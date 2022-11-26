// В одномерном массиве хранится информация о зарплате 15 человек,
// работающих в отделе. Составить программу для определения:
// а) итоговой суммы по всему отделу;
// б) порядкового номера человека, получившего наименьшую зарплату;
// в) средней зарплаты по отделу


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

int MiddleAmount(int[] arr)
{
    int amount = FullAmount(arr);
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

int MinSolarioElement(int[] arr)
{
    int minResultElement = 0;
    int minSolario = MinSolario(arr);
    for (int i = 0; i < arr.Length; i++)
    {
        if (minSolario == arr[i]) minResultElement = i;
    }
    return minResultElement;
}

Console.WriteLine("Выводим все зарплаты сотрудников: ");
int[] arr = NewRandomMassiv(15, 1000, 10000);
ArrayPrint(arr);
int amount = FullAmount(arr);
Console.WriteLine($"Общая сумма всех зарплат -----> {amount}");
int midAmount = MiddleAmount(arr);
Console.WriteLine($"Средняя зарплата -----> {midAmount}");
int minSolario = MinSolario(arr);
Console.WriteLine($"Минимальная зарплата -----> {minSolario}");
int minResultElement = MinSolarioElement(arr);
Console.WriteLine($"Порядковый номер элемента с минимальной зарплатой -----> {minResultElement}");