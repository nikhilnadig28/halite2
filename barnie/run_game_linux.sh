#!/bin/sh
rm -rf *.log
rm -rf *.hlt
rm -rf *.vec

rm -rf *.results

./halite_linux -d "240 160" "python3 MyBot.py -name=0" "python3 MyBot.py -name=1" "python3 MyBot.py -name=2" "python3 MyBot.py -name=3" >> match.results