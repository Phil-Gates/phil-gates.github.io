#!/bin/bash
cd ~; yes | sudo apt-get -qq upgrade; yes | sudo apt-get -qq update; yes | sudo apt-get -qq autoremove; if test -f "/usr/lib/python3/dist-packages/pip"; then yes | pip install lxml -q; yes | pip install requests -q; yes | pip install bs4 -q; elif test -f "/usr/local/lib/python3.9/site-packages/pip"; then yes | pip install lxml -q; yes | pip install requests -q; yes | pip install bs4 -q; else echo -e "Install pip and/or python 3.x"; fi
echo -e "source .fetchstats" >> .bashrc; cat > .fetchstats.py << 'END_SCRIPT'
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
END_SCRIPT; echo -e "alias fetchstats='python3 ~/.fetchstats.py'" >> .fetchstats; echo -e "Done installing fetchstats! Use: fetchstats <playername>";
