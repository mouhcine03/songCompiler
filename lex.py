from googletrans import Translator
import ply.lex as lex
import ply.yacc as yacc
import json
import os 
import re
import tkinter as tk

#-----------------------------constants-----------------------------
#Rihab
#path = r'C:\Users\HP\Documents\compilation\projetCompilation\errorLog.json'
#Mohcine
path = r'C:\Users\HP\Documents\compilation\projetCompilation\errorLog.json'
#dictionary
dataDic = {
    "lexical_error": [],
    "syntactic_error": [],
    "semantic_error": []
}
dataTemplate = {
        "Type": "",
        "Description": "",
        "Position": "",
        "Line":""
   
}


#error log
#creating a json file :

def writeJson(data, filename=path):
    # Check if the file exists in our file system using the library "os"
    if os.path.exists(filename): 
        # Read existing data
        with open(filename, 'r') as f:
            try:
                existing_data = json.load(f) #storing the existing data in the json file in a list called existing_data
            except json.JSONDecodeError:
                existing_data = {"lexical_error": [], "syntactic_error": [], "semantic_error": []}
    else:
        existing_data = {"lexical_error": [], "syntactic_error": [], "semantic_error": []}
    
    # Merge new data with existing data
    for key in data:
        existing_data[key].extend(data[key]) #appending the new error in the existing_data list
    
    # Write the merged data back to the file
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4) #updating the json file

#function for storing the errors in the dictionaries defined before
def errorLog(error_type, description, line=None, position=None):
    errorEntry = dataTemplate.copy()
    errorEntry["Type"] = error_type
    errorEntry["Description"] = description
    errorEntry["Line"] = line
    errorEntry["Position"] = position

    if error_type == "lexical":
        dataDic["lexical_error"].append(errorEntry)
    elif error_type == "syntaxique":
        dataDic["syntactic_error"].append(errorEntry)
    elif error_type == "semantique":
        dataDic["semantic_error"].append(errorEntry)


# Define the tokens and grammar rules
tokens = (
    "NOUNS",
    "VERBS",
    "ADVERBS",
    "ADJECTIVES",
    "ARTICLES",
    "PREPOSITIONS",
    "PRONOUNS",
    "DETERMINANT",
    "CONJUNCTIONS",
    "INTERJECTIONS",
    "PUNCTUATION",
    "LPAREN",
    "RPAREN"
)

# Define the token patterns
t_ignore = " \t"
t_NOUNS = r"\b(?:soul|love|heart|children|thanks|lord|place|sinner|mankind|beliefs|song|chance|doom|father|creation|thing|remarks|question|man|pity|chances|plea|battle|kingdoms|house)\b"
t_VERBS = r"\b(?:beginning|get|feel|hear|crying|saying|give|ask|is|has|hurt|save|comes|singing|pass|was|be|fight|have|grows|ain't|hiding|pleading|will|let's|let|praise|i'd|'m|am|like|join|tell|pray|would|trust)\b"
t_ADVERBS = r"\b(?:together|really|one|more|alright|just|all|there)\b"
t_ADJECTIVES = r"\b(?:my|mercy|own|holy|thinner|dirty|hopeless)\b"
t_ARTICLES = r"\b(?:a|the)\b"
t_PREPOSITIONS = r"\b(?:to|from|in|about|for|of|at|on|among)\b"
t_PRONOUNS = r"\b(?:you|us|i|them|who|it|shall|those|this|what|whose)\b"
t_DETERMINANT = r"\b(?:his|their|no|yes)\b"
t_CONJUNCTIONS = r"\b(?:and|or|so|when|as)\b"
t_INTERJECTIONS = r"\b(?:oh|woah)\b"
t_PUNCTUATION = r"[!?.,;:\"—-]"
t_LPAREN = r"\("
t_RPAREN = r"\)"

# Error handling for illegal characters
def t_error(t):
    error_message = f"Illegal character '{t.value[0]}' at line {t.lineno}"
    errorLog("lexical", error_message, t.lineno, t.lexpos)
    writeJson(dataDic)
    t.lexer.skip(1)
    raise Exception(error_message)

