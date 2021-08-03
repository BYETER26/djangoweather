from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=15DF12E8-DE04-4407-A835-732669547BE2")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) The air quality is considered satisfactory."
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100) The air quality is acceptable."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150) Older adults and children are at a great risk."
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200) Every one may experience health effects."
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300) Health alert."
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301-500) Health warning of emergency conditions."
			category_color = "hazardous"

		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description,
			'category_color'      : category_color
			})

	else:
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=87501&distance=25&API_KEY=15DF12E8-DE04-4407-A835-732669547BE2")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) The air quality is considered satisfactory."
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100) The air quality is acceptable."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150) Older adults and children are at a great risk."
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200) Every one may experience health effects."
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300) Health alert."
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301-500) Health warning of emergency conditions."
			category_color = "hazardous"

		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description,
			'category_color'      : category_color
			})


def about(request):
	return render(request, 'about.html', {})



# elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
# 	category_description = "(101-150) Older adults and children are at a great risk."
# 	category_color = "usg"
#    elif api[0]['Category']['Name'] == "Unhealthy":
# 	category_description = "(151-200) Every one may experience health effects."
# 	category_color = "unhealthy"
# elif api[0]['Category']['Name'] == "Very Unhealthy":
# 	category_description = "(201-300) Health alert."
# 	category_color = "veryunhealthy"
# elif api[0]['Category']['Name'] == "Hazardous":
# 	category_description = "(301-500) Health warning of emergency conditions."
# 	category_color = "hazardous"
