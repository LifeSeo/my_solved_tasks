// Задайте массив и отсортируйте его от меньшего к большему

int[] array = new int[] {23,90,-4,12,-99,78,3,34};
        Array.Sort(array);
        Console.WriteLine("Выводим значения: ");
        Array.ForEach(array, Console.WriteLine);