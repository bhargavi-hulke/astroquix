import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import random
import time
import PIL
from PIL import Image, ImageTk
from itertools import cycle

window = tk.Tk()
window.title("astroquix")
window.geometry("1200x800")
window.configure(bg='black')
window.resizable(True, True)

#dual gif switching background 

class AnimatedGifBackground(tk.Label):
    def __init__(self, master, gif_path):
        super().__init__(master,bg='black')
        self.frames = []
        self.path = gif_path
        self.cycle = None
        self.is_playing = False
        self.duration = 100 # default duration
        self.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    def load_gif(self):
        self.frames = []
        try:
            img = PIL.Image.open(self.path)
            self.duration = max(img.info.get('duration', 100), 50)
            frame_count = 0
            while True:
                try:
                    frame = img.copy().resize((1200, 800), PIL.Image.LANCZOS)
                    self.frames.append(ImageTk.PhotoImage(frame))
                    img.seek(img.tell() + 1)
                    frame_count += 1
                    if frame_count > 30:  # Prevent memory explosion
                        break
                except EOFError:
                    break
            self.cycle = cycle(self.frames)
            print(f"✅ Loaded: {self.path} ({len(self.frames)} frames)") #for debugging
        except Exception as e:
            print(f"❌ GIF failed {self.path}: {e}")
    
    def play(self):
        if self.frames and self.is_playing and self.cycle:
           self.configure(image=next(self.cycle))
           self.after(self.duration, self.play)
           
    def start(self):
        self.load_gif()
        self.is_playing = True
        self.play()
    
    def stop(self):
        self.is_playing = False
        
#define two backgrounds 
welcome_bg =  AnimatedGifBackground(window, "welcome_bg.gif") #calm bg for welcome
quiz_bg = AnimatedGifBackground(window, "quiz_bg.gif") # rapid bg for quiz

#Fetch the background 
def quiz_background():
    welcome_bg.stop()
    welcome_bg.place_forget()
    quiz_bg.place_forget() # Clear previous placement
    quiz_bg.place(x=0, y=0, relwidth=1, relheight=1)
    quiz_bg.lift()  # Bring to front
    quiz_bg.start()
    question_label.lift()
    score_label.lift()      
    timer_label.lift()
    for b in buttons:   
        b.lift()                
    restart_button.lift()
    
    
def welcome_background():
    quiz_bg.stop()
    quiz_bg.place_forget()
    welcome_bg.place_forget()  # Reset position
    welcome_bg.place(x=0, y=0, relwidth=1, relheight=1)
    welcome_bg.lift()  # BRING TO FRONT
    welcome_bg.start()
    # Send welcome UI to front
    label.lift()
    start_button.lift()
    exit_button.lift()
    score_label.lift()      
    timer_label.lift()               
    restart_button.lift()

   
