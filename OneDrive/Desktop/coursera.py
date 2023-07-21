#  install the AWS SDK for Python (Boto3) and extract the exercise source:
import boto3
import json

responses = []
# Creating a session: AWS management console
aws_mag_console = boto3.session.Session(profile_name ='demo_user')
client = aws_mag_console.client(service_name='comprehend', region_name='us-east-1')


# Load data from the comments of a spesific post on instagram
with open("dataset_instagram-comment-scraper_2023-07-21_21-24-29-960.json", "r") as file:
    data = json.load(file)

# Now 'data' is a list of dictionaries, where each dictionary represents one entry in the JSON file
for entry in data:
    post_url = entry["postUrl"]
    post_id = entry["id"]
    text = entry["text"]
    owner_username = entry["ownerUsername"]
    timestamp = entry["timestamp"]
    likes_count = entry["likesCount"]

    print(f"Post ID: {post_id}")
    print(f"Text: {text}")
    print(f"Likes Count: {likes_count}")
    response = client.detect_sentiment(Text=text, LanguageCode='en')
    responses.append(response['Sentiment'])
    while 0 < likes_count:
        responses.append(response['Sentiment'])
        likes_count -= 1
    print("response:", response['Sentiment'])
    print("-" * 20)

# Example of accessing a specific entry
first_entry = data[0]
print(f"URL of the first post: {first_entry['postUrl']}")
print(responses)


# Final result of the sentiment detection of the post
# Create an empty dictionary to store the counts
value_counts = {}

# Count the occurrences of each unique value
for value in responses:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Print the occurrences of each unique value
for value, count in value_counts.items():
    print(f"{value} responses: {count}")


# If we want to get the sentence from user and apply sentiment detection:
# import boto3
# import tkinter as tk

# root = tk.Tk()
# root.geometry('400x240')
# root.title('Sentiment Analysis')
# textExample = tk.Text(root, height=10)
# textExample.pack()
# def getText():
#     # Creating a session: AWS management console
#     aws_mag_console = boto3.session.Session(profile_name ='demo_user')
#     client = aws_mag_console.client(service_name='comprehend', region_name='us-east-1')
#     result = textExample.get('1.0', 'end')
#     print(result)
#     response = client.detect_sentiment(Text=result, LanguageCode='en')
#     print("response:", response['Sentiment'])
# btnRead = tk.Button(root, height=1, width=10, text='Read', command=getText)
# btnRead.pack()
# # Execute Tkinter
# root.mainloop()