
// Advent Calendar Day 1:
// Find the Elf carrying the most calories

using System.Diagnostics.CodeAnalysis;

internal class Program {
    private static void Main(string[] args) {

        string text = File.ReadAllText(@"C:\Users\Borup\C#\AdventOfCode\AdventofCode\Day 1\puzzleinput.txt");

        int sum = 0, biggestSum = 0,  answer = 0, s = 0;
        bool parsed;

        string[] subs = text.Split("\r\n");

        foreach (string sub in subs) {

            parsed = int.TryParse(sub, out s);
            if (parsed) {
                s = int.Parse(sub);
            }

            if (sub == "") {
                if (sum > biggestSum) {
                    biggestSum = sum;
                }
                sum = 0;
            }
            else {
                sum += s;
            }
        }

        Console.WriteLine("Answer is: " + biggestSum);
    }
}