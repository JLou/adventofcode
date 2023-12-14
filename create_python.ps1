for ($i = 5; $i -lt 25; $i++) {
    $day = $i.ToString().PadLeft(2, "0");
    $template = @'
with open("./inputs/#day#", 'r') as f:
    lines = f.read().splitlines()
'@.Replace("#day#", $day);

    $name = $day + ".py"
    New-Item -Path ./2023 -Name $name -ItemType "file" -Value $template
}