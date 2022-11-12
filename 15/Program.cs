// Находим максимальное число использую функцию

int Max(int num1, int num2, int num3)
{
    int res = 0;
    if (num1 > res) res = num1;
    if (num2 > res) res = num2;
    if (num3 > res) res = num3;
return res;
}
int GetDate()
{
    Console.Write("Введите значение: ");
    return Convert.ToInt32(Console.ReadLine());
}
int max = Max(
    Max(GetDate(), GetDate(), GetDate()),
    Max(GetDate(), GetDate(), GetDate()),
    Max(GetDate(), GetDate(), GetDate())
);
Console.WriteLine(max);