from rich.style import Style

frosting_color = "magenta"
donut_color = "orange3"
frosting = Style(color=frosting_color)
title = Style(color="red")
donut = Style(color=donut_color)

name_over_blank = Style(color="white")
name_over_donut = Style(color="white", bgcolor=donut_color)
name_over_frosting = Style(color="white", bgcolor=frosting_color)


frosting_on_donut = Style(color=frosting_color, bgcolor=donut_color)
blue_sprinkle = Style(color="blue", bgcolor=frosting_color)
green_sprinkle = Style(color="green", bgcolor=frosting_color)
purple_sprinkle = Style(color="dark_magenta", bgcolor=frosting_color)
yellow_sprinkle = Style(color="yellow", bgcolor=frosting_color)
dark_magenta_sprinkle = Style(color="dark_magenta", bgcolor=frosting_color)

jelly = Style(color="red")
jelly_on_frosting = Style(color="red", bgcolor=frosting_color)

construction_color = "gray37"
construction = Style(color=construction_color)
construction_2 = Style(color="gray37")

red = Style(color="red")

jelly_on_construction = Style(color="red", bgcolor=construction_color)
jelly_on_donut = Style(color="red", bgcolor=donut_color)