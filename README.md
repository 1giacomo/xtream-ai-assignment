# xtream AI Challenge

## Ready Player 1? 🚀

Hey there! If you're reading this, you've already aced our first screening. Awesome job! 👏👏👏

Welcome to the next level of your journey towards the [xtream](https://xtreamers.io) AI squad. Here's your cool new assignment.

Among the datasets described below, pick **just one** that catches your eye. Each dataset comes with its own set of challenges. Don't stress about doing them all. Just dive into the ones that spark your interest or that you feel confident about. Let your talents shine bright! ✨

Take your time – you've got **10 days** to show us your magic, starting from when you get this. No rush, work at your pace. If you need more time, just let us know. We're here to help you succeed. 🤝

### What You Need to Do

Think of this as a real-world project. Fork this repo and treat it as if you're working on something big! When the deadline hits, we'll be excited to check out your work. No need to tell us you're done – we'll know. 😎

🚨 **Heads Up**: You might think the tasks are a bit open-ended or the instructions aren't super detailed. That’s intentional! We want to see how you creatively make the most out of the data and craft your own effective solutions.

🚨 **Remember**: At the end of this doc, there's a "How to run" section left blank just for you. Please fill it in with instructions on how to run your code – it's important!

### How We'll Evaluate Your Work

We'll be looking at a bunch of things to see how awesome your work is, like:

* Your approach and method
* How well you get the business problem
* Your understanding of the data
* The clarity and completeness of your findings
* How you use your tools (like git and Python packages)
* The neatness of your code
* The clarity of your documentation

🚨 **Keep This in Mind**: This isn't about building the fanciest model: we're more interested in your process and thinking.

## Special Note for Interns

If you're aiming for an internship, focus **only on Challenges 1 and 2** for the dataset you choose.

We'll mainly look at:

* Your workflow
* How well you understand the problem and data
* The approach to the analysis and clarity of your conclusions
* How neat your code is (relative to your experience level)

This is your chance to showcase your unique approach and thought process. Don't worry if your code isn't perfect or your model isn't top-notch yet. We've been in your shoes and are here to help you grow. 🌟

---

### Diamonds

**Problem type**: Regression

**Dataset description**: [Diamonds Readme](./datasets/diamonds/README.md)

Meet Don Francesco, the mystery-shrouded, fabulously wealthy owner of a jewelry empire. 

He's got an impressive collection of 5000 diamonds and a temperament to match - so let's keep him smiling, shall we? 
In our dataset, you'll find all the glittery details of these gems, from size to sparkle, along with their values 
appraised by an expert. You can assume that the expert's valuations are in line with the real market value of the stones.

#### Challenge 1

Francesco wonders: **what makes a diamond valuable?** You should provide him with an answer.

Don Francesco has been very clear with you: he is not a fan of tech jargon, so keep your message plain and simple. 
However, he trusts no one - certainly not you. He's hired Luca, another data scientist, to double-check your findings (no pressure!). 
Your mission is simple. 

Create a Jupyter notebook to explain what Francesco should look at and why.
Your code should be understandable by a data scientist like Luca, but your text and visualizations should be clear for a layman like Francesco.

#### Challenge 2

Plot twist! The expert who priced these gems has now vanished. 
Francesco needs you to be the new diamond evaluator. 
He's looking for a **model that predicts a gem's worth based on its characteristics**. 
And, because Francesco's clientele is as demanding as he is, he wants the why behind every price tag. 

Create another Jupyter notebook where you develop and evaluate your model.

---

## How to run

### Google Colab (Recommended)

Both notebooks are on Google Colab ready to run.

* [Challenge 1](https://colab.research.google.com/drive/1wkIHYESKVFetaFaZ9ZWnE3EZC6939grY)
* [Challenge 2](https://colab.research.google.com/drive/1ty0Bml_yJkIVHd5-rGTN3MOUnqgRRQ5J)

### Run local

If you prefer to run local in your virtual environment you can do it by:

1. Clone the repository:
```bash
git clone https://github.com/1giacomo/xtream-ai-assignment.git
```

2. Navigate to the project directory:

```bash
cd xtream-ai-assignment
```

3. Create you Virtual Environment:
```bash
python -m venv ./venv
```

4. Activate the Virtual Environment:
```bash
source venv/bin/activate
```

5. Install the dependencies:
```bash
pip install -r requirements.txt
```

6. Before running the files, remove this block of code:
```bash
# REMOVE THIS BLOCK IF YOU RUN LOCAL

# Clone the dataset from Github
!git clone https://github.com/1giacomo/xtream-ai-assignment.git

# Load the dataset from the .csv file
diamonds = pd.read_csv("./xtream-ai-assignment/datasets/diamonds/diamonds.csv")
```

Instead uncomment the second block like this:
```bash
# UNCOMMENT THIS BLOCK IF YOU RUN LOCAL

# Load the dataset from the .csv file
diamonds = pd.read_csv("./datasets/diamonds/diamonds.csv")
```
Do it for both the notebooks.

8. Run the notebooks.
