from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.


def tregister(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        phoneno=request.POST['Number']
        Qualification=request.POST['Qualification']
        Department=request.POST['Department']
        Password=request.POST['Password']
        conPassword=request.POST.get("conPassword")
        if Password==conPassword:
            if teacher_reg.objects.filter(Name=name).exists():
                messages.info(request,'Username Already Exists')
            else: 
              userdata=teacher_reg(Name=name,email=email,Number=phoneno,
            Qualification=Qualification,Department=Department,Password=Password)
              userdata.save()
              return redirect("tmssg")          
        else:  
             messages.info(request,'password not match')

    return render(request,'teacher/tregister.html')



def tlog(request):
    if request.method =="GET":
        return render(request,"teacher/tlogin.html")
    else:
        email=request.POST.get('email') 
        Password=request.POST.get('password')
        error_message = None
        farmer_gen = teacher_reg.objects.get(email=email)
        data={'farmer_gen':farmer_gen}
        print(data)
            
        if farmer_gen and farmer_gen.status==1 :
            if(Password==farmer_gen.Password):
                flag=1

            if flag :
                request.session['id']=farmer_gen.id
                request.session['email']=farmer_gen.email
                return render(request,"teacher/tpage.html",data)
            else:
                error_message = 'Email or Password invalid !!'
                return render(request,"teacher/tlogin.html",{'error':error_message})
        else:
            if farmer_gen.status==0:
                    error_message="Admin permission required"
            else:
                error_message = 'Email or Password invalid !!'
    return render(request,'teacher/tlogin.html',{'error':error_message})

# def tlog(request):
#     if request.method=="POST":
#         try:
#             email=request.POST.get('email') 
#             Password=request.POST.get('password')
#             log=teacher_reg.objects.get(email=email,Password=Password)
#             request.session['email']=log.email
#             request.session['id']=log.id
#             return redirect('tpage')
#         except teacher_reg.DoesNotExist as e :
#             messages.info(request,'Invalid User')
#     return render(request,'teacher/tlogin.html')
def tmssg(request):
    return render(request,'teacher/tmssg.html')

def tpage(request):
    return render(request,'teacher/tpage.html')

def tprofile(request):
    hid=request.session['id']
    prof=teacher_reg.objects.get(id=hid)
    return render(request,'teacher/tprofile.html', {'pro':prof})

def teditprofile(request,id):
    edit=teacher_reg.objects.get(id=id)
    if request.method=="POST":
        
        # if len(request.FILES)!=0:
   
        #     edit.Image=request.FILES.get('img')

        edit.Name=request.POST.get("Name")
        edit.Number=request.POST.get("Number")
        edit.Qualification=request.POST.get("Qualification")
        edit.email=request.POST.get("Email")
        edit.Department=request.POST.get("Department")        
        edit.Password=request.POST.get("Password")
        edit.save()
        
        return redirect("tprofile")
    return render(request,'teacher/teditprofile.html',{'pro':edit})

def question(request):
    if request.method=="POST":
        question=request.POST['question']
        answer=request.POST['answer']
        
        tid=request.POST['tid']
        
        userdata=Questions(question=question,answer=answer,teacherid_id=tid)
        userdata.save()
        return redirect("tpage") 
         
       

    return render(request,'teacher/question.html')
def view_ques(request):
    tid=request.session['id']
    data=Questions.objects.filter(teacherid=tid)
    return render(request,'teacher/view_qpaper.html',{'data':data})

def Evaluation(request,id):
    Question=Questions.objects.get(id=id)  
    import tensorflow as tf
    from tensorflow.keras.layers import Dense, Input
    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras.models import Model
    from tensorflow.keras.callbacks import ModelCheckpoint
    from sklearn.model_selection import train_test_split
    from keras.preprocessing.text import Tokenizer
    from tensorflow.keras.layers import LSTM, Dense,Flatten,Conv2D,Conv1D,GlobalMaxPooling1D,GlobalMaxPool1D,SimpleRNN
    from keras.optimizers import Adam
    import numpy as np  
    import pandas as pd 
    import keras.backend as k
    # from keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    from tensorflow.keras.layers import Input, LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional,GRU
    from tensorflow.keras.models import Model,Sequential
    from tensorflow.keras.callbacks import EarlyStopping
    from sklearn.preprocessing import OneHotEncoder
    from keras.utils import to_categorical
    from keras.utils.vis_utils import plot_model
    import matplotlib.pyplot as plt
    
    import re
    def remove_url(s):
        return re.sub(r'http\S+', '', s)    
    def remove_tag(s):
        return re.sub(r'<.*?>', ' ', s) 
    def lower_words(s):
        return s.lower()  
    def decontracted(phrase):
        """decontracted takes text and convert contractions into natural form.
            ref: https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python/47091490#47091490"""

        # specific
        phrase = re.sub(r"won\'t", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)
        phrase = re.sub(r"won\’t", "will not", phrase)
        phrase = re.sub(r"can\’t", "can not", phrase)

        # general
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)

        phrase = re.sub(r"n\’t", " not", phrase)
        phrase = re.sub(r"\’re", " are", phrase)
        phrase = re.sub(r"\’s", " is", phrase)
        phrase = re.sub(r"\’d", " would", phrase)
        phrase = re.sub(r"\’ll", " will", phrase)
        phrase = re.sub(r"\’t", " not", phrase)
        phrase = re.sub(r"\’ve", " have", phrase)
        phrase = re.sub(r"\’m", " am", phrase)

        return phrase
    def remove_words_with_nums(s):
        return re.sub(r"\S*\d\S*", "", s)

        

    def remove_special_character(s):
        return re.sub('[^A-Za-z0-9]+', ' ', s)
    stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren'])
    def remove_stopword(s):
        res = ' '.join([word for word in s.split(' ') if word not in stopwords])
        return res
    import nltk
    # train_df=pd.read_csv('Data/train.csv',encoding='cp1252', error_bad_lines=False)

    from nltk.corpus import brown
    from nltk.stem.wordnet import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    def lemmatization(s):
        res = ' '.join([lemmatizer.lemmatize(word) for word in s.split(' ')])
        return res
    def preprocess_text(text):
        text = remove_url(text)
        text = remove_tag(text)
        text = lower_words(text)
        text = decontracted(text)
        text = remove_words_with_nums(text)
        text = remove_special_character(text)
        text = remove_stopword(text)
        text = lemmatization(text)
        return text
    import pickle
    filename = 'rnntokenizer.sav'
    # loaded_model = pickle.load(open(filename, 'rb')) 
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow import keras
    from keras.preprocessing.text import Tokenizer
    import tensorflow_hub as hub
    import os

    os.environ["TFHUB_CACHE_DIR"] = "/tmp/model"
    model = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder-large/5?tf-hub-format=compressed")
    
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    # answer1="""A very considerable amount of light!  Increasing that distance from the end of the lens to the sensor can cut your light several stops.  Combined with the fact that you'll usually shoot stopped down - expect to need to increase your ISO considerably.

    #     """
    answer1=str(Question.ans)
    answer_embedding=preprocess_text(answer1)
    answer_embeddings = model([answer_embedding])
    # query = """I just got extension tubes, so here the skinny.


    #     ...what am I losing when using tubes...?


    #     A very considerable amount of light!  Increasing that distance from the end of the lens to the sensor can cut your light several stops.  Combined with the fact that you'll usually shoot stopped down - expect to need to increase your ISO considerably.

    #     The fact the macro are usually considered very very sharp, although I believe that 70-200mm 2.8 is supposed to be quite sharp.

    #     The ultra low distortion typical of many macros.

    #     I wouldnt worry too much about the bokeh since the DOF will still be quite limited.

    #     Coupled on my 50mm, a full 60mm'ish extension tube results in a DOF of about a couple inches in front of the lens.  On my 70-300, its probably around 2-3 feet in front of the lens to about a foot in front of the lens.

    #     """
    query=str(Question.answer)
    cleaned_query = preprocess_text(query)
    # def query_match(query):
    #     query_embedding = model([query])
    #     sim = cosine_similarity(answer_embeddings, query_embedding)
    #     # sim_scores = [sim[i][0] for i in range(sim.shape[0])]
    #     return np.argmax(sim)
    query_embedding = model([cleaned_query])
    sim = cosine_similarity(answer_embeddings, query_embedding)
    mark=sim*100
    m=int(mark)
    if m < 40:
        Questions.objects.filter(id=id).update(grade="F")
    elif m>40 and m<51:
        Questions.objects.filter(id=id).update(grade="E")
    elif m>50 and m<61:
        Questions.objects.filter(id=id).update(grade="D")
    elif m>60 and m<71:
        Questions.objects.filter(id=id).update(grade="C")
    elif m>70 and m<81:
        Questions.objects.filter(id=id).update(grade="B")
    elif m>80 and m<91:
        Questions.objects.filter(id=id).update(grade="A")
    elif m>90 and m<101:
        Questions.objects.filter(id=id).update(grade="A+")
    else:
        Questions.objects.filter(id=id).update(grade="Pending")


    




    Questions.objects.filter(id=id).update(mark=mark)
    
    # query_idx,sim = query_match(query)
    return redirect("vques")
    