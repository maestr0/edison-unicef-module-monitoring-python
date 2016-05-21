#!/usr/bin/env python

import sys, time
#import mraa


class Monitoring:
    def start(self):
        print "Monitoring is working"
        time.sleep(2)
        print "Monitoring is working 2"

if __name__ == "__main__":
    m = Monitoring()
    m.start()
