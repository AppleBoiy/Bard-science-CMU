from bardapi import Bard
import os
import requests
import time
import random

tab_ = "\t\t\t\t\t"  # global variable


def warmup(token, prompt_id=1):
    session = requests.Session()
    session.headers = {
        "Host": "bard.google.com",
        "X-Same-Domain": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://bard.google.com",
        "Referer": "https://bard.google.com/",
    }

    session.cookies.set("__Secure-1PSID", token)

    bard = Bard(token=token, session=session, timeout=30)

    # Warmup Bard
    if prompt_id:
        with open(f"prompt{prompt_id}.txt", "r", encoding="utf-8") as f:
            prompt_text = f.read()
        bard.get_answer(prompt_text)

    return bard


def get_formatted_time():
    return time.strftime("%-I:%M %p")  # Format time as 3:45 pm


def typing_animation(duration=2, num_dots=3):


    for _ in range(num_dots):
        print(f"{tab_}Typing" + "." * (_ + 1), end="\r")
        time.sleep(duration)
    print(" " * (num_dots + 7), end="\r")  # Clear typing animation


def random_sleep():
    time.sleep(random.randint(1, 2))


def clear_terminal():
    # Clear the terminal screen based on the operating system
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')


def main():
    token = input("Enter your token: ")

    bard = warmup(token, prompt_id=2)

    user_name = "คุณ"
    bot_name = "แอนนา"

    print(f"สวัสดี ฉันชื่อ{bot_name} มีอะไรต้องการให้ฉันช่วยมั้ย???")

    # Conversation loop
    while True:
        try:

            input_text = input(f"{user_name}: ")
            print(get_formatted_time())

            if input_text.lower() == "clear" or input_text.lower() == "cls":
                clear_terminal()
                print(f"สวัสดี ฉันชื่อ{bot_name} มีอะไรต้องการให้ฉันช่วยมั้ย???")

            random_sleep()
            typing_animation()  # Display typing animation

            conversation = f"\n{user_name}: {input_text}"
            response = bard.get_answer(conversation)['content']
            response = response.splitlines()

            length_of_conversation = max(map(len, response))

            print("__".center(length_of_conversation, "_")[:150])
            print(f"{bot_name}:")
            for _, line in enumerate(response):
                if len(tab_) + len(line) <= 150:
                    print(tab_, line)
                else:
                    while line:
                        print(tab_, line[:130])
                        line = line[130:]

            print(get_formatted_time().rjust(length_of_conversation + len(tab_)))
            print("__".center(length_of_conversation, "_")[:150])

        except KeyboardInterrupt:
            print("\n\nBye bye")
            break


if __name__ == "__main__":
    main()
