// Написать программу, которая из имеющегося массива строк формирует массив из строк,
// длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры,
// либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями,
// лучше обойтись исключительно массивами.

// Задаем массив строки.

string[] arr =  {"Hello","am",
                     "is",
                     "mah!",
                     "Kitteh","I'm 1337",
                     "Your the machine, I'm the human.",
                     "Fire your own laser.",
                     "Shut up noob.",
                     "Luk, I am your father.",
                     "Kitteh","Orly?",
                     "I was made in C#.",
                     "Randomness!",
                     "Are you sure?",
                     "Yeah, me too.",
                     "What are you talking about?",
                     "Kids these days","I know right?",
                     "Icecream is good.",
                     "#include i<ostream>",
                     "Man, I'm bored.",
                     "Just shut up will ya?",
                     "Are you sure?","Yeah!",
                     "As",
                     "You made me angry",
                     "Uh",
                     "What is wrong with you?",
                     "Oog","733","Blobbeh",
                     "Turtlegiant",
                     "If","And","Or",
                     "day",
                     "I'm truly random.",
                     "Are you?",
                     "I'm a pretty smart AI.",
                     "Yarly.","Kitteh Behind Yeh!.",
                     "Man I'm bored","Your not making any sense",
                     "Never!!!","lol",
                     "Rofl","I'm hungry","My food!"};

// Создаем метод вывода в консоль заданого массива
void PrintArray(string[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        if (i < arr.Length - 1) Console.Write($"{arr[i]}, ");
        else Console.Write($"{arr[i]}");
    }
    Console.WriteLine("]");
}
// Создаем метод вывода в консольнового массива
void PrintArraySorting(string[] sortingArray)
{
    for (int i = 0; i < sortingArray.Length; i++)
    {
        Console.Write(sortingArray[i] + " ");
    }
}
// Создаем метод отсеивания из массива элементов, которые больше 3-х знаков
string[] SortingArray(string[] array)
{
    string[] sortingArray = new string[array.Length];
    int temp = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= 3)
        {
            sortingArray[temp] = array[i];
            temp++;
        }
    }
    return sortingArray;
}

Console.WriteLine("Выводим первоначальный рандомный массив: ");
PrintArray(arr);
Console.WriteLine("Выводим отсортированный массив с длинной не более 3 символов в элементе: ");
string[] sortingArray = SortingArray(arr);
PrintArraySorting(sortingArray);