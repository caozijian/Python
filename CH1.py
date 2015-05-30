'''

'''

"""
List:
zero based.

"""
movies = ["The Holy Gail",
          "The Life of Brian",
          "The Meaning of Life"]
print(movies[0])

#Lenth of the list

print("len(movies)")
print(len(movies))

movies.append("Gilliam")
print("append at the end")
print(movies)


movies.pop()
print("pop up the last item")
print(movies)

movies.extend(["extend 1","extend 2"])
print("extend list")
print(movies)


movies.remove("extend 1")
print("remove items")
print(movies)


#for

print("for loop")
fav_movies = ["The Holy Grail", "The Life of Brian"]
for each_flick in fav_movies:
    print(each_flick)

#while

print("while loop")
count = 0
while count < len(fav_movies):
    print(movies[count])
    count = count + 1
    

#List of list

movies = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",["Michael Palin","John Cleese",
                             "Terry Gilliam","Eric Idle","Terry Jones"]]]
print(movies)
for each_item in movies:
    print(each_item)

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)
