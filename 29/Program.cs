// Напишите программу, используя метод. Если товары стоят больше или равно 1000 рублей, 
// то мы их не покупаем. Стоимость товара задается рандомно.

int price = new Random().Next(12, 5750);
Console.WriteLine($"Стоимость товара --> {price}");

// if (price <= 1000)
// {
//     Console.WriteLine("Покупаем");
// }
// else
// {
//     Console.WriteLine("Не покупаем");
// }

bool MaxPrice(int price)
{
    return price < 1000 || price == 1000;
}

Console.WriteLine(MaxPrice(price) ? "Покупаем товар" : "Не покупаем товар");

