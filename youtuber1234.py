from googleapiclient.discovery import build#build function is imported from googleclient.discovery module
import pandas as pd

# Set up the YouTube API client
api_key="yourapikey"
youtube = build('youtube', 'v3', developerKey=api_key)#creates an instance of YouTube API client using
#build function.... 'youtube' is the api service required and 'v3' is the version required,the api key we are using
#just authenticates our api request

# Get the comments for a specific video
video_id = "PPgtFMUu-lc"
comments = []
next_page_token = None
while True:#the while loop executes as longs as there are more comments available to retrieve, which is determined
    #by the presence of nextPageToken field in API response 
    response = youtube.commentThreads().list(#youtube.commentThreads() creates a CommentThreads resource object for interacting with commentthread on youtube
        part="snippet",
        videoId=video_id,
        pageToken=next_page_token
    ).execute()
    print("response")
    for i in response:
        print(i)
        # print(i['items'])
        # print(i['nextPageToken'])
    # print(response)
    print("commentthread")
    print(youtube.commentThreads())

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
    if "nextPageToken" in response:
        next_page_token = response["nextPageToken"]
    else:
        break

# Convert comments to a pandas DataFrame and save to a file
df = pd.DataFrame(comments, columns=["comment"])
df.to_csv("D://comments4.csv", index=False)

#the CommentThreads resource object is a part of the YouTube Data API v3 and respresents a collection of
#commands that are associated with a specific video or channel. A CommentThread resource contains info about 
#a top-level comment as well as any replies to that comment, alongwith metadata about each comment such as author 
#timestamp and commenttext,each CommentThread object includes a snippet object that contains basic details of the 
#comment thread, such as the ID of the video or channel being commented upon,id of top-level comment and 
#number of replies to it, the snippet object also includes 'canReply' field, which indicates whether the current user
#is authorized 
# youtube.commentThreads() creates a CommentThreads resource object  for interacting with comment threads on youtube
#.list() is a method of the CommentThreads resource that performs a search for comment threads matching certain criteria, specified in
#the parameters part="snippet" specifies that we want to retrieve the snippet part of each thread which contains information about
#comment text, author and publish date .... pageToken=next_page_token specifies an optional model for pagination. If there are more than 100
#comments in the video, the API will only return the first 100 comments, to retrieve comments from next page, we can use
#nextPageToken value returned in the previous API response as the pageToken value for the next request. This allows us to retrieve all comments in 
#multiple request  ....The execute() method is then called to actually send the API request and return the response. The response contains a list of 
#comment threads for the specified video,along with some additional metadata like the total number of comments and the 'nextPageToken' value for the next stage of
#results if possible  .... The response variable holds API response in JSON format, which is then used to extract the comment text from each comment thread and append
#it to the comments list .... The while True: loop is used to handle pagination, where we keep retrieving the next page of comments until there are no more pages
#the next_page_token variable is used to specify the page token for the next page of results, finally the comments list is converted to a pandas DataFrame and saved to a 
#csv file using to_csv() method of DataFrame. The csv file will contain single-column called 'comments
#containing all comments retrieved from the video
