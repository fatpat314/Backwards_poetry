import random

def space():
    print("------------------------------")

poem = '''If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!'''

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


def my_own_rearrange():
    print("test")

my_own_rearrange()

#print(lines)


#lines_printed_numbered(lines)
#print(lines)


#lines_printed_random()

#TODO: get a list of strings that contains lines of poem

#Use lines = poem.split("/n")

#Testing code
#lines_printed_backwards(poem_lines_list)
