namespace aoc
{
    public class Day10 : IDay
    {
        public (string, string) Compute(string[] input)
        {

            var illegals = new List<char>();
            var charMap = new Dictionary<char, char>
            {
                ['{'] = '}',
                ['<'] = '>',
                ['('] = ')',
                ['['] = ']',
            };

            var scoremapMissing = new Dictionary<char, int>
            {
                [')'] = 1,
                [']'] = 2,
                ['}'] = 3,
                ['>'] = 4
            };

            var scores2 = new List<long>();
            foreach (var line in input)
            {
                var stack = new Stack<char>();

                var c = FindIllegalChar(stack, line);
                var score = 0L;
                if (c.HasValue) { illegals.Add(c.Value); }
                else
                {
                    while (stack.Count > 0)
                    {
                        var ch = stack.Pop();
                        var missingCh = charMap[ch];
                        score = score * 5 + scoremapMissing[missingCh];
                    }
                }

            }

            var scoremap = new Dictionary<char, int>
            {
                [')'] = 3,
                [']'] = 57,
                ['}'] = 1197,
                ['>'] = 25137
            };


            return ($"{illegals.Select(c => scoremap[c]).Sum()}", $"{scores2.OrderBy(x => x).ElementAt(scores2.Count / 2)}");
        }

        private static char? FindIllegalChar(Stack<char> stack, string line)
        {
            foreach (var c in line)
            {
                switch (c)
                {
                    case '(':
                    case '{':
                    case '[':
                    case '<':
                        stack.Push(c);
                        break;
                    case ')':
                        if (stack.Pop() != '(') return c;
                        break;

                    case '}':
                        if (stack.Pop() != '{') return c;
                        break;

                    case ']':
                        if (stack.Pop() != '[') return c;
                        break;

                    case '>':
                        if (stack.Pop() != '<') return c;
                        break;
                    default:
                        throw new Exception();
                }
            }
            return null;
        }
    }
}