namespace aoc
{
    public class Day02 : IDay
    {

        record Instructions(string Direction, int Length);

        public (string, string) Compute(string[] input)
        {
            var (h, d) = (0, 0);

            var (h2, d2, a) = (0, 0, 0);
            var instructions = input.Select(l =>
            {
                var chunks = l.Split(' ');
                return new Instructions(chunks[0], int.Parse(chunks[1]));
            });

            foreach (var instruction in instructions)
            {
                var (dh, dp) = instruction switch
                {
                    (Direction: "forward", _) => (instruction.Length, 0),
                    (Direction: "down", _) => (0, instruction.Length),
                    (Direction: "up", _) => (0, -instruction.Length),
                    var _ => (0, 0)
                };
                h += dh;
                d += dp;

                var (dh2, dp2, da) = instruction switch
                {
                    (Direction: "forward", _) => (instruction.Length, instruction.Length * a, 0),
                    (Direction: "down", _) => (0, 0, instruction.Length),
                    (Direction: "up", _) => (0, 0, -instruction.Length),
                    var _ => (0, 0, 0)
                };
                h2 += dh2;
                d2 += dp2;
                a += da;

            }

            Console.WriteLine("h=" + h + ", d=" + d);
            Console.WriteLine("h=" + h2 + ", d=" + d2);
            return ((h * d).ToString(), (h2 * d2).ToString());
        }
    }
}
