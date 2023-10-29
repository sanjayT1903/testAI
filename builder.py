import streamlit as st

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as palm
palm.configure(api_key="AIzaSyCHHmecpNDam9V3qPC52FbcBgHkhLnSOeA")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":4},{"category":"HARM_CATEGORY_TOXICITY","threshold":4},{"category":"HARM_CATEGORY_VIOLENCE","threshold":4},{"category":"HARM_CATEGORY_SEXUAL","threshold":4},{"category":"HARM_CATEGORY_MEDICAL","threshold":4},{"category":"HARM_CATEGORY_DANGEROUS","threshold":4}],
}
input = 'I mean these applications for translating any pictures. Like google tranlste.'
prompt = f"""Keep in mind these are old social media comments, You are to rate comments from a 1-10, where 10 is the worst thing a human could say while 1 is normal statements. Anything to be racially offensive for sexual should be above 5 while most other things should be lower!
input: Out of 1-10 where 10 is the most inappropriate statement 1 being least - @turtleseal Next time I got a post abt the Swim Team I’ll add it
sanjay_thasma
Ahhhhhhh
Gay
Group A messed up
lol alex looks gay
output: 9 - The term gay in this context can be seen as highly offensive
input: Out of 1-10 where 10 is the most inappropriate statement 1 being least - @turtleseal Next time I got a post abt the Swim Team I’ll add it
sanjay_thasma
Eating poop tastes so good
You are weird
output: 5- Eating poop is an inappropriate for talking but not necessarily horrible
input: I would love to see you shirtless
output: 4 - It is normal to want to see someone shirtless but it is a bit inappropriate to say out loud and can make people uncomfortable
input: I hate black people
output: 10 - Hate speech is not tolerated
input: sanjay_thasma
Ahhhhhhh
Gay
Group A messed up
lol alex looks gay
output: 8- Gay is a derogatory term and is offensive to a lot of people
input: I love eating muffins
output: 1 - There is nothing wrong with this statement
input: Am I the only one who noticed how much more fair she looks in the sign. Lol
output: 2 - It is not appropriate to comment on someone's skin color.
input: Damn 🔥🔥🔥🔥🔥
output: 3 - It is not appropriate to objectify a person and make them feel like a piece of meat
input: I want to see you naked
output: 7 - It is normal to want to see someone naked but it is a bit inappropriate to say out loud
input: @shaggy856 stop hating cuz u too lazy and wanna stay broke.
output: 5 - This is a personal attack and is not appropriate
input: Why u playing on a phone. Weirdo. Play on anything but that and i will respect u more 
output: 5 - calling someone a weirdo is not appropriate
input: So how many of those girls are yours. 🥵🥵🥵
output: 8 - It is not appropriate to objectify a person and make them feel like a piece of meat
input: When you start wearing silk jackets, thats going to be the end of fashion. Nothing is more respectable than silk clothes 
output: 2 - There is nothing wrong with this statement
input:  can’t believe you called them your boys. I would be ashamed. Smh my head 
output: 4 - There is nothing wrong with this statement
input: Fix the description on this post. Colleges don’t tolerate bad language 
output: 3 - It is not appropriate to use profanity in a professional setting
input: A is crazy 
output: 2 - There is nothing wrong with this statement
input: Always pimpin. #goneclear 
output: 1 - There is nothing wrong with this statement
input: @turtleseal U think I can post the infamous chair photo
sanjay_thasma
output: 1 - There is nothing wrong with this statement
input: hey nigga
output: 10 - This is a racial slur and is offensive
input: I want to show u my m-16 peronsally
output: 10 - This is a threat and is not tolerated
input: kys
output: 9 - Telling someone to kill themselves is a horrible thing to say
input: go back to china where u belong
output: 9 - This is a racial slur and is offensive
input: I will suck you off
output: 10 - Sexual harassment is not tolerated
input: {input}
output:"""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)