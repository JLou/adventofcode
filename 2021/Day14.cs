using System.Text;
using System.Text.RegularExpressions;

namespace aoc
{
    public class Day14 : IDay
    {
        static Dictionary<(string, int), Dictionary<char, long>> Memo = new();
        public (string, string) Compute(string[] input)
        {

            var polymer = input[0];
            var rules = new Dictionary<string, string>();
            for (int i = 2; i < input.Length; i++)
            {
                var r = new Regex(@"(.*) -> (.)");
                var chunks = r.Match(input[i]).Groups.Values.ToArray();
                rules.Add(chunks[1].Value, chunks[2].Value);

            }
            var c = 0;
            var tRules = new Dictionary<string, string>();
            foreach (var (rule, _) in rules)
            {
                var output = rule;
                for (int step = 0; step < 10; step++)
                {
                    var sb = new StringBuilder();
                    sb.Append(output[0]);
                    for (int i = 1; i < output.Length; i++)
                    {
                        var pair = output[(i - 1)..(i + 1)];
                        if (rules.ContainsKey(pair))
                        {
                            sb.Append(rules[pair]);
                        }
                        sb.Append(output[i]);
                    }
                    output = sb.ToString();
                }
                tRules[rule] = output;
            }

            var counts = CountOccurences(polymer, tRules, 4);
            var c2 = counts.Max(c => c.Value) - counts.Min(c => c.Value);

            return ($"{c}", $"{c2}");
        }

        Dictionary<char, long> CountOccurences(string chunk, Dictionary<string, string> rules, int depth, bool root = true)
        {
            if (Memo.ContainsKey((chunk, depth))) { return Memo[(chunk, depth)]; }

            var pairs = new List<string>();
            for (int i = 1; i < chunk.Length; i++)
            {
                var pair = chunk[(i - 1)..(i + 1)];
                if (rules.ContainsKey(pair))
                {
                    pairs.Add(rules[pair]);
                }
                else
                {
                    pairs.Add(pair);
                }
            }

            if (depth == 0)
            {

                if (rules.ContainsKey(chunk))
                {
                    return rules[chunk].GroupBy(c => c).ToDictionary(c => c.Key, c => c.LongCount());
                }
                var d = chunk.GroupBy(c => c).ToDictionary(c => c.Key, c => c.LongCount());
                d[chunk[^1]]--;

                Memo[(chunk, depth)] = d;

                return d;
            }

            var v = pairs.Select(p => CountOccurences(p, rules, depth - 1, false));
            var dict = new Dictionary<char, long>();
            foreach (var dico in v)
            {
                foreach (var (k, value) in dico)
                {
                    if (!dict.ContainsKey(k))
                    {
                        dict.Add(k, 0);
                    }
                    dict[k] += value;
                }
            }
            if (root)
            {
                dict[chunk[^1]]++;
            }

            Memo[(chunk, depth)] = dict;

            return dict;
        }
    }
}