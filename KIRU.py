import json
from difflib import get_close_matches

def Import_response(file_path:str)-> dict:
    with open(file_path,'r') as file:
        data: dict = json.load(file)
    return data


def Save_response(file_path:str,data:dict):
    with open(file_path,'w') as file:
        json.dump(data,file,indent=2)


def Matching(user_question:str,question:list[str])->str or None:
    combination:list=get_close_matches(user_question,question,n=1,cutoff=0.90)
    return combination[0] if combination else None

def Answer(question:str,Data_base:dict)->str or None:
    for q in Data_base["questions"]:
        if q["question"]==question:
            return q["answer"]



def chat_bot():
    Data_base:dict = Import_response('Data_base.json')

    while True:
        user: str = input('You : ')

        if user.lower()=='quit':
            break

        perfect_match:str or None = Matching(user,[q["question"] for q in Data_base["questions"]])

        if perfect_match:
            old_answer:str=Answer(perfect_match,Data_base)
            print(f'KIRU: {old_answer}')

        else:
            print('KIRU: I don\'t know how to respond, Can you Teach Me?')
            new_answer:str = input('Can you type the answer or Type "skip" to skip: ')

            if new_answer.lower() != 'skip':
                Data_base["questions"].append({"question":user,"answer": new_answer})
                Save_response('Data_base.json',Data_base)
                print('KIRU: Thank You for teaching me <3 !!!')

if __name__ == '__main__':
    chat_bot()