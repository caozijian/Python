movies = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
          ["Graham Chapman",["Michael Palin","John Cleese",
                             "Terry Gilliam","Eric Idle","Terry Jones"]]]
def print_lol(the_list,indent=False,level=0):
    for each_list in the_list:
        
            if isinstance(each_list,list):
                # indent and level + 1
                print_lol(each_list,indent,level+1)
            else:
                if indent:
                    for tab_stop in range(level):
                        print("\t",end='')
                    print(each_list)        
                else:
                    print(each_list)        
print_lol(movies,True,0)
        
