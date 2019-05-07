from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic = {}
    
    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    from translate import Translator
    translator = Translator(to_lang="ko")
    translation = translator.translate(text)

    import requests
 
    # 네이버 파파고 api이용하기
    url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=en&text="
    
    request_url = "https://openapi.naver.com/v1/papago/n2mt"
    headers= {"X-Naver-Client-Id": "E3Qm4KfmUlFJjFRsCuTf", "X-Naver-Client-Secret":"Qbj4Gdlgi2"}
    params = {"source": "ko", "target": "en", "text": text}
    response = requests.post(request_url, headers=headers, data=params)
    # print(response.text)
    result = response.json()
    
    return render(request, 'result.html', {'full': text, 'lenwords':len(words), 'dictionary': word_dic.items(), 'trans_to_ko': translation, 'trans_to_en': result['message']['result']['translatedText']})


def saved(request):
    filename = request.GET['filename']
    directory = request.GET['dir']
    f = open(f'{directory}\\{filename}.txt', 'w+t')
    f.write("") # 이전 result 페이지에서 썼던 text 변수를 그대로 사용하는 방법?
    f.close()
    return render(request, 'saved.html')