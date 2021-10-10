import string
import json
from meter_type import *
import os
import spacy
from rhyme import rhyme_scheme

nlp = spacy.load("en_core_web_sm")


def remove_special_symbols(str):
    a = str.replace('\u2018', '\'')
    a = a.replace('\u2019', '\'')
    a = a.replace('—', ' - ')
    a = a.replace('“', '\"')
    a = a.replace('”', '\"')
    a = a.replace(' ', ' ')
    return (a)


"""
creates tsakorpus json
"""


def tsa_json(meta, corpus_dir):
    text_dic = {}
    txt_file = meta[0]
    author = meta[2]
    json_name = txt_file.replace('txt', 'json')

    with open(os.path.join(corpus_dir, txt_file), encoding='utf-8') as txt:
        lines = txt.readlines()
    poem_text = remove_special_symbols(''.join(lines))
    lines = [remove_special_symbols(x.strip()) for x in lines]
    text_dic['meta'] = {}
    text_dic['meta']['filename'] = json_name
    text_dic['meta']['title'] = meta[1]
    text_dic['meta']['author'] = author
    text_dic['meta']['language'] = 'English'
    text_dic['meta']['school/period'] = meta[-1]
    text_dic['meta']['year'] = meta[-2]
    body = []
    spacy_text = nlp(poem_text)
    text_words = []
    text_words = [(i.text, i.lemma_, i.pos_) for i in spacy_text if not i.text in ['\n', '\n\n', '\n \n\n']]
    word_count = 0
    syl_ar = ''
    if lines[-1] == '':
        i = 1
        while lines[-i - 1] == '':
            i += 1

        body = lines[:-i]
    else:
        body = lines
    text = []
    stanza = 0
    num_of_stanzas = 1
    first_stanza = []
    for line in body:
        if line == '':
            num_of_stanzas += 1
            stanza += 1
            continue
        if stanza == 0:
            first_stanza.append(line)
        line = remove_special_symbols(line)
        pos_lem = nlp(line)
        words = [i.text for i in pos_lem]
        line_dict = {}
        line_dict['text'] = line
        wcnt = 0
        words_array = []
        meta = meters(line)
        meter = meta['meter']
        m_info = meter_type(meter)
        meta['foot_type'] = m_info[0]
        meta['foot_num'] = m_info[1]
        meta['stanza'] = str(stanza)
        g = 0
        for word in words:
            word_dict = {}
            word_dict['wf'] = word
            if word_dict['wf'] in string.punctuation or word == '’':
                word_dict['wtype'] = 'punct'
            else:
                word_dict['wtype'] = 'word'
            word_dict['off_start'] = line_dict['text'].find(word_dict['wf'], g)
            g = line_dict['text'].find(word_dict['wf'], g) + len(word_dict['wf'])
            word_dict['off_end'] = g
            word_dict['sentence_index'] = wcnt
            wcnt += 1
            word_dict['next_word'] = wcnt
            if word_dict['wtype'] == 'word':
                ana = []
                ana_dict = {}
                ana_dict['lex'] = text_words[word_count][1]
                ana_dict['gr.pos'] = text_words[word_count][2]
                word_dict['ana'] = [ana_dict]
            words_array.append(word_dict)
            word_count += 1
        line_dict['words'] = words_array
        line_dict['lang'] = 0
        line_dict['meta'] = meta
        text.append(line_dict)
    text_dic['sentences'] = text
    rhyme = rhyme_scheme(poem_text)
    text_dic['meta']['number_of_stanzas'] = str(num_of_stanzas)
    text_dic['meta']['has_rhyme'] = str(rhyme[0])
    text_dic['meta']['rhyme_scheme'] = rhyme[1]

    with open(os.path.join('jsons', json_name), 'w') as fp:
        json.dump(text_dic, fp, indent=4)
