import os
import subprocess
from daemon import runner
import time
import sched, time
import smtplib
fromaddr = 'user_me@gmail.com'
toaddrs  = 'user_you@gmail.com'
msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = 'user_me@gmail.com'
password = 'pwd'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
s = sched.scheduler(time.time, time.sleep)
def print_time(): print "From print_time", time.time()

def print_some_times():
     print time.time()
     s.enter(5, 1, print_time, ())
     s.enter(10, 1, print_time, ())
     s.run()
     print time.time()

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/dist_clean.pid'
        self.pidfile_timeout = 5
        self.cont_flag = True

    def clean(self):
        # ls the directory in question
        # find the first file not in '.', '..'
        # create an email with the file in it and a descriptive subject
        # email to yourself
        # ls the directory
        # if empty, stop the whole app
        # if not empty, schedule the task for tomorrow at noon

    def run(self):
        try:
            while True:
                # schedule the first run at the next noon
                s.enterabs(, 1, clean, ())
                if cont_flag:
                    time.sleep()

        except Exception, e:
            raise

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
