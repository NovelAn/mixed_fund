from bs4 import BeautifulSoup
import loadlinkhtml
import numpy as np
import re
class Getshareholds(object):
    def __init__(self, fund_cc_url, num_quarter=None, year=None, waittime=3):
        '''
        Parameters:
        fund_cc_url - The link to access to more stockholds of the fund
        num_quarter - (int) How many quarter of fund stockholds that need to get,
                     Default None stands on the all quarters of the year.
        year - (int) Which year of fund info you want to get
        waittime - (int) How many seconds that page need to load 
       
        '''
        self.fund_cc_url = fund_cc_url
        self.num_quarter = num_quarter
        self.year = year
        self.waittime = waittime
        
    def get_fund_shareholds(self):
    
        html = loadlinkhtml.getHtml(self.fund_cc_url, year=self.year, waittime=self.waittime)
        soup = BeautifulSoup(html,'lxml')
        boxes = soup.select('div#cctable div.box')[:self.num_quarter]
        for i, box in enumerate(boxes):
            s_code = [tr.find_all('td')[1].get_text() for tr in box.select('table tbody tr')]
            s_name = [tr.find_all('td')[2].get_text() for tr in box.select('table tbody tr')]
            end_date = np.repeat(box.select('label.right.lab2.xq505')[0].get_text()[-10:].strip(' '),len(s_code))
            f_code = np.repeat(re.search(r'\d+',box.select('label.left a[href]')[0].get('href')).group(),len(s_code))
            if (i > 0):
                s_shareholds = [tr.find_all('td')[4].get_text() for tr in box.select('table tbody tr')]
                s_data = np.append(s_data,np.array([f_code,s_code,s_name,s_shareholds,end_date]).T,axis=0)
            else:
                s_shareholds = [tr.find_all('td')[6].get_text() for tr in box.select('table tbody tr')]
                s_data = np.array([f_code,s_code,s_name,s_shareholds,end_date]).T

        return s_data
