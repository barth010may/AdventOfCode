using System.Collections;

namespace Day_5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // DAY 5, PART 1
            // Return the top Letter of every stack after the given procedures

            Stack one = new Stack();
            Stack two = new Stack();
            Stack three = new Stack();
            Stack four = new Stack();
            Stack five = new Stack();
            Stack six = new Stack();
            Stack seven = new Stack();
            Stack eight = new Stack();
            Stack nine = new Stack();
            Stack temp = new Stack();

            char[] oneArray = { 'R', 'G', 'J', 'B', 'T', 'V', 'Z'};
            char[] twoArray = { 'J', 'R', 'V', 'L'};
            char[] threeArray = { 'S', 'Q', 'F'};
            char[] fourArray = { 'Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'};
            char[] fiveArray = { 'R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'};
            char[] sixArray = { 'S', 'W', 'T', 'C', 'H', 'F'};
            char[] sevenArray = { 'D', 'Z', 'C', 'V', 'F', 'N', 'J'};
            char[] eightArray = { 'L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q' };
            char[] nineArray = { 'J', 'B', 'W', 'V', 'P' };

            void PushArray(Stack stack, char[] array)
            {
                foreach (char letter in array) {
                    stack.Push(letter);
                }
            }

            PushArray(one, oneArray);
            PushArray(two, twoArray);
            PushArray(three, threeArray);
            PushArray(four, fourArray);
            PushArray(five, fiveArray);
            PushArray(six, sixArray);
            PushArray(seven, sevenArray);
            PushArray(eight, eightArray);
            PushArray(nine, nineArray);

            Stack[] stacks = { one, two, three, four, five, six, seven, eight, nine, temp };

            string text = File.ReadAllText(@"C:\Users\Borup\C#\AdventOfCode\AdventofCode\Day 5\puzzleinput.txt");

            string[] lines = text.Split("\r\n");

            /*foreach (string line in lines) {
                string[] splitString = line.Split(' ');
                int amountMoved = int.Parse(splitString[1]);
                int fromStack = int.Parse(splitString[3]);
                int toStack = int.Parse(splitString[5]);

                for (int i = 0; i < amountMoved; i++) {
                    stacks[toStack - 1].Push(stacks[fromStack - 1].Pop());
                }
            }

            Console.WriteLine("Answer to Part 1: " + one.Peek() + two.Peek() + three.Peek() + four.Peek() + five.Peek() + six.Peek() + seven.Peek() + eight.Peek() + nine.Peek());
            */

            // DAY 5, PART 2
            // List the top letters in each stack, with a different ordering procedure

            foreach (string line in lines) {
                string[] splitString = line.Split(' ');
                int amountMoved = int.Parse(splitString[1]);
                int fromStack = int.Parse(splitString[3]);
                int toStack = int.Parse(splitString[5]);

                for (int i = 0; i < amountMoved; i++) {
                    temp.Push(stacks[fromStack - 1].Pop());
                }
                for (int i = 0; i < amountMoved; i++) {
                    stacks[toStack - 1].Push(temp.Pop());
                }
            }

            Console.WriteLine("Answer to Part 2: " + one.Peek() + two.Peek() + three.Peek() + four.Peek() + five.Peek() + six.Peek() + seven.Peek() + eight.Peek() + nine.Peek());


        }
    }
}