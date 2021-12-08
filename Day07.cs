namespace aoc
{
    public class Day07 : IDay
    {
        public (string, string) Compute(string[] input)
        {
            var pos = input[0].Split(',').Select(x => Convert.ToInt32(x)).OrderBy(x => x).ToList();

            var meetingPos = pos[pos.Count / 2]; // Median value
            var fuel = pos.Select(p => Math.Abs(p - meetingPos)).Sum();

            var fuel2 = int.MaxValue;
            for (int i = pos[0]; i < pos[^1]; i++)
            {
                var f = pos.Select(x => ComputeFuelBurned(Math.Abs(x - i))).Sum();
                if (f < fuel2)
                {
                    fuel2 = f;
                    Console.WriteLine("meeting at " + i);
                }

            }
            return ($"{fuel}", $"{fuel2}");
        }

        private static int ComputeFuelBurned(int travelDistance)
        {
            return travelDistance * (travelDistance + 1) / 2;
        }
    }
}