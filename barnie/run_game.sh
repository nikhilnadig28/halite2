#!/bin/sh
rm -rf *.log
rm -rf *.hlt

rm -rf *.results

./halite -d "240 160" "python3 MyBot.py" "python3 MyBot.py" "python3 MyBot.py" "python3 MyBot.py" >> match.results