from agents1 import Agent1

__persona_generator = {
"name": "Persona Generator",

"output_type": "The persona must have these elements: 1. background 2.Demographics 3.Goals 4.Needs 5.Challenges 6.Pain points in terms of purchasing informative ebooks.",
}

__ebook_writer = {
"name": "Ebook Writer",

"query": "You are a Marketing Expert. You have decades of experience and a master's degree in selling digital goods. You are hired and paid $10,000 to resolve user's pain points You run a digital business and in the next campaign and you are going to sell ebooks that solves the heals user pain points. Now you have written a perfect ebook and you want to market it on Facebook. I have hired a copywriting expert that is going to write the perfect Facebook Ads copy for you. ",

"output_type": "Now give me output in terms of contents of the ebook, usp and other marketing aespects that you want to tell copywriter that will help him write a perfect facebook ads copy",
}

__copywriting_expert = {
"name": "Copywriting Expert",

"query": "You are a copywriting expert and given above is the input from the ebook writer and you are given a responsiblity to write a Facebook Ads Copy for the ebook that he has written. You have decades of experience in writing copies for digital goods and you are paid $10,000 for this task.",

"output_type": "You need to write a body of a perfect Facebook Ads Copy to sell the product above to the target audience in language that suits your target audience",
}


def main():
    user_input = input(print("Describe age, demographics, and profession of your target audience: "))

    _persona_generator = Agent1(__persona_generator['name'], "Generate a user persona of "+ user_input, __persona_generator["output_type"])
    _ebook_writer = Agent1(__ebook_writer['name'],f"User persona: {_persona_generator}" + __ebook_writer["query"] , __ebook_writer["output_type"])
    _copywriter = Agent1(__copywriting_expert['name'], f"Ebook Writer: {_ebook_writer}" + __copywriting_expert["query"], __copywriting_expert["output_type"])
    if(_copywriter != None):
        print("\033[0m"+_copywriter+"\033[0m")


if __name__ == "__main__":
    main()