# Recruitment task

Python Intern Task - Web Crawler 
 
Clarence got lost while surfing the internet. Help him find his way out by creating a map of the domain he is on. 
 
Write a function `site_map(url)` that takes a site URL as an argument and creates a mapping of that domain as a Python dictionary. The mapping should contain all the accessible pages within that domain. Every entry should consist of: * key: URL * value: dictionary with: ** site title (HTML `<title>` tag) ** links - set of all target URLs within the domain on the page but without anchor links 
 
Example: Confused? Worry not! Here is an example site with a map. Unzip the `example.zip` file into some directory and enter it. Run the following command `python3 -m http.server`. You are serving a website now! Check if everything is okay by visiting the `http://0.0.0.0:8000` URL. If everything works you can run your program with following parameter and verify if it gives the correct answer. 

# How to use it?

Use function prepare_report() and give name of file, where you have input data.

```
prepare_report('input_file.csv')
```

# Additional information

Function do something more than just change the data. I thought that good idea will be to :
1. Add option to choose output file name, default is 'Report YYYY-MM-DD', where date is this day.
2. Add option to choose if we want headers in output file for more readability.
3. Check if input file has headers.
