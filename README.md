Your repo has a much simpler, flatter structure than my first draft assumed—just `00_problem_set/` and `01_problem_set/` so far, each containing one folder per problem. Here’s a README rewritten to match exactly what you have.

---

# CS50P Problem Sets — Solutions

> My personal solutions to the problem sets from [CS50’s Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python/) by Harvard University.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CS50P](https://img.shields.io/badge/CS50P-2024-red)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📖 About

This repository contains my solutions to the **problem sets (PSets)** from CS50P. Each problem set lives in its own numbered folder, and each individual problem gets its own subfolder.

The solutions here are for **reference and learning purposes only**. If you’re currently taking CS50P, please follow the course’s [academic honesty policy](https://cs50.harvard.edu/x/2024/honesty/) and attempt the problems yourself first.

---

## 📂 Repository Structure

```
CS50P/
├── 00_problem_set/
│   ├── einstein/
│   ├── faces/
│   ├── indoor/
│   ├── playback/
│   └── tip/
├── 01_problem_set/
│   ├── bank/
│   ├── deep/
│   ├── extensions/
│   ├── interpreter/
│   └── meal/
└── (future weeks will be added here)
```

Each problem folder contains the `.py` solution file(s) for that problem. I’m adding new weeks as I progress through the course.

---

## 🗓️ Problem Sets Covered

| Week | Topic | Problems |
|------|-------|----------|
| 0 | Functions & Variables | `einstein`, `faces`, `indoor`, `playback`, `tip` |
| 1 | Conditionals | `bank`, `deep`, `extensions`, `interpreter`, `meal` |

**Progress:** Weeks 0 and 1 complete. More weeks coming soon.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (recommended)
- Basic familiarity with the terminal

### Running a Solution

Clone the repo and run any file directly:

```bash
git clone https://github.com/saleh05-59/CS50P.git
cd CS50P
python 00_problem_set/indoor/indoor.py
```

Some programs read from standard input — check the code or comments inside each file for usage examples.

---

## 📝 Notes

- Solutions are written in **clear, beginner-friendly Python**, with comments where helpful.
- Files are structured to match the expected input/output behavior from the CS50P specification.
- Some solutions may differ stylistically from the staff solutions — that’s the point of solving it yourself.

---

## ⚠️ Academic Honesty

Please do **not** copy these solutions for your own CS50P submissions. The purpose of this repo is to:

- Document my own learning journey
- Provide a reference for others who are stuck (after trying themselves)
- Share approaches and alternative implementations

Read Harvard’s [Academic Honesty Policy](https://cs50.harvard.edu/x/2024/honesty/) before submitting any work.

---

## 🛠️ Tools & Resources

- [CS50P Course Website](https://cs50.harvard.edu/python/)
- [CS50P Lecture Notes](https://cs50.harvard.edu/python/2022/notes/)
- [Python Documentation](https://docs.python.org/3/)
- [Check50](https://cs50.readthedocs.io/projects/check50/en/latest/) for autograding

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use it for educational purposes.

---

## 🙏 Acknowledgments

- **David J. Malan** and the entire CS50 team
- **Harvard University** for making CS50P free and accessible
- The CS50 community for discussion forums and support

---

<div align="center">
<sub>Happy coding! 🐍</sub>
</div>

---

A few things you can update as you go:

- **Status badge**: change `in%20progress` to `complete` once you finish all weeks.
- **Structure tree**: add `02_problem_set/`, `03_problem_set/`, etc. as you create them.
- **Progress note**: update the “Weeks 0 and 1 complete” line each time you finish a new week.
- **Final project**: if you add a `final_project/` folder later, add it to the tree and the table.