# Quiz data
quiz_data = [
    {
        "question": "What is the name of the process by which stars produce energy?",
        "options": ["Nuclear Fusion", "Nuclear Fission", "Combustion", "Radiation"],
        "correct answer": "Nuclear Fusion"
    },
    {
        "question": "Which planet in our solar system has the longest day (slowest rotation)?",
        "options": ["Mercury", "Venus", "Earth", "Mars"],
        "correct answer": "Venus"
    },
    {
        "question": "What is the name of the boundary around a black hole beyond which nothing can escape?",
        "options": ["Event Horizon", "Singularity", "Photon Sphere", "Accretion Disk"],
        "correct answer": "Event Horizon"
    },
    {
        "question": "What is the name of the largest volcano in the solar system, located on Mars?",
        "options": ["Olympus Mons", "Mauna Kea", "Mount Everest", "Elysium Mons"],
        "correct answer": "Olympus Mons"
    },
    {
        "question": "What is the name of the phenomenon where a star explodes at the end of its life?",
        "options": ["Black Hole", "Supernova", "Nebula", "Pulsar"],
        "correct answer": "Supernova"
    },
    {
        "question": "What is the name of the spacecraft that first landed humans on the Moon?",
        "options": ["Apollo 11", "Voyager 1", "Sputnik 1", "Hubble"],
        "correct answer": "Apollo 11"
    },
    {
        "question": "What is the name of the region in space where gravity is so strong that not even light can escape?",
        "options": ["Neutron Star", "White Dwarf", "Black Hole", "Quasar"],
        "correct answer": "Black Hole"
    },
    {
        "question": "What is the name of the largest moon in the solar system, orbiting Jupiter?",
        "options": ["Titan", "Europa", "Ganymede", "Callisto"],
        "correct answer": "Ganymede"
    },
    {
        "question": "What is the name of the theory that explains the origin of the universe?",
        "options": ["Big Bang Theory", "Steady State Theory", "String Theory", "Relativity Theory"],
        "correct answer": "Big Bang Theory"
    },
    {
        "question": "What is the name of the constellation that contains the North Star (Polaris)?",
        "options": ["Orion", "Ursa Major", "Ursa Minor", "Cassiopeia"],
        "correct answer": "Ursa Minor"
    },
    {
        "question": "What is the name of the galaxy that will collide with the Milky Way in about 4.5 billion years?",
        "options": ["Andromeda", "Triangulum", "Whirlpool", "Sombrero"],
        "correct answer": "Andromeda"
    },
    {
        "question": "What is the name of the first planet discovered using a telescope?",
        "options": ["Uranus", "Neptune", "Saturn", "Jupiter"],
        "correct answer": "Uranus"
    },
    {
        "question": "What is the name of the brightest planet in the night sky?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct answer": "Venus"
    },
    {
        "question": "What is the name of the phenomenon where the Earth passes between the Sun and the Moon, casting a shadow on the Moon?",
        "options": ["Solar Eclipse", "Lunar Eclipse", "Transit", "Aurora"],
        "correct answer": "Lunar Eclipse"
    },
    {
        "question": "What is the name of the spacecraft that explored Pluto in 2015?",
        "options": ["Voyager 1", "New Horizons", "Cassini", "Curiosity"],
        "correct answer": "New Horizons"
    },
    {
        "question": "What is the name of the star at the center of our solar system?",
        "options": ["Sirius", "Alpha Centauri", "Polaris", "Sun"],
        "correct answer": "Sun"
    },
    {
        "question": "What is the name of the largest asteroid in the asteroid belt?",
        "options": ["Ceres", "Vesta", "Pallas", "Eros"],
        "correct answer": "Ceres"
    },
    {
        "question": "What is the name of the phenomenon where charged particles from the Sun interact with Earth's atmosphere, creating colorful lights?",
        "options": ["Aurora", "Supernova", "Meteor Shower", "Solar Flare"],
        "correct answer": "Aurora"
    },
    {
        "question": "What is the name of the first human-made object to leave the solar system?",
        "options": ["Voyager 1", "Pioneer 10", "New Horizons", "Cassini"],
        "correct answer": "Voyager 1"
    },
    {
        "question": "What is the name of the dwarf planet located in the Kuiper Belt?",
        "options": ["Pluto", "Eris", "Haumea", "Makemake"],
        "correct answer": "Pluto"
    },
    {
        "question": "What is the closest star to Sun?",
        "options": ["Proxima Centauri", "Sirius", "Alpha Centauri A", "Barnard's Star"],
        "correct answer": "Proxima Centauri"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct answer": "Mars"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Neptune"],
        "correct answer": "Jupiter"
    },
    {
        "question": "What is the name of the first artificial satellite launched into space?",
        "options": ["Apollo 11", "Vostok 1", "Sputnik 1", "Explorer 1"],
        "correct answer": "Sputnik 1"
    },
    {
        "question": "What is the name of the phenomenon where the Moon passes between the Earth and the Sun?",
        "options": ["Lunar Eclipse", "Solar Eclipse", "Transit", "Occultation"],
        "correct answer": "Solar Eclipse"
    },
    {
        "question": "Which planet has the most extensive ring system?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "correct answer": "Saturn"
    },
    {
        "question": "What is the name of the galaxy that contains our solar system?",
        "options": ["Andromeda", "Milky Way", "Whirlpool", "Sombrero"],
        "correct answer": "Milky Way"
    },
    {
        "question": "What is the term for a group of stars that form a recognizable pattern?",
        "options": ["Galaxy", "Cluster", "Constellation", "Nebula"],
        "correct answer": "Constellation"
    },
    {
        "question": "What is the name of the largest moon of Saturn?",
        "options": ["Titan", "Rhea", "Iapetus", "Enceladus"],
        "correct answer": "Titan"
    },
    {
        "question": "What is the name of the force that keeps planets in orbit around the Sun?",
        "options": ["Electromagnetism", "Nuclear Force", "Gravity", "Friction"],
        "correct answer": "Gravity"
    },
    {
        "question": "Which planet is known for its extreme winds and storms?",
        "options": ["Venus", "Mars", "Neptune", "Uranus"],
        "correct answer": "Neptune"
    },
    {
        "question": "What is the term for a small rocky body that orbits the Sun, primarily found in the asteroid belt?",
        "options": ["Asteroid", "Comet", "Meteor", "Planet"],
        "correct answer": "Asteroid"
    },
    {
        "question": "What is the name of the region of space beyond Neptune that contains many small icy bodies?",
        "options": ["Asteroid Belt", "Kuiper Belt", "Oort Cloud", "Heliosphere"],
        "correct answer": "Kuiper Belt"
    },
    {
        "question": "What was the name of the first living creature sent into space?",
        "options": ["Belka", "Laika", "Ham", "Yuri"],
        "correct answer": "Laika"
    },
    {
        "question": "Which Indian space agency is known for its successful Mars Orbiter Mission?",
        "options": ["NASA", "ESA", "ISRO", "Roscosmos"],
        "correct answer": "ISRO"
    },
    {
        "question": "What does NASA stand for?",
        "options": ["National Aeronautics and Space Administration", "National Association of Space Astronauts", "North American Space Agency", "National Aerospace and Science Agency"],
        "correct answer": "National Aeronautics and Space Administration"
    },
    {
        "question": "What is a cubesat?",
        "options": ["A type of large satellite", "A small, cube-shaped satellite", "A satellite used for deep space exploration", "A satellite that orbits the Moon"],
        "correct answer": "A small, cube-shaped satellite"
    },
    {
        "question": "What is the Crab Nebula?",
        "options": ["A type of star", "A planetary nebula", "The remnant of a supernova explosion", "A galaxy"],
        "correct answer": "The remnant of a supernova explosion"
    },
    {
        "question": "Which ISRO satellite was launched to study the Moon?",
        "options": ["Mangalyaan", "Chandrayaan-1", "Astrosat", "GSAT"],
        "correct answer": "Chandrayaan-1"
    },

     {"question": "How many planets are there in our solar system?",
       "options": ["7", "8", "9", "10"], 
       "correct answer": "8"},

    {"question": "Which is the largest planet from the inner planets of our solar system?",
      "options": ["Mars", "Venus", "Mercury", "Earth"], "correct answer": "Earth"},

    {"question": "What gas makes up most of the Sun?", 
     "options": ["Oxygen", "Hydrogen", "Helium", "Carbon"], 
     "correct answer": "Hydrogen"},

    {"question": "Which planet has a Great Red Spot?",
      "options": ["Saturn", "Jupiter", "Uranus", "Venus"], 
      "correct answer": "Jupiter"},

     {"question": "Which planet is tilted on its side?", 
      "options": ["Earth", "Mars", "Uranus", "Saturn"], 
      "correct answer": "Uranus"},

    {"question": "What is a shooting star actually?",
      "options": ["Falling star", "Meteor", "Comet", "Asteroid"],
        "correct answer": "Meteor"},

    {"question": "Which is the smallest planet in our solar system?", 
     "options": ["Mercury", "Mars", "Venus", "Pluto"], 
     "correct answer": "Mercury"},

    {"question": "What is the name of the first man in space?",
      "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"],
      "correct answer": "Yuri Gagarin"},

     {"question": "How long does it take light from the Sun to reach Earth?",
       "options": ["8 seconds", "8 minutes", "8 hours", "8 days"],
       "correct answer": "8 minutes"},

     {"question": "Which moon is known for its subsurface ocean?", 
      "options": ["Phobos", "Europa", "Deimos", "Rhea"],
      "correct answer": "Europa"},

     {"question": "What is a light-year?",
       "options": ["Time unit", "Distance unit", "Speed unit", "Mass unit"],
       "correct answer": "Distance unit"},

     {"question": "What causes seasons on Earth?",
       "options": ["Distance from Sun", "Earth's tilt", "Moon's orbit", "Sun's rotation"], 
       "correct answer": "Earth's tilt"},

     {"question": "What is the surface of the Sun called?",
       "options": ["Core", "Photosphere", "Corona", "Chromosphere"], 
       "correct answer": "Photosphere"},

    {"question": "Which of these is rover that was sent on Mars?",
      "options": ["Voyager", "Curiosity", "Pioneer", "Cassini"], 
      "correct answer": "Curiosity"},

     {"question": "Which constellation looks like a hunter?",
       "options": ["Ursa Major", "Orion", "Cassiopeia", "Draco"], 
       "correct answer": "Orion"}
]

