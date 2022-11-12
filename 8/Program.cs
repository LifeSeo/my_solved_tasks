// Необходимо ввести имя с клавиатуры и попроветствовать пользователя. Для пользователя "Маша", необходимо специальное приветствие.

Console.WriteLine("Введите имя пользователя: ");
string username = Console.ReadLine();

if(username.ToLower() == "маша")
{
Console.WriteLine("Вав, Маша, наконец ты пришла");
}
else
{
Console.WriteLine($"Привет, {username}");    
}