# Newline handling to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Lexical analysis function
def lexicalAnalysis():
    try :
        print("-----------------------------Lexical analysis-----------------------------")
        lexer = lex.lex()  # Create the lexer
        try:
            text = textbox.get("1.0", "end-1c")  # Get text from the Text widget
        except tk.TclError as e:
            print(f"Error accessing Text widget: {e}")
            labelRLEX.config(text="\nError: Unable to access the text widget.")
            return
        data = process_data(text)
        lexer.input(data.lower())
        tokens_list = []
        for tok in lexer:
            tokens_list.append(tok)
    except Exception as e:
        print(f'{e}')
        labelRLEX.config(text=labelRLEX.cget("text")+ str(e))
        lines = labelRLEX.cget("text").split("\n")
        labelRSYN.config(height=len(lines))
        return None
    process_lines(tokens_list)
    
# Grammar rule for "S" (sentence)
def p_S(p):
    '''
    S : ADVP PUNCTUATION ADVP PUNCTUATION
      | VP CP PUNCTUATION
      | ADVP LPAREN INTERJECTIONS NP RPAREN PUNCTUATION
      | ADVP LPAREN VP RPAREN PUNCTUATION
      | ADVP PUNCTUATION
      | VP LPAREN PP RPAREN PUNCTUATION
      | CP LPAREN CP RPAREN PUNCTUATION
      | VP VP ADJP LPAREN ADVP RPAREN PUNCTUATION
      | ADVP VP PP LPAREN ADVP RPAREN PUNCTUATION
      | VP NP PP PUNCTUATION
      | VP ADVP ADJP PUNCTUATION 
      | VP LPAREN VP PP RPAREN PUNCTUATION
      | VP PP ADJP PUNCTUATION
      | CP VP NP PUNCTUATION
      | VP VP PUNCTUATION
      | ADVP PP PUNCTUATION 
      | ADVP LPAREN INTERJECTIONS RPAREN PUNCTUATION
      | VP LPAREN VP RPAREN PUNCTUATION
      | ADVP LPAREN INTERJECTIONS NOUNS RPAREN PUNCTUATION
      | VP VP VP ADJP LPAREN ADVP RPAREN PUNCTUATION
      | VP CP LPAREN CONJUNCTIONS VP RPAREN PUNCTUATION
      | VP LPAREN VERBS VERBS PP RPAREN PUNCTUATION
      | VP LPAREN PP RPAREN 
    '''
    print(f"Rule matched: S → {p[1:]}")
    if p[1] ==("one", "love") and p[2] == "," and p[3] == ("one", "heart"):
        pass
    elif p[1] == ("one", "heart"):
        pass
    elif p[1] == ("let's","join","together") and p[2] == ("and",("feel","alright")):
        pass
    elif p[1] == ("one","love") and p[2] == "(" and p[3] == "oh" and p[4] == ("lord","of","mercy") and p[5] == ")":
        pass
    elif p[1] == ("one","heart") and p[2] == "(" and p[3] == ("i","tell","you") and p[4] == ")":
        pass
    elif p[1] == ("let's","join","together") and p[2] == "(" and p[3] == ("at",("this","house"),("i","pray")) and p[4] == ")":
        pass
    elif p[1] == ("and",("feel","alright")) and p[2] == "(" and p[3] == ("and",("i","will","feel","alright")) and p[4] == ")":
        pass
    elif p[1] == ("let","them","all") and p[2] == ("pass","all") and p[3] == ("their","dirty","remarks") and p[4] == "(" and p[5] == ("one","love") and p[6] == ")":
        pass
    elif p[1] == ("there","is","one","question") and p[2] == ("i'd","really","like") and p[3] == ("to","ask") and p[4] == "(" and p[5] == ("one","soul") and p[6] == ")":
        pass
    elif p[1] == ("is","there") and p[2] == ("a","place") and p[3] == ("for",("the","hopeless","sinner")) :
        pass
    elif p[1] == ("who","has","hurt","all","mankind") and p[2] == ("just",("to","save")) and p[3] == ("his","own") :
        pass
    elif p[1] == ("one","love") and p[2] == "(" and p[3] == ("hear","my","plea") and p[4] == ")":
        pass
    elif p[1] == ("let's","join","together") and p[2] == "(" and p[3] == ("let's","just","trust") and p[4] == ("in",("the","lord")) and p[5] == ")":
        pass
    elif p[1] == ("let's","join","together") and p[2] == ("to","fight") and p[3] == ("this","holy","battle"):
        pass
    elif p[1] == ("so","when") and p[2] == ("the","man","comes","there","will","be","no") and p[3] == ("no","doom"):
        pass
    elif p[1] == ('have','pity',('on','those','whose','chances')) and p[2] == ('grows','thinner'):
        pass
    elif p[1] == ('there',"ain't",'no',"hiding","place") and p[2] == ("among","the","kingdoms","of","love","yes"):
        pass
    elif p[1] == ("one","heart") and p[2] == "(" and p[3] == "oh" and p[4] == ")":
        pass
    elif p[1] == ("let's","join","together") and p[2] == "(" and p[3] == ("let","this","house","a","pray") and p[4] == ")":
        pass
    elif p[1] ==("one", "love") and p[2] == "(" and p[3] == "oh" and p[4] == "lord" and p[5] == ")":
        pass
    elif p[1] == ("one","heart") and p[2] == "(" and p[3] == "oh" and p[4] == "lord" and p[5] == ")":
        pass
    elif p[1] == ("let's", 'join', 'together') and p[2] == '(' and p[3] == ("let's", 'all', 'pray') and p[4] == ('to', ('the', 'lord')) and p[5] == ')':
        pass
    elif p[1] == ('i', 'tell', 'you') and p[2] == ('let', 'them', 'all') and p[3] == ('pass', 'all') and p[4] == ('their', 'dirty', 'remarks') and p[5] == '(' and p[6] == ('one', 'love') and p[7] == ")":
        pass
    elif p[1] == ("let's", 'join', 'together') and p[2] == "(" and p[3] == ('at', ('this', 'house'), 'a', 'pray') and p[4] == ")":
        pass
    elif p[1] == ('one', 'heart') and p[2] == "(" and p[3] == ('hear', 'my', 'plea') and p[4] == ")":
        pass
    elif p[1] == ("let's","join","together") and p[2] == "(" and p[3] == "let's" and p[4] == "pray" and p[5] == ('to', ('the', 'lord')) and p[6] == ")":
        pass
    else:
        error_message = f"Semantic error S: check out the structure of your phrase."+"\n"
        labelRSEM.config(text=labelRSEM.cget("text") + error_message)
        lines = labelRSEM.cget("text").split("\n")
        labelRSEM.config(height=len(lines))
        errorLog("semantic", error_message)
        writeJson(dataDic)

