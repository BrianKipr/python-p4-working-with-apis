import requests
import json

class GetPrograms:

    def get_programs(self):
        # Replace 'https://example.com/api' with the actual URL of the API you want to fetch data from
        api_url =  "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Check for any HTTP errors

            return response.text  # Return the JSON response as a string

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None

    def program_school(self):
        programs_list = []
        api_data = self.get_programs()

        if api_data is not None:
            programs = json.loads(api_data)
            for program in programs:
                programs_list.append(program.get("agency"))

        return programs_list

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
