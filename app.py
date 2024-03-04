import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Load the dataset from the CSV file into a Pandas DataFrame
df = pd.read_csv('C:/Users/namit/mini_project/World Happiness Report.csv')

# Route to fetch overall happiness scores for each year
@app.route('/happiness/scores')
def get_happiness_scores():
    # Group by 'Year' and calculate the mean happiness score for each year
    happiness_scores = df.groupby('Year')['Life Ladder'].mean().to_dict()
    return jsonify(happiness_scores)

# Route to fetch the rankings of countries for a specific year
@app.route('/happiness/rankings/<year>')
def get_country_rankings(year):
    # Filter the DataFrame for the specified year and return the rankings
    year_data = df[df['Year'] == int(year)]
    rankings = year_data[['Country Name', 'Life Ladder']].set_index('Country Name').to_dict()['Life Ladder']
    return jsonify(rankings)

# Route to fetch specific metrics contributing to happiness for a country
@app.route('/happiness/metrics/<year>/<country>')
def get_country_metrics(year, country):
    # Filter the DataFrame for the specified year and country and return the metrics
    year_country_data = df[(df['Year'] == int(year)) & (df['Country Name'] == country)]
    if not year_country_data.empty:
        metrics = year_country_data.drop(columns=['Year', 'Country Name']).to_dict('records')[0]
        return jsonify(metrics)
    else:
        return jsonify({"error": "Year or country not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