def p_ADVP(p):
    '''
    ADVP : ADVERBS NOUNS
         | ADVERBS VERBS
         | ADVERBS VERBS ADJP
         | ADVERBS VERBS ADVERBS
         | ADVERBS VERBS ADVERBS NOUNS
         | ADVERBS PP
         | ADVERBS VERBS DETERMINANT VERBS NOUNS  
    '''
    print(f"Rule matched: ADVP → {p[1:]}")
    if p[1] == "one" and p[2] == "love" or p[1] == "one" and p[2] == "heart" or p[1] == "one" and p[2] == "soul":
        p[0] = (p[1],p[2])
    elif p[1] == "there" and p[2] == "is" and p[3] == "one" and p[4] == "question":
        p[0] = (p[1],p[2],p[3],p[4])
    elif p[1] == "just" and p[2] == ("to","save"):
        p[0] = (p[1],p[2])
    elif p[1] == 'there' and p[2] == "ain't" and p[3] == 'no' and p[4] == "hiding" and p[5] == "place":
        p[0] = (p[1],p[2],p[3],p[4],p[5])
    else :
        error_message = f"Semantic error ADVP: please check the structure of your phrase."+"\n"
        labelRSEM.config(text=labelRSEM.cget("text") + error_message)
        lines = labelRSEM.cget("text").split("\n")
        labelRSEM.config(height=len(lines))
        errorLog("semantic", error_message)
        writeJson(dataDic)

