import tensorflow as tf           
import numpy as np
raw_corpus=''' I am very excited about the possibility of joining your organization as a Machine Learning Engineer.
Your Tradition of putting value for Research  and progressive product development is inspirational to developing professional like myself.I am a self-motivated and highly enthusiastic personnel who believes in hard work and dedication. I completed my bachelors degree in electronics and communication engineering form PulchowkCampusIOE.I am a good learner and highly interested in the field of AI.
I began studying Machine learning 2 years ago. I have proficient knowledge in different machine learning Algorithms and Deep learning techniques like CNN RNN.I have done projects during my university education in the field of Computer Vision and currently i am learning about Natural language processing.
I am not a experienced one but i can build myself very fast through my knowledge and skills.Working in the field of machine learning and providing to community has always been my Dream.My academic qualification and Projects during my university education are listed in the CV which i have attached along with this mail.
Looking forward to hear from you'''

raw_corpus=raw_corpus.lower()
words=[]
for word in raw_corpus.split():
    if word!='.':
        words.append(word)
words=set(words)
word2int={}
int2word={}

vocab_size=len(words)

for i,word in enumerate(word):
    word2int[word]=i
    int2word[i]=word
    
