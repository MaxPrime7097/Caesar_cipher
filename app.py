from flask import Flask,request, render_template 
app= Flask(__name__)
def caesar_cipher(text, shift):
    encrypted_text = ''  # This will store the encrypted result
    
    for char in text:  # Loop through each character in the input text 
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase letters start at 65 (A), lowercase at 97 (a) in ASCII
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base) #Normalize to 0-25 range using ASCII. Apply shift and wrap around using %26. Convert back to a letter and add to result
        else:
            encrypted_text += char  # Non-alphabet characters stay the same
    
    return encrypted_text

@app.route('/',
methods=['GET', 'POST'])
def home():  
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        result = caesar_cipher(text,shift)
    return render_template('index.html', result=result)

if __name__ == '_main_': app.run(debug=True)