def p_VP(p):
    '''
    VP : VERBS VERBS ADVERBS
       | VERBS ADVERBS 
       | PRONOUNS VERBS PRONOUNS
       | PRONOUNS VERBS
       | PRONOUNS VERBS VERBS ADVERBS
       | VERBS PRONOUNS ADVERBS
       | VERBS ADVERBS VERBS 
       | PRONOUNS VERBS VERBS ADVERBS NOUNS
       | VERBS ADJECTIVES NOUNS
       | ARTICLES NOUNS VERBS ADVERBS VERBS  VERBS DETERMINANT  
       | VERBS NOUNS PP
       | VERBS ADJECTIVES
       | VERBS PRONOUNS NOUNS ARTICLES VERBS 
        
    '''
    
    print(f"Rule matched: VP → {p[1:]}")
    if p[1] == "let's" and p[2] == "join" and p[3] == "together":
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "feel" and p[2] == "alright" :
        p[0] = (p[1],p[2])
    elif p[1] == "i" and p[2] == "tell" and p[3] == "you":
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "i" and p[2] == "pray":
        p[0] = ("i","pray")
    elif p[1] == "i" and p[2] == "will" and p[3] == "feel" and p[4] == "alright":
        p[0] = (p[1],p[2],p[3],p[4])
    elif p[1] == "let" and p[2] == "them" and p[3] == "all" :
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "pass" and p[2] == "all" :
        p[0] = (p[1],p[2])
    elif p[1] == "i'd" and p[2] == "really" and p[3] == "like" :
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "is" and p[2] == "there":
        p[0] = (p[1],p[2])
    elif p[1] == 'who'and p[2] == 'has' and p[3] == 'hurt' and p[4] == 'all' and p[5] == 'mankind':
        p[0] = (p[1],p[2],p[3],p[4],p[5])
    elif p[1] == "hear" and p[2] == "my" and p[3] == "plea" :
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "let's" and p[2] == "just" and p[3] == "trust" :
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "the" and p[2] == "man" and p[3] == "comes" and p[4] == "there" and p[5] == "will" and p[6] == "be" and p[7] == "no" :
        p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7])
    elif p[1] == "have" and p[2] == "pity" and p[3] == ("on","those","whose","chances"):
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "grows" and p[2] == "thinner":
        p[0] = (p[1],p[2])
    elif p[1] == 'let'and p[2] == 'this' and p[3] == 'house' and p[4] == 'a' and p[5] == "pray":
        p[0] = (p[1],p[2],p[3],p[4],p[5])
    elif p[1] == "let's" and p[2] == "all" and p[3] == "pray":
        p[0] = (p[1],p[2],p[3])
    else:
        error_message = f"Semantic error VP: check out the structure of your phrase please."+"\n"
        labelRSEM.config(text=labelRSEM.cget("text") + error_message)
        lines = labelRSEM.cget("text").split("\n")
        labelRSEM.config(height=len(lines))
        errorLog("semantic", error_message)
        writeJson(dataDic)

def p_NP(p):
    '''
    NP : NOUNS PREPOSITIONS ADJECTIVES
       | PRONOUNS NOUNS
       | ARTICLES NOUNS
       | DETERMINANT NOUNS 
       
    '''
    print(f"Rule matched: NP → {p[1:]}")
    if p[1] == "lord" and p[2] == "of" and p[3] == "mercy":
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "this" and p[2] == "house":
        p [0] = ("this","house")
    elif p[1] == "a" and p[2] == "place" :
        p[0] = (p[1],p[2])
    elif p[1] == "the" and p[2] == "lord":
        p [0] = ("the","lord")
    elif p[1] == "no" and p[2] == "doom":
        p [0] = ("no","doom")
    else:
        error_message = f"Semantic error NP: check out the structure of your phrase please."+"\n"
        labelRSEM.config(text=labelRSEM.cget("text") + error_message)
        lines = labelRSEM.cget("text").split("\n")
        labelRSEM.config(height=len(lines))
        errorLog("semantic", error_message)
        writeJson(dataDic)


