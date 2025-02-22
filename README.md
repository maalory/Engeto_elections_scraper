# Engeto_elections_scraper
Script downloads elections results as csv table from www.volby.cz

EN
This program is my latest project for the Engeto online academy course. It lists the voting results for all municipalities for the selected territorial unit (e.g. in this case Brno-venkov) from the portal www.volby.cz

The program is run in the terminal with 2 arguments: a link and the name of the output file, e.g. :
python proj3_volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203" "vysledky_brno_venkov.csv"

In the output csv file, each line contains information for a specific municipality:
- municipality code
- name of the village
- voters in the list
- issued envelopes
- valid votes
- candidate parties (per column, the number of votes for the party for all parties)

The requirements.txt file contains a list of libraries needed to run the script


CZ
Tento program je muj poslední projekt v rámci Engeto online academy. Má za úkol vyscrapovat výsledky hlasování pro všechny obce za zvolený územní celek (napr. v tomto prípade Brno-venkov) z portálu www.volby.cz

Program se spouští v terminálu pomocí 2 argumentu: odkaz a název výstupního souboru, napr. :
python proj3_volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203" "vysledky_brno_venkov.csv"

Ve výstupním csv souboru obsahuje každý rádek informace pro konkrétní obec:
- kód obce
- název obce
- volici v seznamu
- vydané obálky
- platné hlasy
- kandidující strany (co sloupec, to pocet hlasu pro stranu pro všechny strany)

Soubor requirements.txt obsahuje seznam knihoven potrebných ke spuštení skriptu
