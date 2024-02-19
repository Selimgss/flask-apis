from flask import Flask, jsonify, request
import os
import json
import pandas as pd

app = Flask(__name__)

scraping_type = 'Partial' 
#

parent_directory = os.path.dirname(os.getcwd())
grandparent_directory = os.path.dirname(parent_directory)
grandgrandparent_directory = os.path.dirname(grandparent_directory)
source_file_path_seasons = os.path.join(grandgrandparent_directory, "silver_tables", "TUN_Ligue1_seasons_from_1996.csv")
df_seasons = pd.read_csv(source_file_path_seasons, delimiter=';')

# Load all results data into a dictionary with keys being (season, season_type) tuples
results_data = {}

for _, row in df_seasons.iterrows():
    season_type = row[3]
    season = row[1]

    src_file_path_results_json = os.path.join(grandgrandparent_directory, "silver_tables", "json", scraping_type, f"TUN_Ligue1_{season}_{season_type}.json")

    with open(src_file_path_results_json, "r") as file:
        results = json.load(file)
        results_data[(season, season_type)] = results

@app.route('/api/results/<season>/<season_type>', methods=['GET'])
def get_results_for_season(season, season_type):
    key = (season, season_type)
    if key in results_data:
        return jsonify({'results': results_data[key]})
    else:
        return jsonify({'error': 'result not found'}), 404

@app.route('/api/results/<int:id_game>', methods=['GET'])
def get_result(id_game):
    for results in results_data.values():
        result = next((result for result in results if result['id_game'] == id_game), None)
        if result:
            return jsonify({'result': result})
    
    return jsonify({'error': 'result not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
