# 🎮 2048 Game 🎮

Welcome to the digital version of the classic 2048 game, where you combine tiles to reach the elusive 2048 tile and test your strategic skills!

## 📜 Table of Contents

- [Introduction](#introduction)
- [Game Objective](#game-objective)
- [Game Rules](#game-rules)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Development Reflection](#development-reflection)
- [Lessons Learned](#lessons-learned)
- [Conclusion and Future Scope](#conclusion-and-future-scope)

## 🌟 Introduction

The '2048 Game' brings the beloved tile-sliding puzzle to your digital device. It's a challenging and addictive game where you'll need to combine matching tiles to achieve the 2048 tile and emerge victorious.

## 🎯 Game Objective

Your goal is to reach the 2048 tile by strategically merging matching tiles on a 4x4 grid. The challenge lies in making the right moves to achieve this without running out of space!

## 📏 Game Rules

- **Tile Merging**: Tiles with the same number merge when they touch, creating a tile with the sum of their values.
- **Limited Moves**: You have a limited number of moves to reach the 2048 tile.
- **Victory and Defeat**: The game is won when you achieve the 2048 tile. If the grid is full, and you can't make a move, the game ends.

## 🔧 Tech Stack

Our 2048 game is built using web technologies, including HTML, CSS, and JavaScript, Django, AWS. This combination ensures a seamless and enjoyable gaming experience right from your browser.

## 🌐 Setup

Want to play or even host your own version of the 2048 game? It's easy!

1. Clone the game repository to your local machine: https://github.com/SaiNikhil02/FSE-Project .
2. Installing dependencies: pip3 -r install requirements.txt
3. Run the following commands in your terminal:
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
4. Game URL: https://1024tilegame.pythonanywhere.com/game/
5. Go to `/game/` endpoint, to view the game page.  
6. Use the arrow keys on your keyboard to make your moves.
7. Enjoy the game!

## 💭 Development Reflection

One of the major challenges we encountered during the development of the 2048 game was the design and implementation of the tile merging algorithm. Crafting a robust logic for how tiles should merge when they touch was a complex endeavor that demanded careful planning and extensive testing. We had to meticulously consider various scenarios and edge cases to ensure that the game's core mechanic worked flawlessly.

In addition to the algorithm, another critical aspect of our project was the user interface (UI) design. Designing an intuitive and visually appealing UI was imperative for the game's success. Our aim was to strike a delicate balance between a clean, user-friendly design and the provision of essential information to players, such as their current score and the number of moves remaining. Achieving a design that was both functional and aesthetically pleasing proved to be a time-consuming process, but one that was well worth the effort.

Furthermore, we faced the challenge of implementing a limited number of moves as a core game mechanic. Determining the right number of moves to provide players with a fair chance of reaching the coveted 2048 tile without making it either too easy or excessively challenging was a task that required careful consideration.

Effective teamwork was a lesson we learned throughout the project's development. While collaboration was pivotal to our success, it wasn't without its initial challenges. Coordinating efforts, ensuring that everyone was on the same page, and resolving conflicts required open communication and a willingness to compromise. Once we established a smooth workflow and fostered a sense of unity within the team, the project progressed more efficiently.

Our team collaboration, despite the initial challenges, was a significant success. We carefully divided tasks among team members, scheduled regular meetings to discuss progress and address challenges, and shared knowledge. This collaborative spirit proved to be instrumental in overcoming hurdles and maintaining steady progress.

Understanding the importance of the tile merging algorithm, we made it a priority from the project's early stages. We continuously iterated on the algorithm, conducting thorough testing and addressing any bugs we discovered along the way. This iterative approach resulted in a robust game mechanic that provided players with a satisfying and enjoyable experience.

We actively sought feedback from potential players and incorporated their input into our design and development process. This user-centric approach allowed us to fine-tune the game's difficulty and improve the user interface. Listening to the perspective of end-users proved invaluable in shaping the final product.

Despite our successes, we also encountered some challenges. We underwent several design iterations, some of which consumed time and resources without yielding the desired results. It was a lesson in finding the right balance between creativity and practicality in UI design to ensure a smooth and engaging gaming experience.

Additionally, deploying the game on AWS and ensuring its availability online posed its set of challenges. It required a deep understanding of the tech stack and meticulous configuration.

In conclusion, the development of the 2048 game was a journey filled with valuable lessons. We overcame challenges related to algorithm design, UI development, and teamwork, while also making the most of our successes. As we look to the future, we're excited about the potential to introduce new features, game modes, and enhancements to keep players engaged and entertained. The 2048 game project was not only a testament to our development skills but also a testament to our ability to work together as a team and deliver a fun and challenging gaming experience to our audience. We're grateful for your support and hope you enjoy playing the game as much as we enjoyed creating it.

## 🎓 Lessons Learned

- **Teamwork**: Effective teamwork was crucial in overcoming challenges and developing a polished game.
- **Algorithm Design**: We honed our skills in algorithm design, particularly for tile merging and game logic.
- **UI/UX Design**: Creating a visually appealing and user-friendly interface was a key aspect of our project's success.

## 🥂 Conclusion and Future Scope

The 2048 game project was a valuable learning experience that enhanced our development skills and teamwork. While we celebrated our success in creating a fun and challenging game, we're excited about future enhancements. We're looking forward to introducing new features and game modes to keep players engaged and entertained.

---

**👏 Thank you for being part of our 2048 game's journey. Ready to test your strategic skills? Let's play and reach that 2048 tile! 🎉**