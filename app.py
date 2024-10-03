from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Yu-Gi-Oh", message="Is King of Games")


@app.route('/darkMagician/<cardType>')
def darkMagician(cardType):
    if cardType == 'Normal':
        bg_color = '#FDE68A'  # Background color for Normal
    elif cardType == 'Effect':
        bg_color = '#FF8B53'  # Background color for Effect
    else:
        bg_color = '#FFFFFF'  # Default background if cardType is unknown
    return render_template('cards.html', bg_color=bg_color, monsterName= "Dark Magician", elementType="Dark", stars="7", cardName="Dark-Magician.jpg", creatureType="Spellcaster", cardType="Normal", atk="2500", defense="2100")

@app.route('/blueEyesWhiteDragon')
def blueEyesWhiteDragon():
    return render_template('cards.html', monsterName="Blue Eyes White Dragon", elementType="Light", stars="8", cardName="BlueEyesWhiteDragon-OW.webp", creatureType="Dragon", cardType="Normal", atk="3000", defense="2500")

@app.route('/celticGuardian')
def celticGuardian():
    return render_template('cards.html', monsterName="Celtic Guardian", elementType="Earth", stars="4", cardName="CelticGuardian-OW.webp", creatureType="Warrior", cardType="Normal", atk="1400", defense="1200")


@app.route('/redEyesBlackDragon')
def redEyesBlackDragon():
    return render_template('cards.html', monsterName="Red Eyes Black Dragon", elementType="Dark", stars="7", cardName="RedEyesBDragon-OW.webp", creatureType="Dragon", cardType="Normal", atk="2400", defense="2000")

if __name__ == '__main__':
    app.run(debug=True)


