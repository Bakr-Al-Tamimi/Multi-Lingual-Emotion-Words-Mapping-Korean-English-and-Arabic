import pandas as pd
from deep_translator import GoogleTranslator
import time
import os

def translate_to_arabic(text, translator):
    """Translates a single text string to Arabic, with a slight delay to respect API limits."""
    if pd.isna(text) or str(text).strip() == "":
        return ""
    try:
        time.sleep(0.3)  # Delay to prevent rate-limiting from the translation server
        return translator.translate(str(text))
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return ""

def main():
    input_file = 'Emotion_Words_Combined_Clean.csv'
    output_file = 'Emotion_Words_Combined_Arabic.csv'

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Please check your folder structure.")
        return

    print(f"Loading '{input_file}'...")
    df = pd.read_csv(input_file)

    # Initialize translator (English to Arabic)
    translator = GoogleTranslator(source='en', target='ar')

    print("Starting translation...")
    total_rows = len(df)
    
    arabic_words = []
    
    # Iterate through the DataFrame to translate row by row
    for idx, row in df.iterrows():
        eng_word = row.get('English_Word', '')
        ar_word = translate_to_arabic(eng_word, translator)
        arabic_words.append(ar_word)
        
        # Print progress every 100 words
        if (idx + 1) % 100 == 0:
            print(f"Translated {idx + 1}/{total_rows} words...")

    # Attach the new column to the DataFrame
    df['Arabic_Word'] = arabic_words

    # Save the new dataset using utf-8-sig to preserve Arabic characters
    print(f"Saving translated dataset to '{output_file}'...")
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print("Process complete!")

if __name__ == "__main__":
    main()