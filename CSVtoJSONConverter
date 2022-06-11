import json

csv_file = open('csv-file.txt', 'r')
clubs = [clubs.strip() for clubs in csv_file.readlines()]
csv_file.close()

clubs_keys = ['club', 'city', 'country']
clubs_list = []
for club in clubs:
    split_club = (club.split(','))
    clubs_dictionary = {clubs_keys[i]: split_club[i] for i in range(len(clubs))}
    clubs_list.append(clubs_dictionary)

json_file = open('json-file.txt', 'w')
json.dump(clubs_list, json_file)
json_file.close()
