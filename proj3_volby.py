"""
proj3_volby.py: třetí projekt do Engeto Online Python Akademie

author: Tomáš Balák
email: tomasbalak@gmail.com
discord: Tomáš Balák
"""
import os
import requests
from bs4 import BeautifulSoup
import sys
import csv


# Validate if all 3 arguments are entered
def check_input():
    if len(sys.argv) != 3:
        print("You have not entered valid parameters, please enter the python file name, URL and output csv file and run again.")
        exit()

    # Validate URL
    if "https://www.volby.cz/pls/ps2017nss" not in sys.argv[1]:
        print("Enter valid URL and run again.")
        exit()

    # Validate output file
    if not sys.argv[2].endswith(".csv"):
        print("Provide .csv file format and run again.")
        exit()

    print("Downloading data, please wait.")

# Data from url
def fetch_response(url: str) ->  str:
    with requests.get(url) as response:
        return response

# Convert response to BeautifulSoup object (HTML format)
def parse_html(response: str) -> BeautifulSoup:
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

# Extract relative URLs from the table
def extract_relative_urls(soup: BeautifulSoup) -> list:
    tables = soup.find_all('table')
    url_list = []
    for table in tables:
        a_tags = table.find_all("a")
        for tag in a_tags:
            href = tag.get("href")
            if "vyber=" in href and href not in url_list:
                url_list.append(href)
    return url_list

# Convert relative URLs to absolute URLs
def generate_full_urls(url_list: list) -> list:
    url_base = "https://volby.cz/pls/ps2017nss/"
    urls_to_process = []
    for url in url_list:
        whole_url = url_base + url
        urls_to_process.append(whole_url)
    return urls_to_process

# Process and parse all required URLs
def parse_all_urls(urls_to_process: list) -> list:
    processed_urls = []
    for url in urls_to_process:
        processed_url = parse_html(fetch_response(url))
        processed_urls.append(processed_url)
    return processed_urls

# Extract rows from table
def extract_table_rows(soup: BeautifulSoup) -> list:
    tag_tr = soup.find_all("tr")
    table_row = []
    for table_r in tag_tr:
        table_row.append(table_r.get_text().strip().splitlines())

    return table_row

# Extract city numbers
def extract_city_numbers(table_row: list) -> list:
    city_number_list = []
    for sublist in table_row[2:]:
        if sublist[0] == "-" or sublist[0] == "Obec" or sublist[0] == "číslo":
            continue
        else:
            city_number_list.append(sublist[0])
    return city_number_list

# Extract city names
def extract_city_names(table_row: list) -> list:
    city_name_list = []
    for sublist in table_row[2:]:
        if sublist[1] == "název" or sublist[1] == "Výběrokrsku" or sublist[1] == "-":
            continue
        else:
            city_name_list.append(sublist[1])
    return city_name_list

# Extract number of registered voters
def extract_voter_counts(processed_urls: BeautifulSoup) -> list:
    voters_count = []
    for url in processed_urls:
        voters = url.find("td", {"class": "cislo"}, headers="sa2").get_text()
        voters_count.append(int(voters.replace("\xa0", "")))
    return voters_count

# Extract number of envelopes
def extract_envelope_counts(processed_urls: BeautifulSoup) -> list:
    envelopes_count = []
    for envelopes in processed_urls:
        envelope = envelopes.find("td", {"class": "cislo"}, headers="sa3").get_text()
        envelopes_count.append(int(envelope.replace("\xa0", "")))
    return envelopes_count

# Extract number of valid votes
def extract_valid_vote_counts(processed_urls: BeautifulSoup) -> list:
    valid_votes_count = []
    for votes in processed_urls:
        vote = votes.find("td", {"class": "cislo"}, headers="sa6").get_text()
        valid_votes_count.append(int(vote.replace("\xa0", "")))
    return valid_votes_count

# Extract votes for each political party
def extract_party_votes(processed_urls: BeautifulSoup) -> list:
    all_party_votes = []
    for url in processed_urls:
        votes = url.find_all("td", headers=["t1sb3", "t2sb3"])
        each_party_votes = []
        for vote in votes:
            if vote.get_text().strip() == "-":
                continue
            else:
                each_party_votes.append(vote.get_text().replace("\xa0", ""))
        all_party_votes.append(each_party_votes)
    return all_party_votes

# Extract political party names
def extract_party_names(soup: BeautifulSoup) -> list:
    political_parties = []
    td_tags = soup.find_all("td", {"class": "overflow_name"})
    for tag in td_tags:
        political_parties.append(tag.get_text())
    return political_parties


def final_execute(url: str):
    check_input()
    soup = parse_html(fetch_response(url))
    city_codes = extract_city_numbers(extract_table_rows(soup))
    city_names = extract_city_names(extract_table_rows(soup))
    relative_urls = extract_relative_urls(soup)
    full_urls = generate_full_urls(relative_urls)
    processed_urls = parse_all_urls(full_urls)
    reg_voters = extract_voter_counts(processed_urls)
    envelopes = extract_envelope_counts(processed_urls)
    valid_votes = extract_valid_vote_counts(processed_urls)
    all_votes = extract_party_votes(processed_urls)
    parties = extract_party_names(processed_urls[0])

    # Header row of the output file
    header = ["code", "location", "registered voters", "envelopes", "valid votes", *parties]

    # Creating a single list by zipping the corresponding data together
    data = list(zip(city_codes, city_names, reg_voters, envelopes, valid_votes))

    # Adding the party votes to the data variable and combining them into the final list for CSV
    for i in range(len(data)):
        data[i] = list(data[i]) + all_votes[i]

    return {"header": header, "data": data}

# Writing data to the CSV file
def to_csv(filename: str, data):
        with open(filename, mode="w", encoding="utf-8-sig", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data["header"], delimiter=";")
            writer.writeheader()
            # Writing each row of data into the CSV file
            for row in data["data"]:
                writer.writerow(dict(zip(data["header"], row)))
        print(f"The program finished successfully.\n"
              f"Your output file: {sys.argv[2]} has been created")



if __name__ == '__main__':
    data = final_execute(sys.argv[1])
    to_csv(sys.argv[2], data)