# from flask import Flask, jsonify
# import os
# import json
# import pandas as pd

# app = Flask(__name__)

# scraping_type = 'Partial' 

# source_file_path_seasons = os.getcwd() + "\\silver_tables\\TUN_Ligue1_seasons_from_1996.csv"
# df_seasons = pd.read_csv(source_file_path_seasons, delimiter=';')

# for l in range(len(df_seasons)):
#     season_type = df_seasons.iloc[l][3]
#     season = df_seasons.iloc[l][1]
#     if season_type == 'regular':
#         # Specify the path to your JSON file
#         src_file_path_results_json = os.getcwd() + "\\silver_tables\\json\\" + scraping_type + "\\TUN_Ligue1_" + str(season) + "_.json"
#     else:
#         src_file_path_results_json = os.getcwd() + "\\silver_tables\\json\\" + scraping_type + "\\TUN_Ligue1_" + str(season) + "_" + season_type +".json"

#     # Open the JSON file and load its contents
#     with open(src_file_path_results_json, "r") as file:
#         results = json.load(file)

#     # # Sample data
#     # results = [
#     #     {'id_game': 1, 'title': 'result 1', 'author': 'Author 1'},
#     #     {'id_game': 2, 'title': 'result 2', 'author': 'Author 2'},
#     #     {'id_game': 3, 'title': 'result 3', 'author': 'Author 3'}
#     # ]

#     # Route to get all results
#     @app.route(f'/api/results_{season}{season_type}', methods=['GET'])
#     def get_results():
#         return jsonify({'results': results})

#     # Route to get a specific result by ID
#     @app.route(f'/api/results_{season}{season_type}/<int:id_game>', methods=['GET'])
#     def get_result(id_game):
#         result = next((result for result in results if result['id_game'] == id_game), None)
#         if result:
#             return jsonify({'result': result})
#         else:
#             return jsonify({'error': 'result not found'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)
