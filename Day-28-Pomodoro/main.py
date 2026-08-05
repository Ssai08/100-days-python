from tkinter import Button, Label, Tk, Canvas
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# WORK_SEC = WORK_MIN * 60
# SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
# LONG_BREAK_SEC = LONG_BREAK_MIN * 60
WORK_MIN = 5 # For testing, these are seconds
SHORT_BREAK_MIN = 2 # For testing, these are seconds
LONG_BREAK_MIN = 10 # For testing, these are seconds
WORK_SEC = WORK_MIN #* 60
SHORT_BREAK_SEC = SHORT_BREAK_MIN #* 60
LONG_BREAK_SEC = LONG_BREAK_MIN #* 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps = 0
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    start_button.config(state="disabled")

    if reps %8 == 0:
        count_down(LONG_BREAK_SEC)
        timer_label.config(text="Break", fg=RED)
    elif reps %2 != 0:
        count_down(WORK_SEC)
        timer_label.config(text="Work", fg=GREEN)
    elif reps %2 == 0:
        count_down(SHORT_BREAK_SEC)
        # Add a checkmark after a work session is complete
        work_sessions = reps // 2
        marks = "✔" * work_sessions
        check_mark.config(text=marks)
        timer_label.config(text="Break", fg=PINK)
    print(reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + f"{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(height=300,width=224,bg=YELLOW,highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100,150,image=pomodoro_img)
timer_text = canvas.create_text(100,160,text="00:00",fill="white",font=(FONT_NAME,36,"bold"))
canvas.grid(row=1,column=1)



timer_label = Label(text="Timer", font=(FONT_NAME,26,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

check_mark = Label(font=(FONT_NAME,18,"bold"),fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)

window.mainloop()