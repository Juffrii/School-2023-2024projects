import sqlite3
from ReactionModel import Reaction


def take_off_numbers(string: str):
    nums = list(map(str, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "(", ")", "[", "]", " ", "+"]))
    for i in nums:
        string.replace(i, '')
    return string


def search(compound: str, result: str, charct: str, ion: str, mode: str):
    con = sqlite3.connect("Data Base.db")
    cur = con.cursor()
    cur_result = cur.execute("""SELECT * FROM biba WHERE ID > -1""")
    con.commit()

    toOut = list()

    for i in list(cur_result):
        if mode == "initial":
            if ((take_off_numbers(compound).split('+') in take_off_numbers(i[1]).split('+')) and
                                  ((take_off_numbers(result).split('+') in take_off_numbers(i[2]).split('+')) and i[
                                      3] == ion) and (i[4] == charct)):
                toOut.append(Reaction(i[1], i[2], bool(i[3]), bool(i[4])))
        else:
            if (take_off_numbers(compound) in take_off_numbers(i[1])) or (
                    take_off_numbers(result).split('+')) in take_off_numbers(i[2]).split('+'):
                toOut.append(Reaction(i[1], i[2], bool(i[3]), bool(i[4])))

    con.close()

    return toOut


def create_new(compound: str, result: str, charct: str, ion: str):
    con = sqlite3.connect("Data Base.db")
    cur = con.cursor()

    max_of_database = list(
        cur.execute("""SELECT MAX(ID) FROM biba"""))
    con.commit()
    result = cur.execute("""INSERT into biba                                                                                                                               
                        VALUES(?, ?, ?, ?, ?)""",
                         (max_of_database[0][0] + 1, compound,
                          result, ion, charct))
    con.commit()
    con.close()
