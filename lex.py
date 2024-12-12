import ply.lex as lex
import ply.yacc as yacc

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
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Newline handling to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Lexical analysis function
def lexicalAnalysis():
    print("-----------------------------Lexical analysis-----------------------------")
    lexer = lex.lex()  # Create the lexer
    data = """One love, one heart.
Let's join together and feel alright.
One love (oh Lord of mercy).
One heart (I tell you).
Let's join together (at this house I pray).
And feel alright (and I will feel alright).
Let's join together and feel alright.
let them all pass all their dirty remarks (one love).
There is one question I'd really like to ask (one soul).
Is there a place for the hopeless sinner.
Who has hurt all mankind just to save his own.
One love, one heart.
Let's join together and feel alright.
One love (hear my plea).
One heart.
Let's join together and feel alright.
Let's join together (let's just trust in the Lord).
And feel alright (and I will feel alright).
Let's join together to fight this holy battle.
So when the man comes there will be no no doom.
Have pity on those whose chances grows thinner.
There ain't no hiding place among the kingdoms of love yes.
One love (hear my plea).
One heart (oh).
Let's join together and feel alright.
One love (oh Lord of mercy) .
One heart (I tell you).
Let's join together (let this house a pray).
And feel alright (and I will feel alright).
Let's join together and feel alright.
One love, one heart.
Let's join together and feel alright.
One love (oh Lord).
One heart (oh Lord).
Let's join together and feel alright.
Let's join together (let's all pray to the Lord).
And feel alright (and I will feel alright).
I tell you let them all pass all their dirty remarks (one love).
There is one question i'd really like to ask (one soul).
Is there a place for the hopeless sinner.
Who has hurt all mankind just to save his own.
One love (oh Lord of mercy).
One heart (I tell you).
Let's join together (at this house I pray).
And feel alright (and I will feel alright).
One love (hear my plea).
One heart (hear my plea).
Let's join together and feel alright (and I will feel alright).
Let's join together (let's pray to the Lord).
And feel alright (and I will feel alright).
"""  # Example input (You can modify this)
    lexer.input(data.lower())  # Process input string

    tokens_list = []
    try:
        for tok in lexer:
            tokens_list.append(tok)
            print(f"Token: {tok.type}, Value: {tok.value}")
        return tokens_list  # Return the list of tokens
    except Exception as e:
        print(f"Lexical analysis error: {e}")
        return None

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
      
       
    '''
    print(f"Rule matched: S → {p[1:]}")

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

def p_NP(p):
    '''
    NP : NOUNS PREPOSITIONS ADJECTIVES
       | PRONOUNS NOUNS
       | ARTICLES NOUNS
       | DETERMINANT NOUNS 
       
    '''
    print(f"Rule matched: NP → {p[1:]}")

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

       
    '''
    print(f"Rule matched: PP → {p[1:]}")

def p_CP(p):
    '''
    CP : CONJUNCTIONS VP 
       | CONJUNCTIONS CONJUNCTIONS
       
    '''
    print(f"Rule matched: CP → {p[1:]}")

def p_ADJP(p):
    '''
    ADJP : DETERMINANT ADJECTIVES NOUNS 
         | ARTICLES ADJECTIVES NOUNS
         | DETERMINANT ADJECTIVES
         | PRONOUNS ADJECTIVES NOUNS
         | NOUNS ADJECTIVES 
    '''
    print(f"Rule matched: ADJP → {p[1:]}")




# Error handling for parsing
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.type}' with value '{p.value}'")
    else:
        print("Syntax error at EOF (end of file)")

# Modified function to process the input line by line
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
                print(f"Successfully processed line: {raw_input}")
            except Exception as e:
                print(f"Syntax error: {e}")
            current_line = []  # Reset for the next line

# Main function
def main():
    tokens_list = lexicalAnalysis()  # Perform lexical analysis
    if tokens_list:
        print("\n-----------------------------Syntactic analysis-----------------------------")
        process_lines(tokens_list)  # Process the tokens line by line
    else:
        print("Error in lexical analysis. Syntactic analysis will not be performed.")

# Entry point
if __name__ == "__main__":
    main()
