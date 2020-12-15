# -*- coding: utf-8 -*-

# 크롤링 가장 기본형태 + 메일링


import os, sys, urllib.request
from bs4 import BeautifulSoup


def change_useragent(link):
	req = urllib.request.Request(
		link,
		data = None,
		headers = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
			}
		)
	f = urllib.request.urlopen(req)
	html = f.read()
	return html


def crawling_data(link):
	html = change_useragent(link)
	soup = BeautifulSoup(html, "html.parser")
	return soup


def parsing_data(soup):
	data = soup.find_all("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
	data = str(data)
	return data


def mailing(content):
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()
	smtp.login('#fromaddress@gmail.com', '')	# ('email address', 'password')
	msg = MIMEText(content)
	msg['Subject'] = "subject"
	msg['To'] = '#toaddress@gmail.com'
	smtp.sendmail('#fromaddress@gmail.com', '#toaddress@gmail.com', msg.as_string())
	smtp.quit()
	

def main():
	link = "https://github.com/s01va"	# 해당 링크 입력
	soup = crawling_data(link)
	data = parsing_data(soup)	# data는 리스트
	content = data[0] 	# 가공한 data 등 anything
	mailing(content)


if __name__ == '__main__':
	main()
	sys.exit(0)
	