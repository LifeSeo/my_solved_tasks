// Решение задачи про двух друзей и собаку. Необходимо найти, сколько раз собака успеет пробежать между друзьями.

using System;
class Program {
  static void Main()
{
float count = 0;
float distance = 10000000;
float firstFriendSpeed = 1;
float secondFriendSpeed = 2;
float dogSpeed = 50;
float friend = 2;
float time = 0;


while(distance > 10)
{
    if(friend == 1)
    {
        time = distance / (firstFriendSpeed + dogSpeed);
        friend = 2;
        
    }
    else
    {
        time = distance / (secondFriendSpeed + dogSpeed);
        friend = 1;
       
    }
    distance = distance - (firstFriendSpeed + secondFriendSpeed) * time;
    count++;
}
Console.WriteLine($"Собака пробежит: {count} раз");
  }
}
