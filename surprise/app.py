from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Expanded emoji list to ensure enough emojis for each level
emoji_list = ["😀", "😃", "😄", "😁", "😆", "🙂", "😉", "😊", "😍", "😎", "🤩", "🤓", "😜", "🤯", "😱", "😇", "🥳", "😏", "🥰", "😈", 
              "😵", "😋", "🥳", "😎", "😡", "🥵", "🥶", "😤", "🤡", "😷", "😇", "👽", "👾", "🤖", "👻", "😺", "😸", "😹", "😻", 
              "😼", "😽", "🙀", "😿", "😾", "💩", "🤠", "🤑", "😪", "😴", "😵‍💫", "🧐", "🤓", "🥳", "🥸", "😈", "👿", "👺"]

# Function to generate level data, ensuring the target emoji is included in the list
def generate_level_data(level_num, emoji_count, target_emoji):
    emojis = random.sample(emoji_list, emoji_count - 1)  # Get n-1 random emojis
    emojis.append(target_emoji)  # Ensure the target emoji is included
    random.shuffle(emojis)  # Shuffle to mix the target emoji with others
    return {"level": level_num, "emojis": emojis, "target": target_emoji}

# Game data with increasing difficulty
levels = [
    generate_level_data(1, 15, "😉"),
    generate_level_data(2, 25, "😍"),
    generate_level_data(3, 35, "🤩"),
    generate_level_data(4, 45, "😜"),
    generate_level_data(5, 55, "🤪")
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<int:level>', methods=['GET', 'POST'])
def game(level):
    if level > len(levels):
        return render_template('surprise.html', message="Happy 2nd anniversary my love. I love you so much! 💕")
    
    if request.method == 'POST':
        chosen_emoji = request.form.get('emoji')
        target_emoji = levels[level - 1]['target']
        if chosen_emoji == target_emoji:
            return redirect(url_for('game', level=level + 1))
    
    return render_template('game.html', level=levels[level - 1])

if __name__ == '__main__':
    app.run(debug=True)
