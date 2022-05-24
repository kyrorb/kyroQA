## ctrl

print("test")

from pathlib import Path
import random

def grab_question():

  questions = []
  
  file = Path('papers/edexcel')
  paper_q = ""
  
  for entry in file.iterdir():
    
    if str(entry).endswith(".txt"):
      paper_q = str(entry)

  file = open(paper_q)
  questions_raw = file.readlines()

  for question_unf in questions_raw:

    if question_unf.endswith("")
  
  return questions_raw
  

grab_question()
  