import requests

url = 'https://web.archive.org/web/timemap/json?url=go-60de6c82-be11-98e1-4d6c-c65a234eee95.disney.io&matchType=prefix&collapse=urlkey&output=json&fl=original&filter..&limit=9999999&_=1702928796739'

try:
    response = requests.get(url)
    data = response.json()

    with open('output.sql', 'w') as sql_file:
        # Create the table
        sql_file.write('''
            CREATE TABLE IF NOT EXISTS disney (
                id INTEGER PRIMARY KEY,
                url TEXT
            );
        ''')

        # Insert URLs into the 'disney' table
        for entry in data:
            sql_file.write(f"INSERT INTO disney (url) VALUES ('{entry[0]}');\n")

    print("SQL commands successfully written to 'output.sql'.")

except Exception as e:
    print(f"An error occurred: {e}")
