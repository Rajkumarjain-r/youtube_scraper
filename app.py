from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import oss
import requests
import pandas as pd
import re
import pymongo
import logging
logging.basicConfig(filename="PW_scrapper.log" , level=logging.INFO)

app = Flask(__name__)

@app.route("/", methods = ['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route("/pw-youtube", methods = ['GET','POST'])
@cross_origin(

)
def analyse():
    if request.method == 'POST':
        url = 'https://www.youtube.com/@PW-Foundation/videos'
        DRIVER_PATH = r'chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
        driver.get(url)
        time.sleep(10)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        list_video_url = soup.find_all('a', class_="yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media")
        list_video_url_5 = ["https://www.youtube.com/" + list_video_url[i]["href"] for i in range(5)]

        list_video_title = soup.find_all('yt-formatted-string', class_="style-scope ytd-rich-grid-media")
        list_video_title_5 = [list_video_title[i].text for i in list(range(0, 10, 2))]

        def extract_numbers_and_spaces(text):
            pattern = r"[0-9a-zA-Z\s]+"
            matches = re.findall(pattern, text)
            extracted_text = ''.join(matches)
            return extracted_text

        list_video_title_5 = list_video_title_5 = list(map(lambda x: extract_numbers_and_spaces(x), list_video_title_5))

        list_video_views = soup.find_all('span', class_="inline-metadata-item style-scope ytd-video-meta-block")
        list_video_views_5 = [list_video_views[i].text for i in list(range(0, 10, 2))]

        list_video_timing_5 = [list_video_views[i].text for i in list(range(1, 11, 2))]

        list_video_url_thumbnail = re.findall(r"https://i.ytimg.com/vi/[A-Za-z0-9_-]{11}/[A-Za-z0-9_]{9}.jpg",
                                              html_content)
        list_video_url_thumbnail = list_video_url_thumbnail[2:]
        list_video_url_thumbnail_5 = [list_video_url_thumbnail[i] for i in range(0, 20, 4)]

        result_data = pd.DataFrame(list(
            zip(list_video_title_5, list_video_url_5, list_video_views_5, list_video_timing_5,
                list_video_url_thumbnail_5)))
        result_data.rename(
            columns={0: "Video Title", 1: "Youtube url", 2: "No of views", 3: "Posted on", 4: "Thumbnail"},
            inplace=True)

        result_data_list = result_data.to_dict('records')

        def insert_mongodb():
            client = pymongo.MongoClient("mongodb+srv://Raj12345:12345@cluster0.fbexpxf.mongodb.net/")
            db = client["PW_analysis"]
            collection = db["PW_analysis_results"]
            collection.insert_many(result_data_list)

        try:
            insert_mongodb()
        except Exception as e:
            logging.info(e)

        return render_template('result.html', results=result_data_list[0:(len(result_data_list) - 1)])

if __name__=="__main__":
    app.run(host="0.0.0.0")
