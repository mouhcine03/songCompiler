from lex import process_lines,lexicalAnalysis
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