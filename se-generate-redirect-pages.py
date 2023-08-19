import requests
import os
import json

URL = "https://github.com/apple/swift-evolution/tree/main/proposals"
BASE_URL = "https://github.com/apple/swift-evolution/blob/main/"

response = requests.get(URL)
data = json.loads(response.text)

# Create a dictionary to map proposal numbers to their URLs
proposal_map = {}
for item in data['payload']['tree']['items']:
    if item['contentType'] == 'file' and item['path'].endswith('.md'):
        code = item['name'].split('-')[0]
        href = BASE_URL + item['path']
        proposal_map[code] = href

# Now let's generate the HTML file with embedded JavaScript
filename = 'index.html'
with open(filename, 'w') as file:
    file.write("""<html>
<head>
    <script type="text/javascript">
        function getParameterByName(name, url) {
            if (!url) url = window.location.href;
            name = name.replace(/[\[\]]/g, "\\$&");
            var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
                results = regex.exec(url);
            if (!results) return null;
            if (!results[2]) return '';
            return decodeURIComponent(results[2].replace(/\+/g, " "));
        }

        window.onload = function() {
            let seCode = getParameterByName('se');
            let redirectMap = """ + json.dumps(proposal_map) + """;

            if (seCode) {
                if (redirectMap[seCode]) {
                    window.location.href = redirectMap[seCode];
                }
                else {
                    document.getElementById("error_message").innerHTML = "Invalid or missing Swift Evolution proposal code: &quot;" + seCode + "&quot;";
                } 
            }
            else {
                document.getElementById("main_text").style.display = "block";
            }
        }
    </script>
</head>
<body>
    <div id="error_message"></div>
    <div id="main_text" style="display: none;">

        <h2>professional experience</h2>

        Over 20 years software engineering; 14 of those are mobile focused, with the last 10 specialising in iOS as a contractor.

        Equally happy working in development teams or being the solo iOS developer expert with a client. I'm fortunate to have worked with some great clients in both the private and public sector.

        Swift, Objective C, Python, Java, Golang, C, some C++ and C#. And 6502 :)

        <h2>education</h2>

        BSc (Hons) Computer Science, Edinburgh 1992 - 96

        <h2>see me online</h2>

        <a href='https://uk.linkedin.com/in/alex-hunsley-385937'>LinkedIn</a>

        <p/>

        <a href="https://stackoverflow.com/users/348476/occulus"><img src="https://stackoverflow.com/users/flair/348476.png" width="208" height="58" title="profile for occulus at Stack Overflow"></a>

        <h2>current projects</h2>

        learning Golang; looking into data science; <a href="https://github.com/alexhunsley/tray-racer">tray racer</a>, a toy ray tracer.

        <h2>programming contests</h2>

        My <a href="https://github.com/alexhunsley/aoc-2019">Advent of Code 2019</a> in Golang

        <h2>other interests</h2>

        Sometimes I'm mentoring more junior developers in my own time.

        I exhibit at <a href="https://www.colony-of-artists.com/">Colony of Artists</a> every year (doing photography and digital media).

        <a href="https://www.instagram.com/alexhunsleyart">Some of my art and creations on instagram</a>

        <p/>

        Drumming: Beltane Fire Society and ex-<a href="https://www.harbingersdrumcrew.com/#introduction">Harbingers Drum Crew</a>.

        <p/>

        Ringing church bells (<a href="https://bb.ringingworld.co.uk/search.php?ringer=hunsley">see my activity</a>) - physical exercise and group theory don't normally meet this way

        <p/>

    </div>


</body>
</html>
""")

print(f"File generated as {filename}.")
