"""Functions to parse a file containing student data."""

import readline


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    school_data = open(filename, 'r')

    for line in school_data:
        houses.add(line.split('|')[2])
    houses.discard('')
    school_data.close()

    return houses


all_houses('cohort_data.txt')


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    school_data = open(filename, 'r')

    for line in school_data:
        # print(str(line.split('|')[4]))
        if cohort in line:
            students.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        elif 'G' in line.split('|')[-1]:
            pass
        elif 'I' in line.split('|')[-1]:
            pass
        elif cohort == 'All':
            students.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        else:
            # students = []
            pass

    # print(students)
    school_data.close()

    return sorted(students)


students_by_cohort('cohort_data.txt')


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    rosters = []

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    school_data = open(filename, 'r')

    for line in school_data:
        # print(str(line.split('|')[4]))
        if "Dumbledore's Army" in line:
            dumbledores_army.append(
                f"{line.split('|')[0]} {line.split('|')[1]}")
        elif "Gryffindor" in line:
            gryffindor.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        elif "Hufflepuff" in line:
            hufflepuff.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        elif "Ravenclaw" in line:
            ravenclaw.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        elif "Slytherin" in line:
            slytherin.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        elif "G" in line.split('|')[-1]:
            ghosts.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        elif "I" in line.split('|')[-1]:
            instructors.append(f"{line.split('|')[0]} {line.split('|')[1]}")
        else:
            pass
    rosters.append(sorted(dumbledores_army))
    rosters.append(sorted(gryffindor))
    rosters.append(sorted(hufflepuff))
    rosters.append(sorted(ravenclaw))
    rosters.append(sorted(slytherin))
    rosters.append(sorted(ghosts))
    rosters.append(sorted(instructors))

    school_data.close()
    return rosters


all_names_by_house('cohort_data.txt')


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    school_data = open(filename, 'r')

    for line in school_data:
        string = f"{line.split('|')[0]} {line.split('|')[1]}, {line.split('|')[2]}, {line.split('|')[3]}, {line.split('|')[4].strip()}"
        all_data.append(tuple(map(str, string.split(', '))))

    school_data.close()

    return all_data


all_data('cohort_data.txt')


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    school_data = open(filename, 'r')

    for line in school_data:
        name1 = (name.split(' ')[0])
        try:
            name2 = (name.split(' ')[1])
        except:
            pass

        if name1 in line.split('|')[0] and name2 in line.split('|')[1]:
            cohort = (f"{line.split('|')[-1].strip()}")
            break
        else:
            cohort = None

        # else:
        #     print(None)

    school_data.close()
    return cohort


get_cohort_for('cohort_data.txt', 'Harry Potter')


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    dup_last_name = set()
    last_name_list = []

    school_data = open(filename, 'r')

    for line in school_data:
        last_name = line.split('|')[1]
        if last_name not in last_name_list:
            last_name_list.append(last_name)
        else:
            dup_last_name.add(last_name)

    school_data.close()
    return dup_last_name


find_duped_last_names('cohort_data.txt')


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    all_housemates = []
    housemates = set()

    school_data = open(filename, 'r')

    for line in school_data:
        string = f"{line.split('|')[0]} {line.split('|')[1]}, {line.split('|')[2]}, {line.split('|')[4].strip()}"
        all_housemates.append(tuple(map(str, string.split(', '))))

    for tup in all_housemates:
        if name == tup[0]:
            houses = tup[1]
            cohorts = tup[2]

    for tup in all_housemates:
        if houses in tup[1] and cohorts in tup[2]:
            housemates.add(tup[0])
            housemates.discard(name)

    # for
    #     if house in line.split('|')[0] and cohort in line.split('|')[1]:
    #         cohort = (f"{line.split('|')[-1].strip()}")
    school_data.close()
    return housemates

    # print(all_housemates)


get_housemates_for('cohort_data.txt', 'Harry Potter')


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
