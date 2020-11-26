from selenium  import webdriver
import time

def getHtml(url, click_link_text = None, scroll_link_text = None, year=None, waittime = 2):
    
    '''
    Paramters:
    url - (http url): the entrance page we will get html from
    click_link_text - (string): the text of link that you want to click
    scroll_link_text - (string): the text of link that window need to scroll to view
    year - (int) Default None is year of recent updated quarter, What year's fund data do you want to get
    waittime: seconds the browser will wait after initial load and
    
    Returns:
    html - html code
    '''
    browser = webdriver.Chrome('chromedriver')
    browser.maximize_window()
    browser.get(url)
    time.sleep(waittime)
    if scroll_link_text:
        scroll_to_ele = browser.find_element_by_link_text(scroll_link_text)
        browser.execute_script("arguments[0].scrollIntoView();",scroll_to_ele)
        
    if click_link_text:
        click_button = browser.find_element_by_link_text(click_link_text)
        click_button.click()
        time.sleep(waittime)
    handles = browser.window_handles
    current_handle = browser.current_window_handle
    for handle in handles:
        if handle != current_handle:
            browser.switch_to.window(handle)
        else:
            continue
    if year: # 仅限于对基金页面年份的选择
        year_button = browser.find_element_by_css_selector('div#pagebar label[value="'+str(year)+'"]')
        year_button.click()
        time.sleep(waittime)
    html = browser.page_source
    browser.quit()
    return html
