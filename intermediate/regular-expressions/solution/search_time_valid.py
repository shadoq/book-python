TEXT = """Apollo 11 was the spaceflight that first landed humans on the Moon. Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:67 UTC. Armstrong became the first person to step onto the lunar surface six hours and 39 minutes later on July 21 at 02:56 UTC; Aldrin joined him 19 minutes later. They spent about two and a quarter hours together outside the spacecraft, and they collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth. Command module pilot Michael Collins flew the command module Columbia alone in lunar orbit while they were on the Moon's surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base before lifting off to rejoin Columbia in lunar orbit."""


import re


PATTERN = '([01][0-9]|[2][0-4]):[0-5][0-9] UTC'

re.search(PATTERN, TEXT)
# <re.Match object; span=(337, 346), match='02:56 UTC'>

re.search(PATTERN, TEXT).group()
# '02:56 UTC'
