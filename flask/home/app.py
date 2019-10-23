from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# @app.route('/fake_naver')
# def fake_naver():
#     return render_template('fake_naver.html') 



@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')


@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/recieve')
def recieve():
    # request.args #=> {'username' : 'nwith, 'message':'안녕}

    username = request.args.get('username')
    message = request.args.get('message')

    # ... 


    return render_template('recieve.html', username = username, message = message)


@app.route('/check_lotto')

def check_lotto():
    return render_template('check_lotto.html')


@app.route('/result_lotto')

def result_lotto():
    n = request.args.get('round_lotto')
    # print(list(map(int, request.args.get('numbers').split))) #=> '1 2 3 4 5 6'
    numbers = [int(number) for number in request.args.get('numbers').split()]


    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'

    response = requests.get(url)
    # response.text #=> string
    lotto = response.json() #=> dictionary

    # winner = []
    # for i in range(1,7):
    #  winner.append(lotto[f'drwtNo{i}'])

    winner = [lotto[f'drwtNo{i}'] for i in range(1,7)] #comprehenshon 을 사용하는 것이 더 좋다

    bonus = lotto['bnusNo']

    matched = list(set(numbers) & set(winner)) #=> 중복되는 숫자들

    if len(matched) == 6:
        result ='1등입니다!!!'
    elif len(matched) == 5:
        if bonus in numbers:
            result ='2등입니다.!!'
        else:
            result = '3등입니다!!'
    elif len(matched) == 4:
        result = '4등입니다.!!'
    elif len(matched) ==3:
        result = '5등입니다.!!'
    else :
        result = '꽝입니다...'




    return render_template('result_lotto.html', winner = winner, bonus = bonus, n=n , numbers = numbers, result = result)



# def result_lotto2():

#     n = request.args.get('round_lotto')


#     url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'

#     response = requests.get(url)
#     # response.text #=> string
#     lotto = response.json() #=> dictionary

#     # winner = []
#     # for i in range(1,7):
#     #  winner.append(lotto[f'drwtNo{i}'])

#     winner = [lotto[f'drwtNo{i}'] for i in range(1,7)] #comprehenshon 을 사용하는 것이 더 좋다

#     bonus = lotto['bnusNo']

#     numbers = winner.extend(bonus)
    
#     bing = [f'lotto_num{i}' for i in range(1,7)]


#     lotto_num = request.args.get(bing)
        
#     return render_template('result_lotto.html', bing = bing )







if __name__ == '__main__':
    app.run(debug =True)

