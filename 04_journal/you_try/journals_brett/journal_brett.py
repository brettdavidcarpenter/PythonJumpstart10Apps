import os
import csv

def load(name):
    """

    This creates and loads a new journal

    :param name: This is base name name of the journal to load
    :return: A new journal data structure populated with the file data
    """
    data = []
    filename = get_full_path_name(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(journal_name, journal_data):
    filename = get_full_path_name(journal_name)
    print("....saving to: {0}".format(filename))


    with open(filename, 'w') as file_output:
        for entry in journal_data:
            file_output.write(entry + '\n')


def get_full_path_name(name):
    filename = os.path.abspath(os.path.join('.', 'journals/', name + '.csv'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)


def delete_entries(journal_data):
    journal_data.clear()


def journal_writer(data):
    out = csv.writer(open("myfile.csv", "w"), delimiter=',', quoting=csv.QUOTE_ALL)
    out.writerow(data)


