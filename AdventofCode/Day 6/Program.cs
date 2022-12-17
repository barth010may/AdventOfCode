namespace Day_6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // DAY 6, PART 1
            // Find the first start-of-packet marker

            string text = File.ReadAllText(@"C:\Users\Borup\C#\AdventOfCode\AdventofCode\Day 6\puzzleinput.txt");

            int answer = firstMarker(text);

            Console.WriteLine("Answer to PART 1: " + answer);

            answer = messageMarker(text);

            Console.WriteLine("Answer to PART 2: " + answer);

            int firstMarker(string text)
            {
                for (int i = 0; i < text.Length; i++) {
                    char firstLetter = text[i];
                    char secondLetter = text[i + 1];
                    char thirdLetter = text[i + 2];
                    char fourthLetter = text[i + 3];
                    if (firstLetter != secondLetter && firstLetter != thirdLetter && firstLetter != fourthLetter && 
                        secondLetter != thirdLetter && secondLetter != fourthLetter && fourthLetter != thirdLetter) {
                        return i + 4;
                    }
                }
                return 0;
            }

            // DAY 6, PART 2
            // Find the first marker after 14 unique characters

            int messageMarker(string text)
            {
                for (int i = 0; i < text.Length - 14;i++) {
                    string localString = text.Substring(i, 14);
                    if (uniqueCharacters(localString)) {
                        return i + 14;
                    }
                }
                throw new Exception("An answer could not be found!");

            }

            static bool uniqueCharacters(String str)
            {
                // If at any time we encounter 2
                // same characters, return false
                for (int i = 0; i < str.Length; i++)
                    for (int j = i + 1; j < str.Length; j++)
                        if (str[i] == str[j])
                            return false;

                // If no duplicate characters
                // encountered, return true
                return true;
            }
        }
    }
}