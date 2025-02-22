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
Tento program je muj posledn� projekt v r�mci Engeto online academy. M� za �kol vyscrapovat v�sledky hlasov�n� pro v�echny obce za zvolen� �zemn� celek (napr. v tomto pr�pade Brno-venkov) z port�lu www.volby.cz

Program se spou�t� v termin�lu pomoc� 2 argumentu: odkaz a n�zev v�stupn�ho souboru, napr. :
python proj3_volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203" "vysledky_brno_venkov.csv"

Ve v�stupn�m csv souboru obsahuje ka�d� r�dek informace pro konkr�tn� obec:
- k�d obce
- n�zev obce
- volici v seznamu
- vydan� ob�lky
- platn� hlasy
- kandiduj�c� strany (co sloupec, to pocet hlasu pro stranu pro v�echny strany)

Soubor requirements.txt obsahuje seznam knihoven potrebn�ch ke spu�ten� skriptu
