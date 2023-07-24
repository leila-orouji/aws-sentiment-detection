
#*********
# Sentiment detection of the user based on Detect-sentiment API from AWS
#*********

#  install the AWS SDK for Python (Boto3) and extract the exercise source:
import boto3
import json
import tkinter as tk


# Creare a window to get sentence from the user 
root = tk.Tk()
root.geometry('400x240')
root.title('Sentiment Analysis')
textExample = tk.Text(root, height=10)
textExample.pack()
def getText():
    # Define a User in our IAM AWS credential - Here is "demo_user"
    # Creating a session: AWS management console
    aws_mag_console = boto3.session.Session(profile_name ='demo_user')
    client = aws_mag_console.client(service_name='comprehend', region_name='us-east-1')
    result = textExample.get('1.0', 'end')
    print(result)
    response = client.detect_sentiment(Text=result, LanguageCode='en')
    print(response['Sentiment'])

# Click on the 'Read' button to get the sentence(s) from user
btnRead = tk.Button(root, height=1, width=10, text='Read', command=getText)
btnRead.pack()
# Execute Tkinter
root.mainloop()