# Global variables
current_round=0
current_question = 0
score = 0
questions_list = []
round_history=[]

#function to 10 random questions
def generate_fair_questions():
    global current_round, round_history  # RNG is seeded in start_quiz() for time-based randomness;
    # no re-seed here to avoid predictable repeats.
    
    # Method: Full shuffle ensures even coverage of quiz data
    shuffled = quiz_data[:]
    random.shuffle(shuffled)
    selected = shuffled[:10]
    round_history.append([id(q) for q in selected])
    if len(round_history) > 5:  # Keep last 5 rounds
        round_history.pop(0)
    current_round += 1
    print(f"Round {current_round}: Questions loaded") # Debug
    return selected

#Function to load questions
def load_question():
    global current_question, score,questions_list
   
    
    if not questions_list or current_question >= len(questions_list):
        questions_list = generate_fair_questions()
        current_question = 0
        score = 0

    # Load and display the current question 
    question_data = questions_list[current_question]
    question_label.config(text=question_data.get("question", ""))
    options = question_data.get("options", []).copy()
    random.shuffle(options)

    for i in range(len(buttons)):
     if i < len(options):
      buttons[i].config(text=options[i], state="normal",
          command=(lambda opt=options[i]: disable_opt_buttons(opt)))
      buttons[i].pack(pady=5)
     else:
        buttons[i].config(text="", state="disabled", command=lambda: None)
        buttons[i].pack_forget()# hide unused buttons
    

