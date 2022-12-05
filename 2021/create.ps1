for($i = 5; $i -lt 25; $i++) {
    $day = $i.ToString().PadLeft(2, "0");
$template = @'
namespace aoc
{
    public class Day#day# : IDay
    {
        public (string, string) Compute(string[] input)
        {
            return ("", "");
        }
    }
}
'@.Replace("#day#", $day);

    $name = "Day"+$day+".cs"
    New-Item -Path . -Name $name -ItemType "file" -Value $template
}