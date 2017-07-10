#!/usr/bin/env python

# -----------------------------------------------------------
# Functions for modifying data in SQL databases
# Written for the 2017 Columbia Makerspace swipe system
# - Yonah Elorza 2017, database collaboration by Max Aalto
# -----------------------------------------------------------

from datetime import datetime
import sys


def add_user(uid, uni, lastname, firstname):
    print(uid, uni, lastname, firstname)
    # TODO: write to redis with no perms by default


def change_permissions(uid, field, perm, dct):

    try:
        current_list = dct[uid]
        if (field == 'user'):
            current_list[3] = perm
        elif (field == 'drill'):
            current_list[4] = perm
        elif (field == 'mill'):
            current_list[5] = perm
        elif (field == 'sewing'):
            current_list[6] = perm
        elif (field == 'printer'):
            current_list[7] = perm
        elif (field == 'solder'):
            current_list[8] = perm
        elif (field == 'oscope'):
            current_list[9] = perm
        elif (field == 'vinyl'):
            current_list[10] = perm
        elif (field == 'laser'):
            current_list[11] = perm
        elif (field == 'super'):
            current_list[12] = perm
        elif (field == 'banned'):
            current_list[13] = perm
            dct[uid] = current_list
    except:
        e = sys.exc_info()[0]
        return e

# Not currently implemented
'''
def log_entry(uid, uni, cnx):

    try:
        cursor = cnx.cursor()
        LOG_ADD = ("INSERT INTO entries "
        "(uid, uni, timestamp) "
        "VALUES (%s, %s, %s)")

        LOG_DATA = (uid, uni, datetime.now().strftime("%A, %d %B %Y %I:%M%p"))

        res = cursor.execute(LOG_ADD, LOG_DATA)
        cnx.commit()
        cursor.close()
        return res
    except:
        e = sys.exc_info()[0]
        return e
'''

# Function for querying the credentials (if any exist) for
# a given swiped card
# To call this function:
#   Pass the UID of the card, the field to query, and the MySQL db connection


def change_permissions(uni, **fields):
    print(uni, fields)
    #  for h, i in dct.iteritems():
        #  if(i[0] == uni):
            #  if (field == 'user'):
                #  i[3] = perm
            #  elif (field == 'drill'):
                #  i[4] = perm
            #  elif (field == 'mill'):
                #  i[5] = perm
            #  elif (field == 'sewing'):
                #  i[6] = perm
            #  elif (field == 'printer'):
                #  i[7] = perm
            #  elif (field == 'solder'):
                #  i[8] = perm
            #  elif (field == 'oscope'):
                #  i[9] = perm
            #  elif (field == 'vinyl'):
                #  i[10] = perm
            #  elif (field == 'laser'):
                #  i[11] = perm
            #  elif (field == 'super'):
                #  i[12] = perm
            #  elif (field == 'banned'):
                #  i[13] = perm
                #  h = i
