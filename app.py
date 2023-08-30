from tkinter import *
from bard import get_response, bot_name
from token_1 import api_token
from tkinter import font

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "THSarabunNew"
FONT_BOLD = "DilleniaUPC 22 bold"


class ChatApplications:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()
    
    

    def _setup_main_window(self):

        self.window.title("CS-Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=800, height=900, bg=BG_COLOR)

        # Top Label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=(FONT_BOLD), pady=20)
        head_label.place(relwidth=1)

        # Divider
        line = Label(self.window, width=750, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text 
        self.text_widget = Text(self.window, width=20, height=5, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=(FONT, 20), padx=10, pady=10)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bot Label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Msg Box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=(FONT,20))
        self.msg_entry.place(relwidth=0.75, relheight=0.09, rely=0.01, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send Button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.09, relwidth=0.18)


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "User")

    def _insert_message(self, msg, user_name):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{user_name}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg1, api_token)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplications()
    app.run()