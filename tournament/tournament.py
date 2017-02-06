##########################################
# Project 3: Tournament Results
# Date Started: 02/03/2017
# Date Completed: 02/05/2017
# Submitted by: Fang Wang
##########################################

######################################## Media File ####################################################
# Description:
#Python module that uses the PostgreSQL database to keep track of players and
# matches in a game tournament  using Swiss-system for pairing players in each round.
# Swiss-system tournament:
#
# This file is used to provide access to the database via a library of functions
# which can add, delete or query data in the database to another python program
# (a client program). ultiple tournaments are supported and players can enter
# multiple tournaments. The database returns players' ranking/standing
# based on wins. In the event that multiple players have the same
# number of wins, ranking is calculated by the Opponent Match Wins.

# Overview of functions:
#
# delete_matches(): removes matches from data
# delete_players(): removes players from data
# count_players(tournament_id): counts # of players in given tournament
# register_player(name): registers player
# player_standings(tournament_id):  returns the current standings
# report_match(winner, loser, tournament_id): report match results
# swiss_pairings(tournament_id): calculates appropriate match pairings
########################################################################################################
#!/usr/bin/env python

import psycopg2

def connect():
    """
    Connect to PostgreSQL database. Returns connection and cursor.
    This API opens a connection to the PostgreSQL database. If database is
    opened successfully, it returns a connection object.
    """
    try:
        db = psycopg2.connect("dbname=tournament")
        cursor = db.cursor()
        return db, cursor
    except:
        print "Error while trying to connect to database"
def query(sql):
    """execute SQL query"""
    db,cur=connect()
    cur.execute(sql)

    # use fetchone() for reusability
    res=cur.fetchone()
    db.close()
    return res

def commit(sql, data=None):
    """Execute SQL statment and commits transaction"""
    db,cur=connect()
    if data==None:
        cur.execute(sql)
    else:
        cur.execute(sql,(data,))
    db.commit()
    db.close




def delete_matches():
    """Removes all the match records and from database."""

    sql="""DELETE FROM matches;"""
    commit(sql)


def delete_players():
    """Removes all the player as well as match records from database."""

    sql="""DELETE FROM players;"""
    commit(sql)


def count_players():
    """Returns the number of players currently registered."""

    sql = """SELECT count(*) FROM players;"""
    res=query(sql)
    return res[0]


def register_player(name):
    """Adds a player to the tournament database.

    Args:
        name: the player's full name (need not be unique).
    """

    sql= """INSERT INTO players(name) VALUES(%s);"""
    commit(sql,name)

def player_standings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    sql="""SELECT * FROM standings;"""
    db,cur=connect()
    cur.execute(sql)
    res=cur.fetchall()
    return res

def report_match(winner_id, loser_id):
    """Records the outcome of a single match between two players.

    Args:
        winner:  the id number of the player who won
        loser:  the id number of the player who lost
        tournament_id:  the match's tournament id
    """

    # Add players into matches table:
    sql = "INSERT INTO matches (winner_id, loser_id) \
            VALUES(%s, %s);"
    db,cur=connect()
    cur.execute(sql,(winner_id,loser_id))
    db.commit()
    db.close()


def swiss_pairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each
    player appears exactly once in the pairings.  Each player is paired
    with another player with an equal or nearly-equal win record, that
    is, a player adjacent to him in the standings.

    Returns:
         list of tuples, each containing (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    sql="SELECT id, name FROM standings;"
    db,cur=connect()
    cur.execute(sql)
    standings=cur.fetchall()
    pairs=[]

    for i in range(0,count_players()-1,2):
        pairs.append(standings[i]+standings[i+1])
    return pairs
