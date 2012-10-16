import httplib
import sys
import pdb
LOG = False
if len(sys.argv) > 2:
    LOG = True

URL = "http://www.python.org/index.html"
if len(sys.argv) > 1:
    URL = sys.argv[1]


def logger(fichier, message):
    if LOG:
        fichier.write(message)

F = open("log.txt", "w")
pdb.set_trace()
CONN = httplib.HTTPConnection("cache.univ-st-etienne.fr:3128")
logger(F, "requete sur : %s\n" % URL)
CONN.request("GET", URL)
READ1 = CONN.getresponse()
#print r1.status, r1.reason
logger(F, "Resultat requete : %s %s\n" % (str(READ1.status), READ1.reason))
DATA1 = READ1.read()
COUNT1 = DATA1.count(" ")

COMPT = 0
for i in range(len(DATA1)):
    if DATA1[i] == " ":
        COMPT = COMPT + 1
print DATA1
print COMPT
print COUNT1
CONN.close()
F.close()
