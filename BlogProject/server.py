from flask import Flask, request
import blog_main

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world!"

# GET 방식
@app.route('/blog-ranking')
def blog_ranking():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    # url에 전달받은 파라미터
    keyword = parameter_dict['keyword']
    url = parameter_dict['url']
    print("요청 :")
    print("  ", keyword)
    print("  ", url)

    # 제목, 날짜, 랭크 결과
    dict = blog_main.get_blog_rank_n_info(keyword, url)
    print("결과 :")
    print("  ",dict)

    return str(dict)


@app.route('/parm')
def root():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    parameters = ''
    for key in parameter_dict.keys():
        parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
    return parameters



if __name__ == '__main__':
    app.run()
    #print(blog_main.get_blog_rank_n_info('한의원', 'https://blog.naver.com/jc1103/223189397649'))