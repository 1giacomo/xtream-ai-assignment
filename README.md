# xtream AI Challenge

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
