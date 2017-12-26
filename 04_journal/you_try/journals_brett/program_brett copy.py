import journal_brett
import random

def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------')
    print('      JOURNAL APP')
    print('------------------------')
    print()



def run_event_loop():
    messages = ['What do you got for us today?', 'Hit me with some brilliance', "Hey ma, let's slide.."]
    print(random.choice(messages))
    cmd = 'EMPTY'
    journal_name = 'Default'
    journal_data = journal_brett.load(journal_name)  # [] # list()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'delete all':
            delete_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))
    print('Done, goodbye. ')
    journal_brett.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for indx, entry in enumerate(entries):
        print('* [{}] {}'.format(indx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal_brett.add_entry(text, data)

def delete_entries(data):
    journal_brett.delete_entries(data)


if __name__ == '__main__':
    main()