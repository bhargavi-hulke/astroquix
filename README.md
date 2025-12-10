# 🌌 Astroquix – astronomy quiz game

Astroquix is my first full Python project: a space‑themed multiple‑choice quiz game with animated backgrounds, a countdown timer, and a pool of easy‑to‑moderate astronomy questions. It runs as a desktop app using Tkinter and Pillow. Originally,it started as a simple **rapid-fire quiz** to test the player's knowledge in astronomy and gradually turned into a small space arcade–style experience with animated backgrounds.It also takes the player on a journey through the cosmos with its fun, space themed messages, along the quiz.

---

## ✨ Features

- Dual animated GIF backgrounds (welcome screen + quiz screen), with a clean black fallback if GIFs are missing  
- 60‑second countdown timer with color change warning in the last 10 seconds 
- 10 random questions per round from a larger question bank  
- Score tracking with different end messages based on performance  
- Simple, arcade-style UI with space vibes (dark background, text/buttons)  
- Fair randomization using shuffled question lists each round  
---

## 🛠 Tech Stack

- Python (Tkinter for GUI)  
- Pillow (PIL) for loading and animating GIFs  
- Standard library only otherwise (no external backend or web stuff)
---

## 🚀 How to Run

1. Make sure you have Python 3 installed.  
2. Install Pillow:
      pip install pillow

3. Save the main script as something like `astroquix.py`.  
4. (Optional but recommended) Put your background GIFs in the same folder as the script and name them:

- `welcome_bg.gif` – calm / intro animation  
- `quiz_bg.gif` – more energetic quiz background  

5. Run the app:
     python astroquix.py

If the GIFs are not present or are too large, the app still works and just shows a black background.

---

## 📱 Screenshots

### Welcome Screen
![Welcome Screen](astroquix/welcome_scr.png)
*Calm welcome with "Hell Yeah!! Let's go!!" button*

### Quiz in Action
![Quiz Screen](astroquix/quiz_scr.png)
*Stars background + question + 60s timer + option buttons*

### Final Results
![Results](astroquix/results_scr.png)
*"Stage Completed! 9/10 in 36s"*

---

## 🎮 Gameplay

- On launch, a welcome screen is shown with a start button and an exit button.  
- Hitting the start button:
  - Switches to the quiz GIF background  
  - Starts a 60‑second timer  
  - Loads 10 random questions from the question pool  
- Each question:
  - Shows one question and 4 options  
  - Lets the player pick one option (buttons get disabled after selection)  
- At the end of the quiz (after 10 questions or timeout):
  - The timer stops  
  - The app shows the final score  
  - It also shows how many seconds the player took (based on remaining time)  
  - A themed message is shown depending on the score (e.g., "Stage Completed", "Well done!", "Try Again!")  
  - The player can restart the quiz from the welcome screen.

---

## 🧠 Question Bank

The quiz uses a list of dictionaries with this format:

  {
    "question": "What is the name of the process by which stars produce energy?",
    "options": ["Nuclear Fusion", "Nuclear Fission", "Combustion", "Radiation"],
    "correct answer": "Nuclear Fusion"
}

Topics include:

Planets and moons

Space missions (Apollo, Voyager, ISRO, etc.)

Phenomena like black holes, supernovas, auroras, eclipses

Basic cosmology (Big Bang, galaxies, constellations)

It’s easy to add more questions by appending to the quiz_data list in the same format.

---

## 🎨 GIFs and Assets

I originally used animated GIFs for the background that were quite large (over 200 MB), so I did **not** include them in the repo. Instead:

- The code expects `welcome_bg.gif` and `quiz_bg.gif` in the same directory as the script.  
- If they're missing, the app falls back to a solid black background and still runs fine.  
- Anyone cloning the project can plug in their own space GIFs with those filenames.

---

## 🔧 Known Limitations / Future Ideas

- No settings menu yet (for difficulty, number of questions, etc.)  
- Everything runs in a single window and single file for now  
- Could add sound effects, more levels, or a high‑score system later  

---
## 📄 License

MIT License - Use, modify, share freely!

---
## 🙌 About This Project

This is my first “proper” Python GUI project: a complete, playable app with animations, a timer, and stateful logic. The idea started back in my first semester of college as a beginner, when I wanted a quiz that has the thrill of a game and tests your astronomy wits for all the **spaceheads** out there (like myself, hehe). I gradually improved it by experimenting with a lot of **“what if…?”**, and it eventually turned into an arcade‑style game with a more polished UI. Along the way I got a ton of practice with error handling, animation integration, and GUI design. It still has plenty of room for improvement, but I’m proud of where it is right now.

---

If you try it out or build on top of it, feel free to tweak the questions, themes, and GIFs to match your own version of the cosmos.

---
Made with ❤️ for space explorers 🚀🌌⭐
