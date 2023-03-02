import extractqueries
from bettor_udf import keyconverter, convert
import cassandra
from time import sleep, time
from datetime import datetime, timedelta
from dateutil import parser
from cassandra.cluster import Cluster
from pysbr import *
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider


class BettorExtractor:

    def __init__(self, lid, dt, dt2):
        self.dt = datetime.strptime(dt, '%Y-%m-%d')
        if dt2 is not None:
            self.dt2 = datetime.strptime(dt2, '%Y-%m-%d')
            self.evnts = EventsByDateRange(lid, self.dt, self.dt2)
        if dt2 is None:
            self.evnts = EventsByDate(lid, self.dt)
        self.mids= [91, 397, 398, 401, 402, 83, 725, 311]
        self.sbs = [5, 3, 10, 8, 28, 108, 9, 93, 65, 83, 44, 29, 15, 16, 18, 82, 20, 84, 35, 54, 38]
        self.tms = [607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, \
                    623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636]

        cluster = Cluster(['127.0.0.1'], port=9042,
                          control_connection_timeout=60)
        self.session = cluster.connect()

    def extract_ol(self):
        events = self.evnts.ids()
        ol = []
        for e in events:
            for sprtbk in self.sbs:
                ol.extend(OpeningLines(e, self.mids, sprtbk).list(self.evnts))
                sleep(0.5)
        ol = keyconverter(ol, convert)

        prepared = self.session.prepare(extractqueries.olextract)
        for line in ol:
            line['datetime'] = parser.parse(line['datetime']).replace(microsecond=0, tzinfo=None)
            line['inverse_odds'] = 1/float(line['decimal_odds'])
            line['spread_total'] = line.pop('spread_/_total')
            bound = prepared.bind(line)
            self.session.execute(bound)

    def extract_ev(self):
        events = self.evnts.list()
        evs = keyconverter(events, convert)
        
        prepared = self.session.prepare(extractqueries.evextract)
        for e in evs:
            e['datetime'] = parser.parse(e['datetime']).replace(microsecond=0, tzinfo=None)
            bound = prepared.bind(e)
            self.session.execute(bound)

    def extract_lh(self):
        events = self.evnts.list()
        evntsids = self.evnts.ids()
        lh = []
        for e, ev in zip(events, evntsids):
            participants = []
            for participant in e['participants']:
                pval = participant['participant id']
                participants.append(pval)
            for sb in self.sbs:    
                for m in self.mids:
                    lh.extend(LineHistory(ev, m, sb, participants).list(self.evnts))
                    sleep(0.6)
        lh = keyconverter(lh, convert)

        prepared = self.session.prepare(extractqueries.lhextract)
        for line in lh:
            line['datetime'] = parser.parse(line['datetime']).replace(microsecond=0, tzinfo=None)
            line['inverse_odds'] = 1/float(line['decimal_odds'])
            line['spread_total'] = line.pop('spread_/_total')
            bound = prepared.bind(line)
            self.session.execute(bound)

    def extract_teams(self):
        teams = [Team(t).list()[0] for t in self.tms]
        teams = keyconverter(teams, convert)
        
        prepared = self.session.prepare(extractqueries.teamextract)
        for tm in teams:
            bound = prepared.bind(tm)
            self.session.execute(bound)

    def extract_ch(self):
        events = self.evnts.ids()
        ch = []
        for e in events:
            ch.extend(ConsensusHistory(e, self.mids).list())
        ch = keyconverter(ch, convert)

        prepared = self.session.prepare(extractqueries.chextract)
        for c in ch:
            c['datetime'] = parser.parse(c['datetime']).replace(microsecond=0, tzinfo=None)
            del c['line']['datetime']
            del c['line']['team_id']
            del c['line']['mtgrp']
            del c['line']['entrid'] 
            bound = prepared.bind(c)
            self.session.execute(bound)

    def extract_cl(self):
        events = self.evnts.ids()
        cl = []
        cl.extend(CurrentLines(events, self.mids, self.sbs).list(self.evnts))
        cl = keyconverter(cl, convert)
        
        prepared = self.session.prepare(extractqueries.clextract)
        for line in cl:
            line['datetime'] = parser.parse(line['datetime']).replace(microsecond=0, tzinfo=None)
            line['inverse_odds'] = 1/float(line['decimal_odds'])
            line['spread_total'] = line.pop('spread_/_total')
            bound = prepared.bind(line)
            self.session.execute(bound)

    def extract_bl(self):
        events = self.evnts.ids()
        bl = []
        for e in events:
            bl.extend(BestLines(e, self.mids).list(self.evnts))
            sleep(0.5)
        bl = keyconverter(bl, convert)
        
        prepared = self.session.prepare(extractqueries.blextract)
        for line in bl:
            line['datetime'] = parser.parse(line['datetime']).replace(microsecond=0, tzinfo=None)
            line['spread_total'] = line.pop('spread_/_total')
            bound = prepared.bind(line)
            self.session.execute(bound)