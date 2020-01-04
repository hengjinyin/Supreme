from splinter.browser import Browser
from time import sleep
import datetime
from enum import Enum
import logging
import logging.handlers
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from collections import Counter
import sys


class supreme(object):
    POSTFIX_1 = '?alt=0' 
    POSTFIX_2 = '?alt=1'
    CART_URL = 'https://www.supremenewyork.com/shop/cart'
    CHECKOUT_URL = 'https://www.supremenewyork.com/checkout'
    FIRST_NEW_URL = 'https://www.supremenewyork.com/shop/new'
    FIRST_JACKETS_URL = 'https://www.supremenewyork.com/shop/jackets/pduxhq4jr'
    FIRST_PANTS_URL = 'https://www.supremenewyork.com/shop/pants/quxsve20d'
    FIRST_SHIRTS_URL = 'https://www.supremenewyork.com/shop/all/shirts'
    FIRST_TOPSWEATERS_URL = 'https://www.supremenewyork.com/shop/tops-sweaters/jrgseoiq3'
    FIRST_SWEATSHIRTS_URL = 'https://www.supremenewyork.com/shop/sweatshirts/pq0sz7j2h'
    FIRST_BAGS_URL = 'https://www.supremenewyork.com/shop/bags/uvd6m9jo1'
    FIRST_TIME = True
    TAG_A_MARGIN = 15
    TAG_DIV_MARGIN = 4

    #OldFashion
    OldFashion = {
        'https://www.supremenewyork.com/shop/jackets/pduxhq4jr/kc09nw15t' : 'oldFashion',
        'https://www.supremenewyork.com/shop/accessories/yj95dw3zl/eq35gubw7' : 'oldFashion',
        'http://www.supremenewyork.com/shop/accessories/o3hryesf1/j6uy0pn2a' : 'oldFashion',
        'https://www.supremenewyork.com/shop/hats/at03w6qhd/tcjxzynvi' : 'oldFashion',
        'https://www.supremenewyork.com/shop/hats/at03w6qhd/j3kj5zrfy' : 'oldFashion',
        'http://www.supremenewyork.com/shop/accessories/mrnm015j2/a9qvi31j2' : 'oldFashion',
        'http://www.supremenewyork.com/shop/accessories/mrnm015j2/x6cz3u7vt' : 'oldFashion'
    }

    class SupremeType(Enum):
        Jackets = 'jackets'
        Tshirts = 't-shirts'
        TopsSweaters = 'tops-sweaters'
        SweatShirts = 'sweatshirts'
        Pants = 'pants'
        Hats = 'hats'
        Bag = 'bag'
        Accessories = 'accessories'
        Shoes = 'shoes'
        Skate = 'skate'

    # Grey color is your like category, make sure whatever you like has a "#" in front of it
    DislikeCategories = {
        #SupremeType.Jackets : 'dislike',
        #SupremeType.Tshirts : 'dislike',
        #SupremeType.TopsSweaters : 'dislike',
        #SupremeType.SweatShirts : 'dislike',
        #SupremeType.Pants : 'dislike',
        #SupremeType.Hats: 'dislike',
        #SupremeType.Bag : 'dislike',
        #SupremeType.Accessories : 'dislike',
        #SupremeType.Shoes : 'dislike',
        #SupremeType.Skate : 'dislike'
    }

    BookedItem = {}

    Browsers = list()

    #You can update sleep time
    sleepTime = 0.1

    # count_div = TAG_DIV_MARGIN - 1
    # count_inner_article = 0

    #Fill in your size "Small", "Medium", "Large", "XLarge"
    FIRSTSIZE = "Small"
    SECONDSIZE = "Medium"
    THIRDSIZE = "Large"



    # browser = Browser('chrome')

    def log(self,msg):
        logfile = open("YourOwnLogDirectory/output.txt", "a+")
        logfile.write(msg + " @ " + datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S") + "\n")
        logfile.close()

    def start(self):
        # self.browser.visit(self.FIRST_NEW_URL)

        print "Start log.........."
        self.log("///////////////////////////////////////////////////" + "\n")
        self.log("//////////////////new cycle begin//////////////////" + "\n")
        self.log("///////////////////////////////////////////////////" + "\n")
        self.log('Start log..........')

        time = 1

        stillEmpty = True
        pleaseContinue = True
        try:
            self.log("Stop shopping whenever you want by using keyboard")
            print 'Stop shopping whenever you want by using keyboard'
            while (stillEmpty or True) and pleaseContinue:
                browser = Browser('chrome')
                self.Browsers.append(browser)
                browser.visit(self.FIRST_NEW_URL)
                try:
                    for num in range(300):
                        for br in self.Browsers:
                            if br.url == self.CHECKOUT_URL:
                                self.fillCreditCardInfo(br)
                                break
                        print num
                        self.log("This is NO. " + str(num) + " item")
                        articleElement = browser.find_by_tag('article')[num]
                        hrefElement = articleElement.find_by_tag('a')['href']
                        print hrefElement
                        self.log(str(hrefElement))
                        soldOutFound = articleElement.find_by_tag('div').last.has_class("sold_out_tag")
                        print soldOutFound
                        self.log('soldOutFound' + str(hrefElement))

                        itemType = hrefElement.split('/')[4]
                        if self.DislikeCategories.get(itemType) == 'dislike':
                            print 'I do not want this Category : ' + hrefElement
                            self.log('I do not want this Category : ' + hrefElement)
                            continue
                        elif self.OldFashion.get(hrefElement) == 'oldFashion':
                            print 'I do not want old fashion : ' + hrefElement
                            self.log('I do not want old fashion : ' + hrefElement)
                            continue
                        elif self.BookedItem.get(hrefElement) is not None:
                            print 'This item has been booked before : ' + hrefElement
                            self.log('This item has been booked before : ' + hrefElement)
                            continue

                        if soldOutFound:
                            print "This item has been sold out : " + hrefElement
                            self.log("This item has been sold out : " + hrefElement)
                            continue

                        self.log("click article begin for : " + hrefElement)
                        browser.find_by_tag('article')[num].click()

                        self.log("click article finish for : " + hrefElement)
                        print "begin sleep 0.5s after clicking article for : " + hrefElement
                        self.log("begin sleep 0.5s after clicking article for : " + hrefElement)
                        sleep(self.sleepTime)
                        print "finish sleep 0.5s after clicking article for : " + hrefElement
                        self.log("finish sleep 0.5s after clicking article for : " + hrefElement)
                        self.log("Add to Cart begin for : " + hrefElement)
                        self.AddToCart(browser, itemType)
                        self.log("Add to Cart finished for : " + hrefElement)
                        self.log("browser back begin for : " + hrefElement)
                        browser.back()
                        self.log("browser back finished for : " + hrefElement)
                except Exception as inst:
                    print type(inst)  # the exception instance
                    self.log(str(type(inst)))
                    print inst.args  # arguments stored in .args
                    self.log(str(inst.args))
                    print inst  # __str__ allows args to be printed directly
                    self.log(str(inst))
                    browser.visit(self.CART_URL)
                    test1 = browser.find_by_tag('p').first
                    test2 = test1.find_by_id('items-count')
                    if test2.value == '0 items':
                        pleaseContinue = False
                        print "pleaseContinue is False"
                        self.log("pleaseContinue is False")
                print 'moving on'
                self.log('moving on')
        except Exception as inst:
            print "2nd Exception"
            self.log("2nd Exception")
            print type(inst)  # the exception instance
            self.log(str(type(inst)))
            print inst.args  # arguments stored in .args
            self.log(str(inst.args))
            print inst  # __str__ allows args to be printed directly
            self.log(str(inst))

        # self.browser.visit(self.CART_URL)
        while True:
            # try:
            #     self.log('Please type in 1 to transfer to checkout page:')
            #     response = int(raw_input('Please type in 1 to transfer to checkout page:'))
            # except ValueError:
            #     print "Not a number"
            #     self.log("Not a number")
            # if response == 1:
            #     for br in self.Browsers:
            #         self.fillCreditCardInfo(br)

            for br in self.Browsers:
                if br.url == self.CHECKOUT_URL:
                    self.fillCreditCardInfo(br)

    def fillCreditCardInfo(self,browser):
        orderName = browser.find_by_name('order[billing_name]')
        if orderName != None and orderName.value == "XXX X":
            return
        self.log("Start Fill In Credit Card Info")
        browser.visit(self.CHECKOUT_URL)
        browser.fill('order[billing_name]', "XXX X")
        self.log('order[billing_name] : '+"XXX X")
        browser.fill('order[email]', "XXX@hotmail.com")
        self.log('order[email] : ' + "XXX@hotmail.com")
        browser.fill('order[tel]', "1234567890")
        self.log('order[tel] : ' + "1234567890")
        browser.fill('order[billing_address]', "1234 billing_address Dr")
        self.log('order[billing_address] : ' + "1234 billing_address Dr")
        browser.fill('order[billing_zip]', "44444")
        self.log('order[billing_zip] : ' + "44444")
        browser.fill('order[billing_city]', "City")
        self.log('order[billing_city] : ' + "City")
        browser.find_option_by_text('TX').first.click()
        self.log('click : ' + "TX")
        browser.find_option_by_text('USA').first.click()
        self.log('click : ' + "USA")
        browser.fill('credit_card[nlb]', "1111 1111 1111 1111")
        self.log('credit_card[nlb] : ' + "1111 1111 1111 1111")
        browser.find_option_by_text('00').first.click()
        self.log('expire month : ' + "00")
        browser.find_option_by_text('2018').first.click()
        self.log('expire year : ' + "2018")
        browser.fill('credit_card[rvv]', "111")
        self.log('security num : ' + "111")


    def AddToCart(self,browser, itemType):
        if browser.is_element_present_by_value('add to cart'):
            needsize = False

            if itemType == self.SupremeType.Jackets or itemType == self.SupremeType.Tshirts or itemType == self.SupremeType.SweatShirts or itemType == self.SupremeType.TopsSweaters:
                needsize = True
            if needsize:
                if not browser.find_option_by_text(self.FIRSTSIZE).is_empty():
                    print "First Size Found"
                    self.log("First Size Found")
                    browser.find_option_by_text(self.FIRSTSIZE).first.click()
                # elif not browser.find_option_by_text(self.SECONDSIZE).is_empty():
                #     print "Second Size Found"
                #     self.log("Second Size Found")
                #     browser.find_option_by_text(self.SECONDSIZE).first.click()
                # elif not browser.find_option_by_text(self.THIRDSIZE).is_empty():
                #     print "Third Size Found"
                #     self.log("Third Size Found")
                #     browser.find_option_by_text(self.THIRDSIZE).first.click()
            browser.find_by_name('commit').first.click()
            self.BookedItem[browser.url] = 1
            print "Yes, " + browser.url + " has added to the cart"
            self.log("Yes, " + browser.url + " has added to the cart")
            stillEmpty = False
        else:
            print "No, " + browser.url + " sold out, and keep finding next one"
            self.log("No, " + browser.url + " sold out, and keep finding next one")


if __name__ == '__main__':
    supreme = supreme()
    supreme.start()
