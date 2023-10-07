import requests
from bardapi import Bard


def warmup_bard(token, prompt_id=1):
    session = requests.Session()
    session.headers = {
        "Host": "bard.google.com",
    }

    session.cookies.set("__Secure-1PSID", token)

    bard = Bard(token=token, session=session, timeout=30)

    if prompt_id:
        with open(f"../data/prompt{prompt_id}.txt", "r", encoding="utf-8") as f:
            prompt_text = f.read()
        bard.get_answer(prompt_text)

    return bard
