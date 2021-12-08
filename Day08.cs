namespace aoc
{
    public class Day08 : IDay
    {

        record Sequence(string[] patterns, string[] signals);

        public (string, string) Compute(string[] input)
        {
            var uniqueDigits = new int[] { 2, 4, 3, 7 };
            var sequences = new List<Sequence>();
            foreach (var line in input)
            {
                var chunks = line.Split(" | ");
                sequences.Add(new Sequence(chunks[0].Split(" "), chunks[1].Split(" ")));
            }

            var digitMapping = new Dictionary<int, string>
            {
                [1] = "cf",
                [7] = "acf",
                [4] = "bcdf",
                [2] = "acdeg",
                [3] = "acdfg",
                [5] = "abdfg",
                [0] = "abcefg",
                [6] = "abdefg",
                [9] = "abcdfg",
                [8] = "abcdefg",
            };

            var wireMapping = new Dictionary<string, int>
            {
                ["cf"] = 1,
                ["acf"] = 7,
                ["bcdf"] = 4,
                ["acdeg"] = 2,
                ["acdfg"] = 3,
                ["abdfg"] = 5,
                ["abcefg"] = 0,
                ["abdefg"] = 6,
                ["abcdfg"] = 9,
                ["abcdefg"] = 8
            };

            var digits = digitMapping.GroupBy(kvp => kvp.Value.Length, kvp => kvp.Key).ToDictionary(g => g.Key, g => g.ToList());

            var sum = 0;

            foreach (var (patterns, signals) in sequences)
            {
                var wireCount = patterns.SelectMany(p => p.ToCharArray()).GroupBy(g => g).GroupBy(g => g.Count(), g => g.Key).ToDictionary(g => g.Key, g => g.ToList());
                var associationMap = new Dictionary<char, HashSet<char>>
                {
                    ['a'] = new(wireCount[8]),
                    ['b'] = new(wireCount[6]),
                    ['c'] = new(wireCount[8]),
                    ['d'] = new(wireCount[7]),
                    ['e'] = new(wireCount[4]),
                    ['f'] = new(wireCount[9]),
                    ['g'] = new(wireCount[7]),
                };

                foreach (var pattern in patterns.Where(p => uniqueDigits.Contains(p.Length)))
                {
                    var possibleDigits = digits[pattern.Length];
                    HashSet<char> possibleSegments = new(possibleDigits.SelectMany(d => digitMapping[d].ToCharArray()));
                    foreach (var (position, possibleWires) in associationMap)
                    {
                        if (possibleSegments.Contains(position))
                        {
                            associationMap[position] = new(associationMap[position].Intersect(pattern.ToCharArray()));
                        }
                        else
                        {
                            foreach (var ch in pattern)
                            {
                                associationMap[position].Remove(ch);
                            }
                        }
                    }
                }

                var reverseAssociationMap = new Dictionary<char, char>();
                foreach (var (k, v) in associationMap)
                {
                    reverseAssociationMap[v.First()] = k;
                }
                sum += Convert.ToInt32(string.Join("", signals
                    .Select(signal => signal.Select(c => reverseAssociationMap[c]).OrderBy(c => c).ToArray())
                    .Select(c => wireMapping[new string(c)])));
            }



            var c = sequences.SelectMany(s => s.signals).Count(s => uniqueDigits.Contains(s.Length));

            return ($"{c}", $"{sum}");
        }
    }
}