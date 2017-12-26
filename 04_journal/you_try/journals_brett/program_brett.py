import journal_brett
import random
import time
from journal_brett import journal_writer
from tabulate import tabulate

def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------')
    print('      JOURNAL APP')
    print('------------------------')
    print()

def convert_str(list):

    return list

def generate_phrase():
    verbs = "ironize, Conjecture, Illuminate, Expose, Render, Interpret, Contradict, Challenge, Conflict, Analyze, \
             Examine, Study, Signal, Investigate, Scrutinize, Generate, Fashion, Form, Construct"
    adjectives = ["abrasive, acidic, barbarous, bawdy, callous, capricious, daffy, damaged, evanescent, exuberant, \
                exultant"]
    nouns = ["Interferometer, Kite, Wing, Word, Harbor, Peacoat, Water, Eye, Nothing, Sonnet, Wife"]
    verbs.split()
    #convert_str(verbs)
    convert_str(adjectives)
    convert_str(nouns)
    print(random.choice(verbs) + "ing " + random.choice(adjectives) + random.choice(nouns))
    time.sleep(2)
    print("all done!")


def run_event_loop():
    messages = ['What do you got for us today?', 'Hit me with some brilliance', "Hey ma, let's slide.."]
    print(random.choice(messages))
    cmd = 'EMPTY'
    journal_name = 'Default'
    journal_data = journal_brett.load(journal_name)  # [] # list()
    while cmd != 'x' and cmd:
        index = 0
        question_set = ["[L]ist entries, [A]dd an entry, E[x]it:", "What's the MVP?"]
        cmd = input(question_set[index])
        cmd = cmd.lower().strip()
        verb =["test"]

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'delete all':
            delete_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))
    journal_brett.save(journal_name, journal_data)
    journal_writer(journal_data)


def list_entries(data):
   print('Your journal entries: ')
   entries = reversed(data)
   for indx, entry in enumerate(entries):
        print('* [{}] {}'.format(indx + 1, entry))


def add_entry(data):
    name_text = input('Product Name, <enter> to exit: ')
    description_text = input("Describe it ")
    entry_text = name_text + '\n' + description_text
    journal_brett.add_entry(entry_text, data)
    print("...")
    time.sleep(1)
    print("Cool! I'll remember this")


def delete_entries(data):
    journal_brett.delete_entries(data)


if __name__ == '__main__':
    main()