# -*- coding: utf-8 -*-

import os, sys, time, csv
import twitter
from selenium import webdriver

######################################################################

# Twitter API token

# CRK_coupon_auto > Consumer Keys > API Key and Secret
CONSUMERAPIKEY = ""
CONSUMERSECRETKEY = ""

# CRK_coupon_auto > Authentication Tokens > Access Token and Secret
AUTHACCESSTOKEN = ""
AUTHACCESSSECRET = ""

######################################################################

Emails = ["", ""]

HOMEPATH = ""

######################################################################

def couponcodeParsing():
	couponlist = []
	twt_api = twitter.Api(
		consumer_key=CONSUMERAPIKEY,
		consumer_secret=CONSUMERSECRETKEY,
		access_token_key=AUTHACCESSTOKEN,
		access_token_secret=AUTHACCESSSECRET
	)
	
	account = "@CRKingdom_TIPS"
	statuses = twt_api.GetUserTimeline(screen_name=account, count=50, include_rts=True, exclude_replies=False)

	for status in statuses:
		iscoupontwt = False
		if status.text.find("쿠폰") != -1:
			txtlist = status.text.split('\n')
			content = ""
			couponcode = ""
			for txt in txtlist:
				if txt.find(" 쿠폰입니다") != -1:
					content = txt.split(" 쿠폰입니다")[0]
				if len(txt) == 16 and txt.isalpha():
					couponcode = txt
					iscoupontwt = True
				if iscoupontwt == True:
					inputlist = [couponcode, content, status.created_at]
					if inputlist not in couponlist:
						couponlist.append(inputlist)
	
	couponlist = reversed(couponlist)
	return couponlist

def main():
	homepath = HOMEPATH
	if homepath == "":
		homepath = os.getcwd()
	couponlist_csv = homepath + "\\couponlist.csv"

	log_couponlist = []

	if os.path.exists(couponlist_csv) == False:
		ftmp = open(couponlist_csv, 'w')
		ftmp.close()
	else:
		fr = open(couponlist_csv, 'r', newline='')
		reader = csv.reader(fr, delimiter=',')

		for line in reader:
			if not line:
				break
			log_couponlist.append(line)

		fr.close()

	couponlist = list(couponcodeParsing())
	
	if len(log_couponlist) < 1:
		new_couponlist = couponlist
	else:
		lastidx = couponlist.index(log_couponlist[-1])
		new_couponlist = couponlist[lastidx+1:]

	if len(new_couponlist) != 0:
		fa = open(couponlist_csv, 'a', newline='')
		writer = csv.writer(fa, delimiter=',')

		ferror = open(homepath + "\\error.log", 'a')

		options = webdriver.ChromeOptions()
		options.add_argument("headless")
		driver = webdriver.Chrome("./chromedriver.exe", options=options)

		for new_coupon in new_couponlist:
			writer.writerow(new_coupon)
			for email in Emails:
				try:
					driver.get("https://game.devplay.com/coupon/ck/ko")
					driver.find_element_by_id("email-box").send_keys(email)
					driver.find_element_by_id("code-box").send_keys(new_coupon[0])
					driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/form/div[5]/div").click()
					time.sleep(5)
					try:
						alert = driver.switch_to_alert()
						ferror.write(new_coupon[0] + email + " " + alert.text + "\n")
						alert.accept()
						print
					except:
						pass
				except Exception as e:
					ferror.write(new_coupon[0] + email + " " + e + "\n")
		
		driver.close()
		ferror.close()
		fa.close()

if __name__ == "__main__":
	main()
	sys.exit(0)
