import gensim, nltk
import os,re
import numpy as np

'''
all_sentences = []
datapath = "./Data"
datafolders = os.listdir(datapath);
for folder in datafolders:
    folderpath = os.path.join(datapath, folder);
    datafile   = os.listdir(folderpath);
    for files in datafile:
        if re.match(".*\.txt",files):
            filepath = os.path.join(folderpath, files);
            print filepath
            filein = open(filepath).read().decode('utf8')
            lines = nltk.sent_tokenize(filein)
            for line in lines:
                for word in nltk.word_tokenize(line):
                    #print word.lower()
                    if word == 'comptroller': print "------ FOUND -------"
                    
                if nltk.word_tokenize(line) != []: all_sentences.append([word.lower() for word in nltk.word_tokenize(line)])

#print all_sentences
    #sentences = MySentences(datapath + '/')
    #print sentences # a memory-friendly iterator
#all_sentences.append(sentences)
model  = gensim.models.Word2Vec(all_sentences,min_count=1)
output = "./word2vec_output_new";
model.save(output)

'''
model = gensim.models.Word2Vec.load('./word2vec_output_new')
#print model['accommodation']
print model['legal']
phrase_embeddings = {}

phrases_path = './Results'
phrases_txt  = os.listdir(phrases_path)
for text_file in phrases_txt:
    filepath = os.path.join(phrases_path, text_file)
    print filepath
    with open(filepath,'r') as file_in:
        for line in file_in:
            #print line
            try:
                phrase = nltk.word_tokenize(line)
                print phrase
                text_phrase = '_'.join(phrase[0:len(phrase)-1])
                if phrase != [] and not re.match('NP',phrase[-1]) and phrase[0] != '\xe2\x80\xa2':
                    vec = model[phrase[0]]
                    for word in phrase[1:len(phrase)-1]: vec += model[word.decode('utf8')]
                    phrase_embedding = vec / (len(phrase)-1)
                    phrase_embeddings[text_phrase] = phrase_embedding
            except KeyError, e: print filepath, line
            except UnicodeDecodeError, e: print 'got a unicode decode error'

print phrase_embeddings.keys()
