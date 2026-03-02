tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet" : 100,
    "hashtag" : ["Data1","Data2","Data3"]

}
print(tweet)

tweet["hashtag"][1] = ["Alterado"]
print(tweet)
print(tweet.values)
print(tweet.keys)
print(tweet.items)