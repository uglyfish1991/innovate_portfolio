#a dictionary

music_list = [
    {
        "artist": "Radiohead",
        "song name": "How to Disappear Completely",
        "Album": "Kid A",
        "genre": "Alt Rock"
    },
    {
        "artist": "My Chemical Romance",
        "song name": "Sleep",
        "Album": "The Black Parade",
        "genre": "Emo"
    },
    {
        "artist": "Killing Joke",
        "song name": "Slave To Substance",
        "Album": "Absolute Dissent",
        "genre": "Industrial Metal"
    },
]

fav_bands=[] # an empty list that I'll append into

for each_dict in music_list:
    fav_bands.append(list(each_dict.values())[0])

# print(fav_bands) <- this was in just to check my list, I didn't need it in the final code


def add_to_list(band): 
    fav_bands.append(band) #This function is used to use the list method .append() and add whatever the user types in to the end of the list.
