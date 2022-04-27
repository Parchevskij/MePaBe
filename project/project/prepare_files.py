import codecs
import json
import os

json_file = "/Users/evgenij/PycharmProjects/MePaBe/project/rbc_ru.json"
json_data = []

os.mkdir("sas_ready_txt_rbc")
with open(json_file) as json_fileopen:
    json_data = json.load(json_fileopen)


# def process_text(line):
#     text = line['text'].replace('\xa0', ' ')
#     data = line['date']
#     text = " ".join([sent for sent in text])
#     title_list = text.split(' — ')
#     text = title_list[0]
#     data = data.replace("'", "")
#     data = data.replace("\xa0", ' ')
#     data = data.strip()
#
#     return text + "\n\n" + data

def process_text(text, date):
    # text_list = text.split(".")
    # text_list = text_list[1:]
    # text = ".".join([sent for sent in text_list])
    # title = " ".join([sent for sent in title])
    # title_list = title.split(' — ')
    # title = title_list[0]
    text = text.replace("'", "")
    text = text.replace("\xa0", ' ')
    text = text.strip()

    return text + '\n\n' + date


article_uuid = 1
for article in json_data:
    article_text = process_text(article['text'], article['date'])
    with codecs.open("sas_ready_txt_rbc/" + str(article_uuid) + ".txt", "w", "utf-8-sig") as temp:
        temp.write(article_text)
    article_uuid += 1

