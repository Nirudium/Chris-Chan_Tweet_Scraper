from datetime import datetime
import csv

def writetomainfile(text, date):
    with open("cwctweets-" + datetime.today().strftime('%Y-%m-%d') + ".csv") as cwctweets:
        return