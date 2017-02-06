# Project_Tournament_Results
Project 4 Relational Databases
Udacity Full Stack Developer Nanodegree

**Project Overview**

In this project, a Python module that uses the PostgreSQL database was written to
keep track of players and matches in a game tournament. I developed a database
schema to store the game matches between players and wrote a Python module to
rank the players and pair them up in matches in a tournament.
The module passes the included unit tests.

*key words**:

Python, Relational Database, PostgreSQl, Psycopg2

You can download all the files: $ git clone https://github.com/fwangboulder/Project_Tournament_Results.git

To structure code well and make sure they are Pep 8 compliant:

install autopep8 and run it for my file.

$ pip install --upgrade autopep8

$ autopep8 --in-place --aggressive --aggressive  filename

**How to run it?**


Step I. Installation required.

1. Install Vagrant and VirtualBox (conceptual overview: https://www.youtube.com/watch?v=djnqoEO2rLc)

    check for success installation by checking the version

    $vagrant --version

2. Download the VM configuration.

    $ git clone https://github.com/udacity/fullstack-nanodegree-vm.git

3. Start the virtual Machine.

    Change to the directory inside called vagrant.

    $cd vagrant

    Display files inside

    $ls

    start: this step is slow (a few minutes) depending on how fast your internet is.

    $vagrant up

4. Log in to your newly installed Linux VM.

    $vagrant ssh

5. Test for running the database.

    Change to directory /vagrant and look around. You will also see the tournament template inside.

    $cd /vagrant

    $ls

    Start database

    $psql

    vagrant=> create database test;

    connect database

    vagrant=>\c test

    display table

    vagrant=>\dt

    vagrant=>create table a(id serial primary key, name text)

    quit database

    vagrant=>\q

6. Logging out and in VM.

    $exit

    Log in again.

    $vagrant ssh

    If the computer is rebooted, you need to run vagrant up to restart the VM.

Step II. Git clone this repository.

1. Change directory to this repository.

    $cd Project_Tournament_Results

2. Start virtual Machine (a few minutes).

    $vagrant up

3. Login to Linux VM.

    $vagrant ssh

4. Change directory to tournament.

    $cd /vagrant/tournament

5. Look around and then Run the test file.

    $ls

    ```

    you will see three files inside:

    SQL database and table definitions in a file (tournament.sql)

    Python functions filling out a template of an API (tournament.py):

      # Overview of functions:
      # delete_matches(): removes matches from data
      # delete_players(): removes players from data
      # count_players(tournament_id): counts # of players in given tournament
      # register_player(name): registers player
      # player_standings(tournament_id):  returns the current standings
      # report_match(winner, loser, tournament_id): report match results
      # swiss_pairings(tournament_id): calculates appropriate match pairings

    A test suite to verify the code (tournament_test.py)

    ```

    $python tournament_test.py

    you will see the follow results.

      ```
      1. Old matches can be deleted.
      2. Player records can be deleted.
      3. After deleting, count_players() returns zero.
      4. After registering a player, count_players() returns 1.
      5. Players can be registered and deleted.
      6. Newly registered players appear in the standings with no matches.
      7. After a match, players have updated standings.
      8. After one match, players with one win are paired.
      Success!  All tests pass!

      ```
