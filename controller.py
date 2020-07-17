from flask import request, abort, jsonify
import mutant
import models


def inicio():
    return {
        'api_info': 'Api RRHH de Magneto ',
        'endpoints': {
            "GET /stats": {
                'info': "Estadisticas de las verificaciones",
                'example_response': '{“count_mutant_dna”:40, “count_human_dna”:100: “ratio”:0.4}'
            },
            "POST /mutant": {
                'info': "Cargar nueva verificacion de DNA",
                'example_request': "{'dna':['ATGCGA','CAGTGC','TTATGT','AGAAGG','CCCCTA','TCACTG']}",
                'example_response': '200-OK (mutante) / 403-Forbidden (humano)',
                'constraint': "Lista de Strings NxN; Solo letras (A,T,C,G)"
            }
        }
    }


def newMutant():
    json = request.get_json()
    if 'dna' not in json:
        return jsonify({"error": "Formato incorrecto, ver opciones en la url raiz"}), 400

    dna = json['dna']
    if not mutant.validDna(dna):
        return jsonify({"error": "Formato incorrecto, ver opciones en la url raiz"}), 400

    isM = mutant.isMutant(dna)
    models.Dna(dna, isM).save()

    if isM:
        return jsonify({"OK": "es mutante"}), 200
    else:
        return jsonify({"error": "es humano"}), 403


def stats():
    human,mutant = models.Dna.stats()
    ratio = round(mutant/human,2) if human>0 else 0
    return jsonify({"count_mutant_dna":mutant, "count_human_dna":human, "ratio":ratio}), 200
