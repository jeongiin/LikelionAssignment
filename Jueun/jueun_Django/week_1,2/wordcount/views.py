from django.shortcuts import render

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
            #increase
            word_dic[word]+=1
        else: 
            #add to dictionary
            word_dic[word]=1
    return render(request, 'result.html',{'full': text,'total': len(words), 'dictionary': word_dic.items })