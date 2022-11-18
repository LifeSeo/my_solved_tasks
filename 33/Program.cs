// Задача 22: Напишите программу, которая
// принимает на вход число (N) и выдаёт таблицу
// квадратов чисел от 1 до N.
// 5 -> 1, 4, 9, 16, 25.
// 2 -> 1,4


Console.WriteLine("Введите число");
int n = Convert.ToInt32(Console.ReadLine());


void Quarter (int num)
{   
    int count = 0;
    while (count <= num)
    {   
        Console.WriteLine($" Число - {count} И его квадрат {count*count}");
        count++;
    }
}
Quarter (n);
