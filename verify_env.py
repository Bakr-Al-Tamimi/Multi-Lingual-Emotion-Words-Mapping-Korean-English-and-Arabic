import sys
import os

def verify():
    print(f"Python version: {sys.version.split()[0]}")
    
    # 1. Check for Pandas
    try:
        import pandas as pd
        print(f"✅ pandas is installed (version: {pd.__version__})")
    except ImportError:
        print("❌ pandas is NOT installed. Please run: pip install pandas")
        
    # 2. Check for Deep-Translator
    try:
        import deep_translator
        print(f"✅ deep-translator is installed (version: {deep_translator.__version__})")
    except ImportError:
        print("❌ deep-translator is NOT installed. Please run: pip install deep-translator")
        
    # 3. Check for the dataset
    filename = "Emotion_Words_Combined_Clean.csv"
    if os.path.isfile(filename):
        print(f"✅ Dataset '{filename}' found in the current directory.")
    else:
        print(f"❌ Dataset '{filename}' NOT found. Please move it into this folder.")

if __name__ == "__main__":
    print("--- Environment Verification ---")
    verify()
    print("--------------------------------")