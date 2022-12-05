namespace aoc
{
    public class Day03 : IDay
    {
        public (string, string) Compute(string[] input)
        {
            var oneCounts = new int[input[0].Length];

            HashSet<string> o2values = new HashSet<string>(input);
            HashSet<string> co2values = new HashSet<string>(input);
            foreach (var line in input.Select(i => i.ToCharArray()))
            {
                for (int i = 0; i < line.Length; i++)
                {
                    if (line[i] == '1')
                    {
                        oneCounts[i]++;
                    }
                }
            }

            int iter = 0;
            while (o2values.Count > 1)
            {
                var (mostMatchingBit, leastMatchingBit) = FindMostCommonBit(o2values, iter);
                foreach (var v in o2values)
                {
                    if (v[iter] != mostMatchingBit) o2values.Remove(v);
                }
                iter++;
            }

            iter = 0;
            while (co2values.Count > 1)
            {
                var (mostMatchingBit, leastMatchingBit) = FindMostCommonBit(co2values, iter);
                foreach (var v in co2values)
                {
                    if (v[iter] != leastMatchingBit) co2values.Remove(v);
                }
                iter++;
            }

            var number = Convert.ToUInt32(oneCounts.Aggregate("", (
                acc,
                next) => next > input.Length / 2 ? acc + '1' : acc + '0'), fromBase: 2);
            var number2 = (~number) << (32 - input[0].Length) >> (32 - input[0].Length);

            var (o2, co2) = (Convert.ToUInt32(o2values.First(), fromBase: 2),
                             Convert.ToUInt32(co2values.First(), fromBase: 2));

            return ((number * number2).ToString(), (o2 * co2).ToString());
        }

        private static (char, char) FindMostCommonBit(HashSet<string> input, int rank)
        {
            int countOnes = 0;
            foreach (var item in input)
            {
                if (item[rank] == '1') countOnes++;
            }

            return countOnes >= (input.Count() - countOnes) ? ('1', '0') : ('0', '1');
        }
    }
}
