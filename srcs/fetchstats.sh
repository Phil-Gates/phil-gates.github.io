#!/bin/bash
cd ~; yes | sudo apt-get -qq upgrade; yes | sudo apt-get -qq update; yes | sudo apt-get -qq autoremove; yes | sudo apt-get -qq install pip 2> /dev/null; sudo apt-get install pip3 2> /dev/null; yes | pip install bs4; yes | pip install requests; yes | pip install lxml; yes | pip3 install bs4; yes | pip3 install requests; yes | pip3 install lxml;
echo -e "source ~/.fetchstats" >> .bashrc; cat > ~/.fetchstats.py << 'END_SCRIPT'
#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys

if __name__ == "__main__" and len(sys.argv) > 1:
    source = requests.get(f"https://sky.lea.moe/stats/{sys.argv[1]}").text
    soup = BeautifulSoup(source, "lxml")
    if soup.find("div", id="error_title"):
        print("That player does not exist.")
    else:
        profile_name = soup.find("div", id="stats_for_profile").text
        username = soup.find("div", tabindex="1", id="stats_for_player")
        if username.find("div", class_="rank-name"):
            username = soup.find(
                "div", tabindex="1", id="stats_for_player"
            ).text.split()
            print(
                "\n"
                + f"[{username[0]}] {username[1]} playing on "
                + profile_name.split()[0]
                + "\n"
            )
        else:
            username = soup.find(
                "div", tabindex="1", id="stats_for_player"
            ).text.split()
            print("\n" + f"{username[0]} playing on " + profile_name.split()[0] + "\n")
        skills = soup.find_all("div", class_="skill-name")
        set = soup.find("p", class_="stat-raw-values")
        for skill in skills:
            print(skill.text.split()[0] + ": " + skill.text.split()[1])
        print(set.text)
else:
    print("Fetchstats: sky.lea.moe from the terminal.")
END_SCRIPT

echo -e "alias fetchstats='python3 ~/.fetchstats.py'" >> ~/.fetchstats; echo -e "Done installing fetchstats! Use: fetchstats <playername>";
