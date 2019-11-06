import random

def space():
    print("------------------------------")

poem = """I like people.
I’d like some paper people.
They’d be purple paper people. Maybe pop-up purple paper people.
Proper pop-up purple paper people.
“How do you prop up pop-up purple paper people?”
I hear you cry. Well I …
I’d probably prop up proper pop-up purple paper people
With a proper pop-up purple people paperclip,
But I’d pre-prepare appropriate adhesives as alternatives,
A cheeky pack of Blu Tack just in case the paper slipped.
Because I could build a pop-up metropolis.
But I wouldn’t wanna deal with all the paper people politics.
Paper politicians with their paper-thin policies,
Broken promises without appropriate apologies."""

#lines = poem.split("\n")

def lines_printed_backwards(poem_lines_list):
    ''' This function takes in a list of strings containing
    the lines of your poem as arguments and will print the
    poem lines out in reverse with the line numbers reversed
    '''
    lines = poem.split("\n")
    lines.reverse()
    #print(lines)

    line_count = len(lines)

    for i in range(len(lines)):
        line = lines[i]
        print(line_count, line)
        #print(line_count)

        line_count -= 1

space()
print("REVERSED")
space()

lines_printed_backwards(poem)



space()


def lines_printed_random(poem_lines_list):
    ''' function which will randomly select lines from a
    list of strings and print them out in random order. '''


    lines = poem.split("\n")
    line_count = len(lines)
    for i in range(len(lines)):
        sample = random.choices(lines)
        print(line_count,sample)

        line_count -= 1
space()
print("RANDOM")
space()
lines_printed_random(poem)

space()
print("REARRANGED")
space()


def my_own_rearrange():
    lines = poem.split("\n")
    # get each line of the poem into a list


    # call the indexes of this list as I wish.
    rearrange = lines[0], lines[13], lines[2], lines[11], lines[4], lines[9], lines[8], lines[7], lines[6], lines[5], lines[10], lines[3], lines[12], lines[1]

    # rearrange = str(rearrange)
    # rearrange = rearrange.split(",s")

    print(rearrange)

my_own_rearrange()

#print(lines)


#lines_printed_numbered(lines)
#print(lines)


#lines_printed_random()

#TODO: get a list of strings that contains lines of poem

#Use lines = poem.split("/n")

#Testing code
#lines_printed_backwards(poem_lines_list)
