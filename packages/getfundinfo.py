import loadlinkhtml
from bs4 import BeautifulSoup
class Getfund(object):
    
    def __init__(self,url,sortby=None):
        '''
        Parameters: 
        url - (str) the fund page we will get html from
        sortby - (str) defalut None. How many fields of year of incremental rate you want to sort by desc
        '''
        
        self.url = url
        self.sortby = sortby

    def get_fund_info(self):
        '''
        Get fund infomation of the current page that's sorted by incremental rate fileds of year
        
        Returns:
        table_data_list - (list) the list of needed fund data
        fund_name_urls - (list) the list of url of all specific fund
        fund_table_heads - (list) the list of heads of fund data
        '''
        html = loadlinkhtml.getHtml(url=self.url,click_link_text=self.sortby)
        soup = BeautifulSoup(html,'lxml')
        table = soup.select('div .tableMain')[0].find('table')
        td_list = [td.get_text() for td in table.select('tbody td')]
        f_name_urls = [a.get('href') for a in table.select('tbody td.fname a[href]')] # 获取每只基金详情url
        table_heads = [thead.get_text() for thead in table.find('thead').find_all('th')]
        
        return (td_list,f_name_urls,table_heads)
    
    def split_dataset(self,raw_data,length,start_lid=0):
                       
        '''
        Split a dataset into several small datasets to stand on each one of record in DataFrame

        Parameters: 
        raw_data - (list/tuple/dict/np.array...) the dataset you split from
        length - (int) the num of element contained in splited object
        start_lid - (int) start of index

        Returns:
        splited_datasets: (list) the list of splited datasets
        '''
        data_list = []
        while ((start_lid+1) <= len(raw_data)):
            data_list.append(raw_data[start_lid:start_lid+length])
            start_lid += length
        return data_list
