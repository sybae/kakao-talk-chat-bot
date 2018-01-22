from flask import request, jsonify
from flask_restful import Resource
from app import dbtalk, twitter

# It is just HelloWorld class. It's not used.
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Kakao API 'Keyboard'
class Keyboard(Resource):
    def get(self):
        dataSend = {
            'type': 'text'
            #'type': 'buttons',
            #'buttons': ['start', 'help']
        }
        return jsonify(dataSend)

# Kakao API 'Message'
class Message(Resource):
    def post(self):
        dataReceive = request.get_json()
        content = dataReceive['content']

        if content.lower() == u'help' or content == u'도움':
            dataSend = {
                'message': {
                    'text': '밤토리봇 v0.3.3\n\n'
                            + '참으로 쓸데없는 문장이 아무렇게나 튀어나옵니다. 인물에 대해서는 최대한 사실에 입각한 내용을 등록하는 것이 최초 서비스의 사상이었지만, 서비스 오픈 이후 3시간만에 폐기되었습니다.\n\n' \
                            + '[bth, 생일] - 멤버전체생일\n' \
                            + '[cnt, 전체] - 누적된 아무말 개수\n' \
                            + '[/add ?] - 아무말 등록\n' \
                            + '[nfl, 넷플] - 넷플릭스 업데이트 내역\n' \
                            + '[ver] - Show Version History\n' \
                            + '\n그 외의 입력에 대해서는 모두 아무말이 시전됩니다. 글을 등록해주실 때에는 욕설 등을 피해주시기 바랍니다.'
                }
            }
        elif content.lower() == u'bth' or content == u'생일':
            dataSend = {
                'message': {
                    'text': 'PUT_SOME_YOUR_CODES'
                }
            }
        elif content.lower() == u'cnt' or content == u'전체':
            accCnt = dbtalk.getAccCount()
            rsltMsg = '누적된 아무말은 ' + format(accCnt, ',') + ' 개 입니다.'
            dataSend = {
                'message': {
                    'text': rsltMsg
                }
            }
        elif content.lower() == u'nfl' or content == u'넷플':
            dataSend = {
                'message': {
                    'text': twitter.getNetflixUpdateFullText()
                }
            }
        elif content.lower() == u'ver':
            dataSend = {
                'message': {
                    'text': "v0.3.3 What's new on Netflix.\n" \
                            + 'v0.2.2 Improved DB connection.\n' \
                            + 'v0.1.9 Release snippety service.\n' \
                            + '\n' \
                            + '개발자 편의를 위해 넷플릭스 업데이트 내역 기능을 추가합니다.\n' \
                            + '버그리포트 및 아이디어는 갠톡 또는 메일로 부탁드립니다.'
                }
            }
        elif u'/add ' in content:
            contentWork = content.replace('/add ', '').strip()
            rsltAdd = dbtalk.addMention(contentWork)
            if rsltAdd == True:
                rsltMsg = 'Done...'
            else:
                rsltMsg = 'Fail...'
            dataSend = {
                'message': {
                    'text': rsltMsg
                }
            }
        elif u'/getid ' in content:
            contentWork = content.replace('/getid ', '').strip()
            mtid = dbtalk.getId(contentWork)
            dataSend = {
                'message': {
                    'text': 'id = ' + str(mtid)
                }
            }
        elif u'/delmention ' in content:
            contentWork = content.replace('/delmention ', '').strip()
            rsltDel = dbtalk.delMention(contentWork)
            rsltMsg = 'Del Done..' if rsltDel == True else 'Del Fail..'
            dataSend = {
                'message': {
                    'text': rsltMsg
                }
            }
        else:
            ranTalk = dbtalk.getOneRandom()
            dataSend = {
                'message': {
                    'text': ranTalk
                }
            }

        return jsonify(dataSend)

# Setting API URL
def addResouceDef(api):
    api.add_resource(HelloWorld, '/')
    api.add_resource(Keyboard, '/keyboard')
    api.add_resource(Message, '/message')