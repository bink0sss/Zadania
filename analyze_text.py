def analyze_text(text, search_word):
   
    words = text.split()
    sentences = text.split('.')
    
    
    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()])  
    average_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0

   
    occurrences = [i for i, word in enumerate(words) if word == search_word]
    occurrence_count = len(occurrences)

  
    print(f"Liczba słów: {word_count}")
    print(f"Liczba zdań: {sentence_count}")
    print(f"Średnia długość słowa: {average_word_length:.2f} znaków")
    
    if occurrence_count > 0:
        print(f"Słowo '{search_word}' występuje {occurrence_count} razy na pozycjach: {occurrences}.")
    else:
        print(f"Słowo '{search_word}' nie występuje w tekście.")


text = input("Podaj tekst: ")
search_word = input("Podaj szukane słowo: ")

analyze_text(text, search_word)