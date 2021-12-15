using System.Text;
using System.Text.RegularExpressions;

namespace aoc
{
    public class Day13 : IDay
    {
        record Point(int x, int y);
        public (string, string) Compute(string[] input)
        {
            var set = new HashSet<Point>();
            int emptyLine = 0;
            var p1 = 0;
            for (int i = 0; i < input.Length; i++)
            {
                var line = input[i];

                if (line.Length == 0) { emptyLine = i; break; }

                var chunks = line.Split(',');
                set.Add(new Point(Convert.ToInt32(chunks[0]), Convert.ToInt32(chunks[1])));
            }

            var regexp = new Regex(@"fold along (x|y)=(\d+)");
            for (int i = emptyLine + 1; i < input.Length; i++)
            {
                var line = input[i];
                var matches = regexp.Match(line);
                var axis = matches.Groups[1].Value;
                var foldCoord = Convert.ToInt32(matches.Groups[2].Value);

                var toMove = set.Where(p => axis == "x" ? p.x > foldCoord : p.y > foldCoord).ToList();
                foreach (var p in toMove)
                {
                    set.Remove(p);
                    if (axis == "x")
                    {
                        set.Add(p with { x = -p.x + 2 * foldCoord });
                    }
                    else
                    {
                        set.Add(p with { y = -p.y + 2 * foldCoord });
                    }
                }
                if (i == emptyLine + 1) p1 = set.Count;
            }

            var maxX = set.Select(p => p.x).Max();
            var maxy = set.Select(p => p.y).Max();

            var stringBuilder = new StringBuilder();
            stringBuilder.AppendLine();
            for (int y = 0; y <= maxy; y++)
            {
                for (int x = 0; x <= maxX; x++)
                {
                    if (set.Contains(new Point(x, y)))
                    {
                        stringBuilder.Append("▓");
                    }
                    else
                    {
                        stringBuilder.Append(' ');
                    }

                }
                stringBuilder.AppendLine();
            }
            return ($"{p1}", $"{stringBuilder.ToString()}");
        }
    }
}