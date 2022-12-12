namespace Day_4
{

    internal class Program
    {
        static void Main(string[] args)
        {
            // DAY 4 , PART 1
            // In how many assignment pairs does one range fully contain the other?

            string text = File.ReadAllText(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 4\puzzleinput.txt");

            string[] lines = text.Split("\r\n");

            int sum = 0;

            for (int i = 0; i < lines.Length; i++) {
                string[] localline = lines[i].Split(',');
                // case where the second range is fully contained in the first
                if (int.Parse(localline[0].Split('-')[0]) < int.Parse(localline[1].Split('-')[0])) {
                    if (int.Parse(localline[0].Split('-')[1]) >= int.Parse(localline[1].Split('-')[1])) {
                        sum++;
                    }
                }
                // case where the first range is fully contained in the second
                else if (int.Parse(localline[0].Split('-')[0]) > int.Parse(localline[1].Split('-')[0])) {
                    if (int.Parse(localline[0].Split('-')[1]) <= int.Parse(localline[1].Split('-')[1])) {
                        sum++;
                    }
                }
                else if (int.Parse(localline[0].Split('-')[0]) == int.Parse(localline[1].Split('-')[0])) {
                    sum++;
                }

            }

            Console.WriteLine("Answer to PART 1: " + sum);

            // DAY 4 , PART 2
            // Find the number of assignment pairs where the range do overlap 

            sum = 0;

            for (int i = 0; i < lines.Length; i++) {
                string[] localline = lines[i].Split(',');
                if (int.Parse(localline[0].Split('-')[0]) < int.Parse(localline[1].Split('-')[0])) {
                    if (int.Parse(localline[0].Split('-')[1]) < int.Parse(localline[1].Split('-')[0])) {
                        // nothing happens xD get jebaited
                    }
                    else {
                        sum++;
                    }
                }
                else if (int.Parse(localline[0].Split('-')[0]) > int.Parse(localline[1].Split('-')[0])) {
                    if (int.Parse(localline[0].Split('-')[0]) > int.Parse(localline[1].Split('-')[1])) {
                        // nothing happens here either lol
                        // prob a weird way of checking ngl
                    }
                    else {
                        sum++;
                    }
                }
                else {
                    sum++;
                }

            }

            Console.WriteLine("Answer to PART 2: " + sum);

        }
    }
}