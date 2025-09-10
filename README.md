# Unbeatable Tic-Tac-Toe AI
A simple project that uses the **Minimax Algorithm** with **alpha-beta pruning** to create a Tic-Tac-Toe AI that can't be beaten.

## Table of Contents
- [Description](#description)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Commit Message Guideline](#commit-message-guidelines)

## Description
This project is a Tic-Tac-Toe game where one player is controlled by a human and the other is an AI. The AI's logic is built on the well-known minimax algorithm, which analyzes every possible move to find the optimal one. To make the AI efficient, I implemented alpha-beta pruning to intelligently "prune" or skip branches of the decision tree that would never lead to a better outcome. The user interface is built using the ``pygame`` library.

## Getting Started

### Prerequisites
You need **Python 3.x** and the `pygame` library to run this game.

### Installation

You can install the required library using `pip`:
```bash
pip install pygame
```

## Usage
To start the game, simply run this script in your terminal:
```bash
python runner.py
```

After the game window appears, you can choose to play as **X** or **O**, and the AI will take the opposing role.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this project better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement."

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes. Check [here](#commit-message-guidelines) for the commit message guidelines
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## Credits

This project was inspired by and developed as part of the **CS50AI** course by **Harvard University**, which provided a fantastic foundation in artificial intelligence and game theory. You can view the course [here](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home).  
I'd also like to thank the open-source community for the `pygame` library, which made building the graphical interface possible.

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

## Commit Message Guidelines
This project follows the principles of **Conventional Commits** [here](https://www.conventionalcommits.org/en/v1.0.0/#specification).  
The commit message should be structured as follows:

`type(scope): description`

* **`type`**: Must be one of the following: `feat` (new feature), `fix` (bug fix), `docs` (documentation), `style` (formatting), `refactor` (code change that doesn't fix a bug or add a feature), `test` (adding tests), `build` (changes to the build system), `ci` (CI configuration changes), `perf` (performance improvements), or `chore` (miscellaneous changes).
* **`scope`**: Optional, but recommended. It provides context for the change (e.g., `gui`, `minimax`, `tictactoe`).
* **`description`**: A brief, imperative-tense description of the change.

