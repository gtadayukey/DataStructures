using ArrayImplementation;

MyArray<int> myArray = new();

myArray.Push(1); // [1]
myArray.Push(3); // [1, 3]
myArray.Push(5); // [1, 3, 5]
myArray.Push(7); // [1, 3, 5, 7]
myArray.Pop(); // [1, 3, 5]
myArray.Pop(); // [1, 3]
myArray.Push(2); // [1, 3, 2]
myArray.Push(4); // [1, 3, 2, 4]
myArray.Push(6); // [1, 3, 2, 4, 6]
myArray.Delete(0); // [3, 2, 4, 6]
myArray.Delete(2); // [3, 2, 6]

Console.WriteLine(myArray);

