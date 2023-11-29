import spacy
#nlp=spacy.load("en_core_web_sm")
import random
from spacy.util import minibatch,compounding
from pathlib import Path
from spacy.training.example import Example
import streamlit as st









nlp=spacy.load("en_core_web_sm")
nlp.pipe_names
train=[("Apple is a fruit.", {"entities": [(0, 5, "Fruit")]}),
   ("brinjal", {"entities": [(0, 7, "Vegetable")]}),
       
       ("Vitamin A",{"entities":[(0,9,"Vitamin")]}),
       ("Retinol",{"entities":[(0,7,"Vitamin A")]}),
       ("Retinyl palmitate",{"entities":[(0,17,"Vitamin A")]}),
       ("Beta-Carotene",{"entities":[(0,13,"Pro-VitaminA")]}),
       ("Thiamine chloride hydrochloride",{"entities":[(0,31,"VitaminB1")]}),
       ("Riboflavin",{"entities":[(0,10,"Vitamin b2")]}),
       ("Riboflavin 5’- phosphate sodium",{"entities":[(0,32,"Vitamin b2")]}),
       ("Calcium",{"entities":[(0,7,"Minerals")]}),
       ("Chloride",{"entities":[(0,8,"Minerals")]}),
       ("Copper",{"entities":[(0,6,"Minerals")]}),
       ("Iodine",{"entities":[(0,6,"Minerals")]}),
       ("Iron",{"entities":[(0,4,"Minerals")]}),
       ("Magnesium ",{"entities":[(0,9,"Minerals")]}),
       ("Manganese ",{"entities":[(0,9,"Minerals")]})
,("Molybdenum ",{"entities":[(0,9,"Minerals")]}),
       ("Phosphorous ",{"entities":[(0,11,"Minerals")]}),
       ("Potassium",{"entities":[(0,9,"Minerals")]})
,("Selenium",{"entities":[(0,8,"Minerals")]})
,("Sodium",{"entities":[(0,6,"Minerals")]}),
       ("Boron",{"entities":[(0,5,"Minerals")]}),
       ("L-Histidine",{"entities":[(0,11,"Amino-acid")]}),
       ("L-Histidine hydrochloride",{"entities":[(0,25,"Amino-acid")]}),
       ("L-Isoleucine",{"entities":[(0,12,"Amino-acid")]}),
       ("L-Isoleucine hydrochloride",{"entities":[(0,26,"Amino-acid")]}),
       ("L-Leucine",{"entities":[(0,9,"Amino-acid")]})
,("L-Leucine hydrochloride",{"entities":[(0,23,"Amino-acid")]}),
       ("L-Lysine hydrochloride",{"entities":[(0,22,"Amino-acid")]}),
       ("DL-Methionine",{"entities":[(0,13,"Amino-acid")]}),
       ("L-Cysteine",{"entities":[(0,10,"Amino-acid")]}),
       ("L-Cysteine hydrochloride",{"entities":[(0,24,"Amino-acid")]}),
       ("L-Carnitine",{"entities":[(0,11,"Amino-acid")]}),
       ("L-Carnitine hydrochloride",{"entities":[(0,25,"Amino-acid")]})
,("L-Citruline",{"entities":[(0,11,"Amino-acid")]})
       ,("Adenosine 5-monophosphate ",{"entities":[(0,25,"Nucleotides")]})
       ,("Vitamin A ",{"entities":[(0,9,"Vitamin")]}),
       ("Vitamin B ",{"entities":[(0,9,"Vitamin")]}),
       ("Vitamin C ",{"entities":[(0,9,"Vitamin")]}),
       ("Vitamin B12 ",{"entities":[(0,10,"Vitamin")]}),
       ("Abelmoschus moschatus ",{"entities":[(0,21,"Botanical Ingrdient")]}),
       ("Stem bark ",{"entities":[(0,9,"Botanical Ingrdient")]}),
("Acacia catechu  ",{"entities":[(0,14,"Botanical Ingrdient")]}),
       ("Bacopa monnier  ",{"entities":[(0,14,"Botanical Ingrdient")]}),
       ("Ajuga bracteosa wall  ",{"entities":[(0,20,"Botanical Ingrdient")]}),
       ("Bombax ceiba L  ",{"entities":[(0,14,"Botanical Ingrdient")]}),
("Brassica rapa L  ",{"entities":[(0,15,"Botanical Ingrdient")]}),
       ("Bixa orellana  ",{"entities":[(0,13,"Botanical Ingrdient")]}),
       ("Camellia sinensis ",{"entities":[(0,17,"Botanical Ingrdient")]}),
       ("Carissa carandas L. ",{"entities":[(0,19,"Botanical Ingrdient")]})]

'''ner=nlp.get_pipe("ner")
for _,annotations in train:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])
disable_pipes=[pipe for pipe in nlp.pipe_names if pipe!=ner]
for text, _ in train:
    doc=nlp(text)
    print("abc")
    print("Entities",[(ent.text,ent.label_) for ent in doc.ents])'''
entity_dict = {}
for text, _ in train:
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    for value, label in entities:
        if value.lower() not in entity_dict:
            entity_dict[value.lower()] = [(value, label)]
        else:
            entity_dict[value.lower()].append((value, label))

# Example usage
input_value = "Apple"
input_value_lower = input_value.lower()

if input_value_lower in entity_dict:
    entities_for_value = entity_dict[input_value_lower]
    print(f"Entities for '{input_value}': {entities_for_value}")
else:
    print(f"No entities found for '{input_value}'.")
st.title("Entity Search")

# User input for value
input_value = st.text_input("Enter a value:")

# Convert input to lowercase for case-insensitive search
input_value_lower = input_value.lower()

# Display entities if input is found in the dictionary
if input_value_lower in entity_dict:
    entities_for_value = entity_dict[input_value_lower]
    st.subheader(f"Entities for '{input_value}':")
    for value, label in entities_for_value:
        st.write(f"- Entity: {value}, Label: {label}")
else:
    st.warning(f"No entities found for '{input_value}'.")

