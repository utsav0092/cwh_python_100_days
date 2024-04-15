"""Shout out to everyone"""

from os import system

"""For Mac"""
names = ["Rahul", "Rohan", "Javad", "John"]
for name in names:
    system(f' say shoutout to {name}')