# function to check answer
def check_ans(selected_option):
   
    global current_question, score
    if current_question >= len(questions_list):
     return
    question_data = questions_list[current_question]
    correct_answer = question_data.get("correct answer")

    if selected_option == correct_answer:
        score += 1
        update_score_label()
    
    else:
        messagebox.showinfo("Warning!", f" wrong manoeuvre cap'n ! \n - right button was: {correct_answer}")

    # move to next question
    current_question += 1
    if current_question < len(questions_list):
        load_question()
        restart_button.pack_forget()
        return

    # Quiz finished 
    stop_timer()
    welcome_background()
    time_taken = 60-timer_seconds
    if score >= 8:
        messagebox.showinfo("Stage Completed", f"Your score: {score}/{10}\n you got it in {time_taken}s,\n ready for beyond this one?")
    elif 5 <= score < 8:
        messagebox.showinfo("Well done!", f" Your score: {score}/{10},\n woahhh! that was close! you got it in {time_taken}s\n you've escaped the blackhole!")
    else:
        messagebox.showinfo("Try Again!", f" Your score: {score}/{10},\n you did well in {time_taken}s but,\n uhh ohh!! you were caught in a blackhole!")

    # hide option buttons and show restart button
    for b in buttons:
        b.pack_forget()
    restart_button.pack(pady=20)
    exit_button.pack(pady=20)
   
    
def disable_opt_buttons(selected_option):
    for b in buttons:
        try:
            b.config(state="disabled")
        except Exception:
            pass
    check_ans(selected_option)


