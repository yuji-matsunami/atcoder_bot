import requests
from bs4 import BeautifulSoup

def get_contest():
    response = requests.get('https://atcoder.jp/contests/')
    soup = BeautifulSoup(response.text, 'html.parser')
    upcoming_table = soup.select_one('#contest-table-upcoming')
    contest_list = upcoming_table.select('tr')
    for i in range(1, len(contest_list)):
        contest_type = contest_list[i].find_all(title="Algorithm")
        if len(contest_type) != 1: continue
        time = contest_list[i].find('time').text
        contest_name = contest_list[i].find_all('a')[-1].text
        if 'AtCoder Beginner Contest' in contest_name:
            return (time, contest_name)
    return 0

if __name__=='__main__':
    print(get_contest())