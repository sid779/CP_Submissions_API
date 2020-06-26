from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

app = Flask(__name__)
api = Api(app)
'''
@app.route('/')
def hello_world():
    return 'KIRA IS THE GOD OF THE NEW WORLD'

@app.route('/<string:username>')
def get_submisssions(username):
    result = requests.get('https://www.stopstalk.com/user/profile/'+username)
    print(result.status_code)
    src = result.content
    # print (src)


    if(result.status_code==200):
        url = 'https://www.stopstalk.com/user/profile/'+username
        driver = webdriver.Firefox()
        driver.get(url)
        delay = 5  # seconds

        soup = BeautifulSoup(driver.page_source, 'lxml')
        #print (soup.prettify())
        tables = soup.body.main.div.div.div.div.find('table')
        # table = soup.findAll('div')
        #print(tables)
        h4tag = soup.body.main.div.div.div.div.strong.b
        print(h4tag)
        print(h4tag.string)

        name = soup.body.main.div.div.div.div.strong.b.string
        codechef = soup.body.main.div.div.div.div.find(id="codechef-solved-count").string
        codeforces = soup.body.main.div.div.div.div.find(id="codeforces-solved-count").string
        hackerrank = soup.body.main.div.div.div.div.find(id="hackerrank-solved-count").string
        hackerearth = soup.body.main.div.div.div.div.find(id="hackerearth-solved-count").string
        spoj = soup.body.main.div.div.div.div.find(id="spoj-solved-count").string
        total = soup.body.main.div.div.div.div.find(id="solved-problems").string

        print('Name: ' + name)
        print('Codechef: ' + codechef)
        print('CodeForces: ' + codeforces)
        print('Hackerrank: ' + hackerrank)
        print('Hackerearth: ' + hackerearth)
        print('Spoj: ' + spoj)
        print ('Total solved: ' + total)

        return jsonify({
            'Name' : name,
            'Codechef ': codechef,
            'CodeForces': codeforces,
            'Hackerrank': hackerrank,
            'Hackerearth': hackerearth,
            'Spoj': spoj,
            'Total': total,
        }), 200

    return 'USER NOT FOUND',404
'''

class Hello_world(Resource):
    def get(self):
        return 'KIRA IS THE GOD OF THE NEW WORLD'
    def post(self):
        return 'LOST IN REALM',404

class Get_Submissions(Resource):
    def get(self, username):
        result = requests.get('https://www.stopstalk.com/user/profile/' + username)
        print(result.status_code)
        src = result.content
        # print (src)

        if (result.status_code == 200):
            url = 'https://www.stopstalk.com/user/profile/' + username
            driver = webdriver.Firefox()
            driver.get(url)
            delay = 5  # seconds

            soup = BeautifulSoup(driver.page_source, 'lxml')
            # print (soup.prettify())
            tables = soup.body.main.div.div.div.div.find('table')
            # table = soup.findAll('div')
            # print(tables)
            h4tag = soup.body.main.div.div.div.div.strong.b
            print(h4tag)
            print(h4tag.string)

            name = soup.body.main.div.div.div.div.strong.b.string
            codechef = soup.body.main.div.div.div.div.find(id="codechef-solved-count").string
            codeforces = soup.body.main.div.div.div.div.find(id="codeforces-solved-count").string
            hackerrank = soup.body.main.div.div.div.div.find(id="hackerrank-solved-count").string
            hackerearth = soup.body.main.div.div.div.div.find(id="hackerearth-solved-count").string
            spoj = soup.body.main.div.div.div.div.find(id="spoj-solved-count").string
            total = soup.body.main.div.div.div.div.find(id="solved-problems").string

            print('Name: ' + name)
            print('Codechef: ' + codechef)
            print('CodeForces: ' + codeforces)
            print('Hackerrank: ' + hackerrank)
            print('Hackerearth: ' + hackerearth)
            print('Spoj: ' + spoj)
            print('Total solved: ' + total)

            return {
                'Name': name,
                'Codechef': codechef,
                'CodeForces': codeforces,
                'Hackerrank': hackerrank,
                'Hackerearth': hackerearth,
                'Spoj': spoj,
                'Total': total,
            }, 200

        return {'About':'USER NOT FOUND'}, 404
    def post(self,username):
        return 'LOST IN REALM',404


api.add_resource(Hello_world,'/')
api.add_resource(Get_Submissions,'/<string:username>')


if __name__ == '__main__':
    app.run(debug=True)


'''
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(driver.find_elements_by_xpath('..//elementid')))
        print('Page is ready!')
    except TimeoutException:
        print('Couldn\'t load page')

'''