from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Yu-Gi-Oh", message="Is King of Games")


@app.route('/darkMagician')
def darkMagician():
    return render_template('cards.html', monsterName= "Dark Magician", elementType="Dark", stars="7", cardName="Dark-Magician.jpg", creatureType="Spellcaster", cardType="Normal", atk="2500", defense="2100")

@app.route('/blueEyesWhiteDragon')
def blueEyesWhiteDragon():
    return render_template('cards.html', monsterName="Blue Eyes White Dragon", elementType="Light", stars="8", cardName="BlueEyesWhiteDragon-OW.webp", creatureType="Dragon", cardType="Normal", atk="3000", defense="2500")

@app.route('/redEyesBlackDragon')
def redEyesBlackDragon():
    return render_template('cards.html', monsterName="Red Eyes Black Dragon", elementType="Dark", stars="7", cardName="RedEyesBDragon-OW.webp", creatureType="Dragon", cardType="Normal", atk="2400", defense="2000")

if __name__ == '__main__':
    app.run(debug=True)


