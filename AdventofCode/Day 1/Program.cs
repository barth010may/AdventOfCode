
// Advent Calendar Day 1:


using System.Diagnostics.CodeAnalysis;

internal class Program {
    private static void Main(string[] args) {

        string text = File.ReadAllText(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 1\puzzleinput.txt");

        int sum = 0, biggestSum = 0, answer = 0, s = 0, biggerSum = 0, bigSum =0;
        bool parsed;

        string[] subs = text.Split("\r\n");

        // FIRST PART SOLUTION
        // Find the sum of Elf carrying the most calories

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

        Console.WriteLine("Answer to part 1: " + biggestSum);

        // SECOND PART SOLUTION
        // Find the sum of the top 3 elves carrying the most calories

        // Check for the 2nd biggest

        foreach (string sub in subs) {

            parsed = int.TryParse(sub, out s);
            if (parsed) {
                s = int.Parse(sub);
            }

            if (sub == "") {
                if (sum > biggerSum && sum < biggestSum) {
                    biggerSum = sum;
                }
                sum = 0;
            }
            else {
                sum += s;
            }
        }

        
        
        // Check for the 3rd biggest
        
        foreach (string sub in subs) {

            parsed = int.TryParse(sub, out s);
            if (parsed) {
                s = int.Parse(sub);
            }

            if (sub == "") {
                if (sum > bigSum && sum < biggerSum) {
                    bigSum = sum;
                }
                sum = 0;
            }
            else {
                sum += s;
            }
        }

        Console.WriteLine("Answer to Part 2: " + (biggestSum + biggerSum + bigSum));
















    }
}