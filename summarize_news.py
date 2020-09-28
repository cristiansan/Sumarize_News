import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

url = 'https://edition.cnn.com/2020/09/27/health/us-coronavirus-sunday/index.html'


article=Article(url)

article.download()
article.parse()
article.nlp()

print(f'Title: {article.title}')
