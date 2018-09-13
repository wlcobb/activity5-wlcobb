# Activity 5



#this one uses sets
def dedupe1(x):                #function to eliminate dups.
    return list(set(x))

names = ['mary','mary','bill','sam','maria', 'kahn','bill','barry','george','hank','belinda','maria','karthik']
print ('Activity 5 List Duplicator Function')              #heading for the activity
print()
print('Initial List of Names')      #the list of names originally provided
print (names)
print()
my_sorted_list = sorted(dedupe1(names))  #sorting the unduplicated list
print('List of unique names after running through the deduplicator program')
print (my_sorted_list)