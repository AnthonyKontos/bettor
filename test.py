from bettor_extract import BettorExtractor
from bettor_udf import keyconverter, convert
import cassandra
import time

b = BettorExtractor(lid=3, dt='2022-09-24', dt2='2022-09-25')
#b.extract_lh()
#sleep(10)
#b.extract_ol()
#sleep(10)
#b.extract_teams()
#sleep(10)
#b.extract_ev()
#sleep(10)
#b.extract_ch()
#sleep(10)
start_time = time.time()
b.extract_cl()
print("--- %s seconds ---" % (time.time() - start_time))
#sleep(10)
#b.extract_bl()


# participants list<participantsType, participantsType>,
# scores list<scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType, scoresType>,


