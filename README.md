# kakao-talk-chat-bot
> Python Flask RESTful API 통한 카카오톡 플러스친구 기반의 챗봇

## 시작
카카오톡 단체 채팅방 중 애착이 있는 한 곳에서 사용하기 위하여 제작되었습니다. 카카오톡에서 텍스트 요청을 받아 관련 처리를 하여 대답합니다. 시작은 그러했지만 범용성을 높인다면 더 많은 유저에게 서비스할 수 있습니다. 이와 관련하여 클리앙, 트위터 등의 크롤링 기능이 개발되었습니다. 2017년 말에 개발되어 BitBucket 내에서 관리하다가 GitHub 에도 등재합니다. 현재도 이 챗봇은 지속적으로 서비스되고 있어 카카오톡 내에서 이야기를 주고 받고 있습니다.

## 환경
이 프로그램을 분해해보면 아래처럼 나열됩니다.
 - Python 3
 - Flask RESTful
 - SQLite3
 - Tweepy
 - Beautiful Soup
 - PythonAnywhere (Talk with Kakao API)

[카카오톡 플러스친구 API](https://github.com/plusfriend/auto_reply) 통해서 구체적인 사항을 확인할 수 있습니다.

## 테스트
모바일 디바이스에서 접근하기 전에 curl 테스트를 진행합니다. Restful API 테스트를 위해서는 `-H` 헤더 옵션을 json 세팅합니다.
```sh
$ curl -i -v -X POST http://127.0.0.1:5000/message -H "Content-Type:application/json" -d '{"content":"help"}'
```

## 자아성찰
이미지 및 링크를 포함한 텍스트 응답을 개발하였습니다. 그런데 카카오톡에서 정말 아름답지 않게 보여주었습니다. 추가로 시스템에서 바로 Push 통해 알려주는 부분을 구현하려고 시도하였습니다. 하지만 카카오에서는 반드시 디바이스를 통한 처리만을 허용하고 있었습니다. 이는 Apple, Google 푸쉬를 통해야 하며 결국 네이티브 어플리케이션을 제작해야만 하는 필요가 있다는 뜻 입니다. 이 부분이 아쉽지만 정책을 존중합니다. 앞으로 더 나아가 언어학습을 적용하는 부분을 고려해보고 있습니다.