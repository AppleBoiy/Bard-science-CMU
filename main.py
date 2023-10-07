from utils import *


def main():
    token = input("Enter your token: ")
    _bard = warmup_bard(token, prompt_id=2)
    user_name = "คุณ"
    bot_name = "แอนนา"

    print(f"สวัสดี ฉันชื่อ{bot_name} มีอะไรต้องการให้ฉันช่วยมั้ย???")

    while True:
        try:
            input_text = input(f"{user_name}: ")
            print(get_formatted_time())

            if input_text.lower() == "clear" or input_text.lower() == "cls":
                clear_terminal()
                print(f"สวัสดี ฉันชื่อ{bot_name} มีอะไรต้องการให้ฉันช่วยมั้ย???")

            random_sleep()
            typing_animation()

            conversation = f"\n{user_name}: {input_text}"
            response = _bard.get_answer(conversation)['content']

            if response.startswith("Response Error"):
                raise TimeoutError(response)

            response = response.splitlines()
            length_of_conversation = max(map(len, response))

            print("__".center(150, "_"))
            print(f"{bot_name}:")
            for _, line in enumerate(response):
                if len(tab_) + len(line) <= 150:
                    print(tab_, line)
                else:
                    while line:
                        print(tab_, line[:130])
                        line = line[130:]

            print(get_formatted_time().rjust(length_of_conversation + len(tab_)))
            print("__".center(150, "_"))

        except KeyboardInterrupt:
            print("\n\nBye bye")
            break

        except TimeoutError:
            token = input("Enter your token: ")
            _bard = warmup_bard(token, prompt_id=2)
            continue

        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    main()
