from app import app
import controller


@app.route('/')
def inicio():
    return controller.inicio()


@app.route('/stats')
def stats():
    return controller.stats()


@app.route('/mutant/', methods=['POST'])
def newMutant():
    return controller.newMutant()
