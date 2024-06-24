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

__dropshipping_expert = {
"name": "Dropshipping Expert",

"query": "You are a dropshipping expert with decades of experience. You promised me to give your best service becuase I am paying you $10,000 for your service and given above is the persona of your target audience. Because you are drop shipping expert you are going to sell the product above to the target audience. The product you are selling is: ",

"output_type": "You have to tell the copywriter about the product, its USP, and the target audience for him to write a perfect Facebook Ads Copy to sell the product above. Also let him know what would be the best language for your target audience.",
}

__copywriting_expert = {
"name": "Copywriting Expert",

"query": "You are a copywriting expert and given above is the input from the ebook writer and you are given a responsiblity to write a Facebook Ads Copy for the ebook that he has written. You have decades of experience in writing copies for digital goods and you are paid $10,000 for this task.",

"output_type": "You need to write a body of a perfect Facebook Ads Copy in less than 120 words to sell the product above to the target audience in language that suits your target audience",
}

def expert_agent(index, persona, product):
    if index == 1:
        return Agent1(__dropshipping_expert['name'], f"Persona: {persona}" + __dropshipping_expert["query"] + product, __dropshipping_expert["output_type"])

    elif index == 2:
        return Agent1(__ebook_writer['name'], f"Persona: {persona}" + __ebook_writer["query"], __ebook_writer["output_type"])
    else:
        return None


def main():
    user_input = input(print("Describe age, demographics, and profession of your target audience:\n"))
    index = input(print("What do you want to use this for?:\n1.Drop shipping\n2.Digital Goods/Ebook\n3. Course"))
    product = input(print("What product are you selling?:\n(type 0 if you didn't choose drop shipping)\n"))

    _persona_generator = Agent1(__persona_generator['name'], "Generate a user persona of "+ user_input, __persona_generator["output_type"])
    _expert_agent = Agent1(__dropshipping_expert['name'], f"Persona: {_persona_generator}" + __dropshipping_expert["query"] + product, __dropshipping_expert["output_type"])
    _copywriter = Agent1(__copywriting_expert['name'], f"Expert said:\n{_expert_agent}" + __copywriting_expert["query"], __copywriting_expert["output_type"])
    if(_copywriter != None):
        print("\033[0m"+_copywriter+"\033[0m")


if __name__ == "__main__":
    main()