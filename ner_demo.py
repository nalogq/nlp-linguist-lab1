import spacy

nlp = spacy.load("ru_core_news_sm")

text = "Анна Петрова работает в компании Яндекс в Москве."

doc = nlp(text)

for ent in doc.ents:
    print(f"{ent.text}\t{ent.label_}")
