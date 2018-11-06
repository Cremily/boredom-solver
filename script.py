#please remember to push!

import os
import random
import sys
base_path = (sys.path[0])
files = os.listdir(base_path)
text = {}
number = 1
for file in files:
    try:
        file_type = file.split('.')[1]
        if file_type == 'txt':
            text.update({str(number):file})
            number += 1
    except IndexError as e:
        print(file,e)
def select_options():
    global text
    print("Choose from:")
    for number in text:
        print(str(number) +": " + text[number])
    print('\n' + "Type all choices, then type end to finish!")
    choices = []
    number_picked = []
    choice_select = ""
    while len(choices) < len(text):
        choice_select = input()
        if choice_select == 'end':
            break
        if choice_select in number_picked:
            continue
        try:
            choices.append(text[choice_select])
            number_picked.append(choice_select)
            string_list = "You selected: "
            for choice in choices:
                string_list += choice + ", "
            string_list = string_list[:-2]
            print(string_list)
        except KeyError as e:
            print("%s is not a valid choice!" % (choice_select))
            print(e)
    if input("Is this correct? Y/N ").lower() in ['n','no']:
        choices = select_options()
    else:
        return choices
choices = select_options()
type_answers = {}
global_answers = []
print(choices)
for choice in choices:
    f = False
    choice = base_path + (r'\%s' % (choice))
    type_answers.update({choice:[]})
    choice_path = choice 
    try:
        f = open(choice_path,'r')
    except Exception as e:
        print("sorry, couldn't find %s!" % choice_path)
        print(e)
    if f:
        for line in f:
            line = line[:-1]
            type_answers[choice].append(line)
            global_answers.append(line)
random_choices = []
base_length = len(base_path)
for ans in type_answers:
    num_of_choices = len(type_answers[ans])
    seed = random.randrange(0,num_of_choices)
    rand_choice = ([ans,type_answers[ans][seed]])
    print("Your chosen %s is %s" % (rand_choice[0][base_length+1:-5].lower(),rand_choice[1]))
    random_choices.append(rand_choice[1])
def global_choice():
    global global_answers
    return global_answers[random.randrange(0,len(global_answers))]
global_ans = global_choice()
while global_ans in random_choices:
    global_ans = global_choice()
print("Your generic choice is %s" % global_ans)
