// Задача 57: Составить частотный словарь элементов
// двумерного массива. Частотный словарь содержит
// информацию о том, сколько раз встречается элемент
// входных данных.

int[,] CreateMatrixRndInt(int rows, int columns, int min, int max)
{
    int[,] matrix = new int[rows, columns];
    Random rnd = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = rnd.Next(min, max + 1);
            // TODO: вывести индексы массива.
            // matrix[i, j] = i * 10 + j;
        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix, string beginRow, string separatorElems, string endRow)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        Console.Write(beginRow);
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (j < matrix.GetLength(1) - 1)
                Console.Write($"{matrix[i, j],4}{separatorElems}");
            else Console.Write($"{matrix[i, j],4}");
        }
        Console.WriteLine(endRow);
    }
}

void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"{array[i]} ");
    }
}

int[] MatrixToArray(int[,] matrix)
{
    int rows = matrix.GetLength(0);
    int columns = matrix.GetLength(0);
    int[] array = new int[matrix.Length];
    int index = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            array[index] = matrix[i, j];
            index++;
        }
    }
    return array;
}

int SizeRequencyElemsArray(int[] array)
{
    int size = 0;
    int temp = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] != temp)
        {
            size++;
            temp = array[i];
        }
    }
    return size;
}

int[,] RequencyElemsArray(int[] array)
{
    int size = SizeRequencyElemsArray(array);
    int temp = 0;
    int[,] matrix = new int[size, 2];
    int index = -1;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] != temp)
        {
            index++;
            temp = array[i];
            matrix[index, 0] = array[i];
        }
        if (array[i] == temp)
            matrix[index, 1]++;
    }
    return matrix;
}

void PrintMatrixSpecial(int[,] matrix, string beginRow, string firstRow, string endRow)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        Console.Write(beginRow);
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (j == 0)
                Console.Write($"{matrix[i, j],2}{firstRow}");
            else Console.Write($"{matrix[i, j],2}");
        }
        Console.WriteLine(endRow);
    }
}

int[,] matrix1 = CreateMatrixRndInt(4, 4, 1, 9);
PrintMatrix(matrix1, "", "", "");
Console.WriteLine();
int[] array1 = MatrixToArray(matrix1);
Array.Sort(array1);
PrintArray(array1);
Console.WriteLine();
int[,] requencyElemsArray = RequencyElemsArray(array1);
PrintMatrixSpecial(requencyElemsArray, "Число", " повторяется", " раз");