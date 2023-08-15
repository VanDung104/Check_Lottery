import requests
import bs4
import argparse
import json

result = dict()
points = dict()
def init1():
    res = requests.get("https://ketqua.vn")
    tree = bs4.BeautifulSoup(res.text,"html.parser")
    special_prize = tree.find('td', attrs={"class": "txt-special-prize"})
    result["special_prize"] = [special_prize.text.strip()]
    print(special_prize.text.strip())
    result_board = tree.find('div', attrs={'class': 'result-board'})
    rows = result_board.find_all('tr')
    prize_name = None
    for row in rows:
        tmp_name = row.find('td', class_ = "fw-medium")
        if tmp_name:
            prize_name = tmp_name.text.strip()
            result[prize_name] = []
        results = row.find_all('td', class_ = "txt-normal-prize")
        results_list = [item.get_text().strip() for item in results]
        if prize_name:
            result[prize_name] += results_list
    # prizeJson = json.loads(tmp.text)
def init2():
    for prize in result:
        if result[prize]:
            for point in result[prize]:
                points[point] = prize

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('values', nargs='*')
    args = parser.parse_args()
    ok = False
    init1()
    init2()
    for item in args.values:
        for point in points:
            if item == point[-2:]:
                ok = True
                print("Ban danh: {}-->Ngon qua ban trung giai {}" \
                .format(item, points[point]))
    if not ok:
        print("Ket qua hom nay:")
        for prize in result:
            if result[prize]:
                print("{}:{}".format(prize, result[prize]))


if __name__ == '__main__':
	main()