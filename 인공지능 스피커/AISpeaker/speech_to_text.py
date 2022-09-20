# STT(Speech To Text)

import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print('지금부터 말해주세요')
    audio = r.listen(source) # 마이크로부터 음성 듣기

# 파일로부터 음성 불러오기(wav, aiff/aiff-c, flac 가능, mp3는 불가)
r = sr.Recognizer()
with sr.AudioFile('sample.wav') as source:
    audio = r.record(source) # 파일로부터 음성 불러오기

try:
    # 구글 API로 인식(하루 50회로 제한된다고함)
    # 영어 문장
    # text = r.recognize_google(audio, language='en-US')
    # print(text)

    # 한글 문장
    text = r.recognize_google(audio, language='ko-KR')
    print(text)

except sr.UnknownValueError:
    print('인식 실패') # 음성인식 실패한 경우
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API key오류, 네트워크 단절 등