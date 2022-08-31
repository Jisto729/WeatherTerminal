#!/usr/bin/env python

#WeatherTerminal.py: Prints weather information for the next 24 hours from following sites:
__author__ = "Filip Dvořák"


import datetime

import requests, bs4

def get_html_soup_from_link(link:str):
    page = requests.get(link)
    try:
        page.raise_for_status
    except Exception as exc:
        print("A problem occured: %s", exc)
    return bs4.BeautifulSoup(page.text, "html.parser")


def temp_info_in_pocasi():
    soup = get_html_soup_from_link("https://www.in-pocasi.cz/predpoved-pocasi/cz/vysocina/trebic-423/")
    temp_widgets = soup.select("div[id^='h1'][id$='_t']")
    temp_info = []
    for i in range(0, 24):
        #gets the temperature from a widget
        temp_info.append(int((temp_widgets[i].get_text().split(" "))[0]))
    return temp_info

def temp_info_meteoskop():
    soup = get_html_soup_from_link("https://www.meteoskop.cz/pocasi/trebic")
    temp_widgets = soup.select("td[class='temp'] span") #gets all hour widgets
    temp_info = []
    for i in range(1, 25):
        #gets the temperature from a widget
        temp_info.append(int((temp_widgets[i].get_text().split(" "))[0]))
    return temp_info

def temp_info_meteobox():
    return 1

def temp_info_presne_pocasi():
    return 1

def temp_info_weather_com():
    return 1



def print_horizontal_line(length:int):
    for i in range(length):
        print("-", end = "")
    print()

def print_num_with_2_spaces(curr, next):
        if curr in range(-10, 10):
            space = " "
        else:
            space = ""

        if next < 0:
            print(curr, end = space + " ")
        else:
            print(curr, end = space + "  ")

def print_temp_by_hour(temp_info:list):
    print("Temperature:", end = " ")
    for i in range(len(temp_info) - 1):
        print_num_with_2_spaces(temp_info[i], temp_info[i +1 ])
    print(temp_info[len(temp_info) - 1])

def print_24_hours(hour:int):
    print("    Time:   ", end = " ")
    for i in range(24):
        next_hour = hour + 1
        if next_hour >= 24:
            next_hour = 0
        print_num_with_2_spaces(hour, next_hour)
        hour = next_hour
    print()

def print_middle(width:int, string:str):
    if width < len(string):
        print("string too long")
    spaces = int((width - len(string))/2)
    for i in range(spaces):
        print(" ", end="")
    print(string)


if __name__ == '__main__':
    TABLE_WIDTH = 107
    now = datetime.datetime.now()
    #temp = [12, -9, 9, -12, 15, 5, 6, -2, -17, 18, 14, 15, 13, 14, 15, 26, 14, 17, 17, 18, 18, 19, 12, -15]
    #temp_info_meteoskop()
    print_horizontal_line(TABLE_WIDTH)
    print_24_hours(now.hour + 1)
    print_horizontal_line(TABLE_WIDTH)
    print_middle(TABLE_WIDTH, "In-pocasi")
    print_temp_by_hour(temp_info_in_pocasi())
    print_middle(TABLE_WIDTH, "Meteoskop")
    print_temp_by_hour(temp_info_meteoskop())
    print_horizontal_line(TABLE_WIDTH)