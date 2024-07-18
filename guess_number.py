from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

game_count = 0
player_wins = 0

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    global game_count, player_wins

    if request.method == 'POST':
        player_choice = request.form.get('player_choice')
        name = request.form.get('name', 'PlayerOne')

        if player_choice not in ["1", "2", "3"]:
            return render_template('index.html', error="Please enter 1, 2, or 3.", name=name)

        computer_choice = random.choice(["1", "2", "3"])
        player = int(player_choice)
        computer = int(computer_choice)

        if player == computer:
            player_wins += 1
            result = "🎉🎉🎉 You win!"
        else:
            result = f"Sorry, {name}. Better luck next time."

        game_count += 1
        win_percentage = f"{(player_wins/game_count)*100:.2f}%"

        return render_template('index.html', result=result, game_count=game_count, player_wins=player_wins, win_percentage=win_percentage, name=name,player=player, computer=computer)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
