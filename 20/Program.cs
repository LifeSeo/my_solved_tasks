// Создайте функцию и выведите на экран консоли сегодняшнею дату.

class Programm
{
    static void Main(string[] args)
    {
        Programm x = new Programm();
        x.Date();
    }

void Date()
{
    DateTime todayDate = DateTime.Now;
    Console.WriteLine(todayDate.ToString("dd/MM/yyyy"));
}
}
