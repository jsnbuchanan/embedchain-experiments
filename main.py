import os

from dotenv import dotenv_values

from embedchain import App

config = dotenv_values(".env")
os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
app = App()

# Add different data sources
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
app.add("https://www.forbes.com/profile/elon-musk")
# You can also add local data sources such as pdf, csv files etc.
# elon_bot.add("/path/to/file.pdf")

response = app.query("What is the net worth of Elon Musk?")
print(response)