def p_PP(p):
    '''
    PP : PREPOSITIONS NP VP 
       | PREPOSITIONS VERBS 
       | PREPOSITIONS ADJP
       | PREPOSITIONS NP
       | PREPOSITIONS NOUNS
       | PREPOSITIONS PRONOUNS PRONOUNS NOUNS
       | PREPOSITIONS ARTICLES NOUNS PREPOSITIONS NOUNS DETERMINANT
       | PREPOSITIONS ARTICLES NOUNS
       | PREPOSITIONS NP ARTICLES VERBS
    '''
    #i added the last one 
    print(f"Rule matched: PP → {p[1:]}")
    if p[1] == 'at' and p[2] == ("this","house") and p[3] == ("i","pray"):
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "to" and p[2] == "ask" or  p[1] == "for" and p[2] == ("the","hopeless","sinner") or p[1] == "to" and p[2] == "save" or p[1] == "in" and p[2] == ("the","lord") or p[1] == "to" and p[2] == "fight":
        p[0] = (p[1],p[2])
    elif p[1]=='on' and p[2] == 'those' and p[3] == 'whose' and p[4] == 'chances':
        p[0] = (p[1],p[2],p[3],p[4])
    elif p[1] == "among" and p[2] == "the" and p[3] == "kingdoms" and p[4] == "of" and p[5] == "love" and p[6] == "yes":
        p[0] = (p[1],p[2],p[3],p[4],p[5],p[6])
    elif p[1] == "to" and p[2] == ("the","lord"):
        p[0] = (p[1],p[2])
    elif p[1] == 'at' and p[2] == ("this","house") and p[3] == "a" and p[4] == "pray":
        p[0] = (p[1],p[2],p[3],p[4])
    else:
        error_message = f"Semantic error PP: check out the structure of your phrase please."+"\n"
        labelRSEM.config(text=labelRSEM.cget("text") + error_message)
        lines = labelRSEM.cget("text").split("\n")
        labelRSEM.config(height=len(lines))
        errorLog("semantic", error_message)
        writeJson(dataDic)
def p_CP(p):
    '''
    CP : CONJUNCTIONS VP 
       | CONJUNCTIONS CONJUNCTIONS
       
    '''
    print(f"Rule matched: CP → {p[1:]}")
    if p[1] == "and" and p[2] == ("feel","alright"):
        p[0] = (p[1],p[2])
    elif p[1] == "and" and p[2] == ("i","will","feel","alright"):
        p[0] = (p[1],p[2])
    elif p[1] == "so" and p[2] == "when":
        p[0] = (p[1],p[2])
    else:
        error_message = f"Semantic error CP: did you mean and feel alright."+"\n"
        labelRSEM.config(text=labelRSEM.cget("text") + error_message)
        lines = labelRSEM.cget("text").split("\n")
        labelRSEM.config(height=len(lines))
        errorLog("semantic", error_message)
        writeJson(dataDic)

def p_ADJP(p):
    '''
    ADJP : DETERMINANT ADJECTIVES NOUNS 
         | ARTICLES ADJECTIVES NOUNS
         | DETERMINANT ADJECTIVES
         | PRONOUNS ADJECTIVES NOUNS
         | NOUNS ADJECTIVES 
    '''
    print(f"Rule matched: ADJP → {p[1:]}")
    if p[1] == "their" and p[2] == "dirty" and p[3] == "remarks":
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "the" and p[2] == "hopeless" and p[3] == "sinner":
        p[0] = (p[1],p[2],p[3])
    elif p[1] == "his" and p[2] == "own":
        p[0] = (p[1],p[2])
    elif p[1] == "this" and p[2] == "holy" and p[3] == "battle" :
        p[0] = (p[1],p[2],p[3])
    else:
        error_message = f"Semantic error ADJP: check out the structure of your phrase please."+"\n"
        labelRSEM.config(text=labelRSEM.cget("text") + error_message)
        lines = labelRSEM.cget("text").split("\n")
        labelRSEM.config(height=len(lines))
        errorLog("semantic", error_message)
        writeJson(dataDic)



