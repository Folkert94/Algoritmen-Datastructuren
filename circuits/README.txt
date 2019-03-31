README
Folkert Stijnman
Data Structuren & Algoritmen
10475206

Overview

Voor het runnen van dit programma worden numpy, random en csv gebruikt als
libraries.

In Flat.py vind je de 'Flat'-class die een 7-tal lagen opzet gegeven de gewilde
dimensies. Voor elke node in deze 'Flat'-class is een aparte 'Node'-class
aangemaakt, met aparte north,south,west,east,up en down links naar andere nodes
zodat makkelijk kan worden genavigeerd. Deze nodes kunnen worden veranderd in
gates maar ook in routes.

In extract_solutions.py wordt herhaaldelijk een circuitboard met 7 lagen
aangemaakt, de gates geinitieerd en de paths gezocht. De paths worden eerst
met een A* algoritme gezocht, dan met een A* met subgoals op de hoogste
'dunbevolkste' laag (met de minste paths op de laag) en ten slotte wordt nog
geprobeerd om deze subgoals enigszins te randomiseren op de hoogste
'dunbevolkste' laag.

In find_route in Flat.py vind je het algoritme dat gebruik probeert te maken
van het aantal routes in een bepaalde laag bij het kiezen van de volgende node.
Een node op een laag die 'meer bezet' is, is duurder. Zo wordt geprobeerd te
voorkomen dat lagen te vol raken. Met find_route_sub_goal wordt geprobeerd een
path te vinden via de hoogste laag die het minst bezet is met paths.

In 'test-files' is nog geprobeerd om de routes te sorteren op lengte
(length_test) - langste routes eerst -, of de routes te sorten op gates
die het meest gebruikt worden (priority_paths) - drukste gates eerst.
Dit leverde geen betere resultaten op.
