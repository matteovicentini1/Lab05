# Add whatever it is needed to interface with the DB Table corso
import model.corso as c
from database.DB_connect import get_connection
import model.studente as s


def getesami():
    corsi=[]
    cnx =get_connection()
    cursore=cnx.cursor(dictionary=True)
    query ='''SELECT *
    FROM corso'''
    cursore.execute(query)
    for i in cursore:
        corsi.append(c.Corso(i['nome'],i['codins'],i['crediti'],i['pd']))
    return corsi

def getstudenti():
    studenti=[]
    cnx = get_connection()
    cursore = cnx.cursor(dictionary=True)
    query = '''SELECT *
        FROM studente'''
    cursore.execute(query)
    for i in cursore:
        studenti.append(s.Studente(i['matricola'],i['nome'],i['cognome'],i['CDS']))
    return studenti

def getcoppie():
    coppie = []
    cnx = get_connection()
    cursore = cnx.cursor(dictionary=True)
    query = '''SELECT *
            FROM iscrizione'''
    cursore.execute(query)
    for i in cursore:
        coppie.append((i['matricola'], i['codins']))
    return coppie