# Error handling for parsing
def p_error(p):
    if p:
        error_message = f"Syntax error at token '{p.type}' with value '{p.value}'"
        errorLog("syntactic", error_message, p.lineno, p.lexpos)
        writeJson(dataDic)
        raise Exception(error_message)
    else:
        error_message = "Syntax error at EOF (end of file)"
        errorLog("syntactic", error_message)
        writeJson(dataDic)
        raise Exception(error_message)

def process_lines(tokens_list):
    parser = yacc.yacc()  # Create the parser
    current_line = []

    for tok in tokens_list:
        current_line.append(tok.value)
        if tok.type == 'PUNCTUATION' and tok.value in ['.', '!', '?']:
            raw_input = " ".join(current_line)
            print(f"\nProcessing line: {raw_input}")
            try:
                parser.parse(raw_input)
                message = f"Successfully processed line: {raw_input}\n"
                labelRSYN.config(text=labelRSYN.cget("text") + message)
                lines = labelRSYN.cget("text").split("\n")
                labelRSYN.config(height=len(lines))
            except Exception as e:
                error_message = f"Syntax error: {e}\n"
                labelRSYN.config(text=labelRSYN.cget("text") + error_message)
                lines = labelRSYN.cget("text").split("\n")
                labelRSYN.config(height=len(lines))

             #Traduction du texte après les analyses
            translations = translate_texts(raw_input)
            if translations:
                print(f"Translated line (French): {translations['fr']}")
                print(f"Translated line (Spanish): {translations['es']}")
                print(f"Translated line (italien): {translations['it']}")
                
            current_line = []  # Reset for the next line


# translation function
def translate_texts(text, target_languages=['it', 'fr', 'es']):
    translator = Translator()
    translations = {}
    for lang in target_languages:
        try:
            translation = translator.translate(text, dest=lang)
            translations[lang] = translation.text
        except Exception as e:
            print(f"Translation error for {lang}: {e}")
            translations[lang] = None
    return translations

# data processing function
def process_data(data):
    processed_lines = []
    pattern = r"\.$|!$|\?$"  # Matches sentences ending with '.', '!', or '?'
    Pdatas = data.splitlines()  
    for Pdata in Pdatas:
        match = re.search(pattern, Pdata)
        if match is None:
            Pdata = Pdata + "."
        processed_lines.append(Pdata)
    return "\n".join(processed_lines)


# Define the window close handler
def on_close():
    print("Window is closing... cleaning up!")
    window.destroy()

window = tk.Tk()
window.geometry("900x900")
window.title("one love - Bob Marley")
window.protocol("WM_DELETE_WINDOW", on_close)

label = tk.Label(window, text="Welcome to the compiler made for the Bob Marley song - one love"+"\n"+"made by ANANOUCH Mouad, EL HASNAOUI Mohcine, GHAILAN Taha and SEMMAR Rihab",font={'Ariel',13})
label1 = tk.Label(window, text="Enter the desired lyric:",font={'Ariel',10})
textbox = tk.Text(window, height=3, width=50, font=("Arial", 10))
button = tk.Button(window, text="analysis",font=('Ariel',10),command=lexicalAnalysis)
labelLEX = tk.Label(window,text="Lexical Analysis Result:",font=('Ariel',13))
labelRLEX = tk.Label(window)
labelSYN = tk.Label(window,text="Syntactic Analysis Result:",font=('Ariel',13))
labelRSYN = tk.Label(window)
labelSEM = tk.Label(window,text="Semantic Analysis Result:",font=('Ariel',13))
labelRSEM = tk.Label(window)

#placing on the window
label.place(x=50,y=60)
label1.place(x=50,y=120)
textbox.place(x=50,y=150)
button.place(x=50,y=220)
labelLEX.place(x=50,y=260)
labelRLEX.place(x=50,y=280)
labelSYN.place(x=50,y=320)
labelRSYN.place(x=50,y=340)
labelSEM.place(x=50,y=440)
labelRSEM.place(x=50,y=460)
window.mainloop()


#Main function
def main():
    
    

 #Entry point 
 if __name__ == "__main__":
    main()
