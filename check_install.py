import sys
import os

print(f"Python Executable: {sys.executable}")
print(f"Working Directory: {os.getcwd()}")

# CHECK FOR SHADOWING
if os.path.exists("langchain.py"):
    print("🚨 CRITICAL ERROR: You have a file named 'langchain.py' in this folder!")
    print("   -> RENAME or DELETE it immediately. It is blocking the real library.")
    sys.exit()

if os.path.exists("langchain"):
    print("⚠️ WARNING: You have a folder named 'langchain' in this folder.")
    print("   -> If this is not your code, rename it.")

# ATTEMPT IMPORT
try:
    import langchain
    print(f"✅ LangChain imported from: {langchain.__file__}")
    print(f"   Version: {langchain.__version__}")
    
    from langchain.chains import ConversationalRetrievalChain
    print("✅ SUCCESS: ConversationalRetrievalChain found!")
    
except ImportError as e:
    print(f"❌ IMPORT ERROR: {e}")
    print("   -> This means the library is not installed in THIS Python environment.")