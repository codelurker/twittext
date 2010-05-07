#!/usr/bin/env python

import twitterapi
import statusview
import curses

import cursestools as ctools

class Main:
    def __init__(self, conf):
        self.twitter = twitterapi.twitterapi(conf.get_token(), 200)
    
    def start(self, stdcur):
        curses.use_default_colors()
        self.view = statusview.StatusView(stdcur)
        self.hometl = self.twitter.create_timeline("home_timeline", 30)
        self.hometl.reloadEventHandler = self.refresh
        self.hometl.start()
        stdcur.getch()

    def refresh(self, ids):
        statuses = self.twitter.get_statuses(ids)
        ctools.dputs(statuses)
        self.view.refresh(statuses)
