import twitter
#enter your consumer key,secret and access token secret,key in below function as parameters 

api=twitter.Api(consumer_key='Hc89GpUxM0DVkTWdGKdw',consumer_secret='ZfkARmEJKFsEIFoAqqt5Ih85NMr3DKhgcOQ4eO3N9k',access_token_key='635651955-t6B4LBLptIjNIxEKtBS6fIKek2mQI0FE3XJE2zzf',access_token_secret='jt0SaO89Ay6JOilmOhzHmEHer84vU88StHvUWJz7s') 

#now using PostUpdate method of the api we can use to post an update on twitter account 

status = api.PostUpdate('My first tweet using python..:):):):)') 
wait = input("PRESS ENTER TO CONTINUE.")