# Function to start the quiz 
def start_quiz():
    global current_question, score,questions_list
    current_question = 0
    score = 0
    start_button.pack_forget()
    restart_button.pack_forget()
     # Seeding the RNG with current time for better per-round randomness
    random.seed(time.time())
    question_label.pack(pady=20)
    questions_list = generate_fair_questions() # Fresh random set
    quiz_background()#switching to quiz bg

    for button in buttons:
        button.pack(pady=5)  
    hide_welcome()
    update_score_label()
    start_timer()
    load_question()

# Welcome page
label = tk.Label(window, text="Welcome aboard space explorer! \n Strap in for a journey into the cosmos,and \n Find out how much you know about the universe!!", font=(tkFont.Font(family="Orbitron", size=18, weight="bold")),bg="black",fg="white", wraplength=500)
label.pack(pady=20)

def hide_welcome():
    label.pack_forget()
    button.pack_forget()
    
#Start quiz button
start_button = tk.Button(window, text="Hell Yeah!! Let's go!!", font=(tkFont.Font(family="Orbitron", size=18)),bg="darkgreen",fg="white",relief="raised", bd=4, command=start_quiz)
start_button.pack(pady=20)

# Restart button (initially hidden) — reuses start_quiz
restart_button = tk.Button(window, text="Restart Quiz", font=(tkFont.Font(family="Orbitron", size=18)),bg="darkgreen",fg="white",relief="raised", bd=4, command=start_quiz)

#exit button code
def exit_app():
     if messagebox.askyesno("WARNING!", "Are you sure you want to eject?"):
        window.destroy()

# Exit button
exit_button = tk.Button(window, text="Meh...not in the Mood -_-", font=(tkFont.Font(family="Orbitron", size=18)),bg="black",fg="orange",relief="raised", bd=4, command=exit_app)
exit_button.pack(pady=20)

# Buttons for options
buttons = []
for i in range(4):
    button = tk.Button(window, text="", font=("Arial", 14), fg="white", bg="#1a1a3e",relief="raised", bd=3, activebackground="#181842")
    buttons.append(button)

# Question label
question_label = tk.Label(window, text="", font=("Arial", 16),bg="#1a1a3e",fg="white", wraplength=700)
question_label.pack(pady=20)

#score label
score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 12),fg="gold", bg="black")
score_label.pack()

# Timer label (counts down from 60 seconds)
timer_seconds = 60
timer_id = None
timer_label = tk.Label(window, text=f"Time: {timer_seconds}s", font=("Arial", 12),bg="black",fg="powderblue")
timer_label.pack()

def update_score_label():
    score_label.config(text=f"Score: {score}")


def timer_tick():
    #Handle one tick of the countdown timer
    global timer_seconds, timer_id
    timer_seconds -= 1
    # update text and color
    timer_label.config(text=f"Time: {timer_seconds}s")
    if timer_seconds <= 10:
        timer_label.config(fg="red")
    else:
        timer_label.config(fg="powderblue")
    if timer_seconds <= 0:
        # time's up - end the quiz
        messagebox.showinfo("Time's up!", f"The Spaceship ran out of fuel! Your score: {score}/{10}")
        question_label.pack_forget()
        for b in buttons:
            b.pack_forget()
        restart_button.pack(pady=20)
        exit_button.pack(pady=20)
        exit_button.lift()
        timer_id = None
        return

    # schedule next tick
    timer_id = window.after(1000, timer_tick)

def start_timer():
    """Initialize and start the countdown timer (60s)."""
    global timer_seconds, timer_id
    # reset timer
    timer_seconds = 60
    timer_label.config(text=f"Time: {timer_seconds}s", fg="powderblue")
    # cancel existing timer if any
    if timer_id is not None:
        window.after_cancel(timer_id)
    timer_id = window.after(1000, timer_tick)

def stop_timer():
    global timer_id
    if timer_id is not None:
        try:
            window.after_cancel(timer_id)
        except Exception:
            pass
        timer_id = None
        
welcome_background()
if __name__ == "__main__":
    window.mainloop()

