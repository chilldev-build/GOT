from pprint import pprint
from characters import characters

##This funtion will ask for a letter and then reply with the count in the character file

#letter = input("Enter a letter and I will tell you how many characters are in the list: ")
#
#def count(n):
#    counter = 0
#
#    for character in characters:
#        if character['name'][0] == n:
#            #pprint(character['name'])
#            counter += 1
#    print(counter)
#
#count(letter)    

## This will count the total characters in the file

#counter = 0
#
#for character in characters:
#    if character['name'] != '':
#        pprint(character['name'])
#        counter += 1
#print(counter)

## This one will count the dead characters 

#counter = 0
#
#for character in characters:
#    if character['died'] != '':
#        pprint(character['died'])
#        counter += 1
#print(counter)

##This will count the names with titles in the titles list

#counter = 0
#
#for character in characters:
#    if character['titles'] != ['']:
#        pprint(character['titles'])
#        counter += 1
#print(counter)


#counter = 0

#for character in characters:
#    #if character['name'] != ['']:
#    print(character['name'],character['titles'])
#        #counter += 1
#print(counter)

#["url"]
#["name"]
#["gender"]
#["culture"]
#["born"]
#["died"]
#["titles"]
#["aliases"]
#["father"]
#["mother"]
#["spouse"]
#["allegiances"]
#["books"]
#["povBooks"]
#["tvSeries"]
#["playedBy"]
#

##Titles Solution from Sean

most_titles = 0

for person in characters:
    num_titles = len(person)['titles']
    if num_titles > most_titles:
        most_titles = num_titles

for person in characters:
    num_titles = len(person)['titles']
    if num_titles == most_titles:
        print('%s has %s titles')

print('nope that\'s it!')


    #if character['name'].startswith('A') == True:
    #    pprint(character['name'])

#print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#     print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))