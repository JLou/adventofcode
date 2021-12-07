namespace aoc
{
    public class Day06 : IDay
    {
        private Dictionary<int, long> fishForDays = new Dictionary<int, long>();

        public (string, string) Compute(string[] input)
        {
            //var initialFishes = input[0].Split(',').Select(x => 18 - Convert.ToInt32(x) - 1).ToArray();

            long c1 = ComputeForDays(input, 80);
            long c2 = ComputeForDays(input, 256);


            return ($"{c1}", $"{c2}");
        }

        private long ComputeForDays(string[] input, int i)
        {
            fishForDays = new Dictionary<int, long>();

            var initialFishes = input[0].Split(',').Select(x => i + 7 - 1 - Convert.ToInt32(x));

            var c = 0l;
            foreach (var f in initialFishes)
            {
                c += HowManyOffspring(f);
            };

            return c;

        }

        public IEnumerable<int> WillSpawnFishesAt(int daysLeft)
        {
            var currentDay = daysLeft;

            var fishes = new List<int>();
            while (currentDay >= 7)
            {
                fishes.Add(currentDay - 9);
                currentDay -= 7;
            }

            return fishes;
        }
        public long HowManyOffspring(int daysLeft)
        {
            if (daysLeft < 7)
            {
                return 1;
            }
            if (!fishForDays.ContainsKey(daysLeft))
            {
                var offsprings = WillSpawnFishesAt(daysLeft);
                var offCount = offsprings.Select(o => HowManyOffspring(o));

                fishForDays[daysLeft] = offCount.Sum() + 1;
            }
            return fishForDays[daysLeft];
        }
    }
}