"""Functions to parse a file containing student data."""


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

    cohort_data = open(filename)

    for line in cohort_data:
        house = line.rstrip().split('|')[2]
        if house:
            houses.add(house)

    return houses


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

    cohort_data = open(filename)

    for line in cohort_data:
        # The `_` is a way to say, "Hey don't worry about this variable
        # because we'll never use it --- we only care about `first`,
        # `last`, and `cohort_name`.
        #
        # Python doesn't handle underscores in a special way or anything ---
        # it's still just a variable name.
        first, last, _, _, cohort_name = line.rstrip().split('|')

        if cohort_name not in ('I', 'G') and cohort in ('All', cohort_name):
            students.append(f'{first} {last}')

    return sorted(students)


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

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    cohort_data = open(filename)

    for line in cohort_data:
        first, last, house, _, cohort_name = line.rstrip().split('|')

        full_name = f'{first} {last}'

        if house:
            if house == "Dumbledore's Army":
                dumbledores_army.append(full_name)
            elif house == 'Gryffindor':
                gryffindor.append(full_name)
            elif house == 'Hufflepuff':
                hufflepuff.append(full_name)
            elif house == 'Ravenclaw':
                ravenclaw.append(full_name)
            elif house == 'Slytherin':
                slytherin.append(full_name)
        else:
            # If the person doesn't have a house, they're a non-student.
            # For now, the only non-students are ghosts and instructors
            if cohort_name == 'G':
                ghosts.append(full_name)
            elif cohort_name == 'I':
                instructors.append(full_name)

    return [sorted(dumbledores_army),
            sorted(gryffindor),
            sorted(hufflepuff),
            sorted(ravenclaw),
            sorted(slytherin),
            sorted(ghosts),
            sorted(instructors), ]


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

    cohort_data = open(filename)

    for line in cohort_data:
        first, last, house, advisor, cohort_name = line.rstrip().split('|')
        all_data.append((f'{first} {last}', house, advisor, cohort_name))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    for full_name, _, _, cohort_name in all_data(filename):
        if full_name == name:
            return cohort_name


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

    dupes = set()
    seen = set()

    for full_name, _, _, _ in all_data(filename):
        last = full_name.split(' ')[-1]

        if last in seen:
            dupes.add(last)

        seen.add(last)

    return dupes


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    housemates = set()

    target_person = None
    for person in all_data(filename):
        full_name, house, advisor, cohort_name = person

        if full_name == name:
            target_person = person
            break

    if target_person:
        target_name, target_house, _, target_cohort = target_person

        for full_name, house, _, cohort_name in all_data(filename):
            if ((house, cohort_name) == (target_house, target_cohort) and
                    full_name != name):
                housemates.add(full_name)

    return housemates


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
