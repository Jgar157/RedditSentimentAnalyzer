"""
    Testing praw and flask interactions
"""
import praw
import random
# from Neural import NeuralAnalyzer as na


def main(subreddit_name: str) -> dict:
    """
    Testing praw and flask interactions
    :return: value for website to use
    """
    reddit = praw.Reddit(client_id='RYKQk1tTkp0fdr6VTuzcrg',
                         client_secret='acg2DKb0kXPWdLUbmMuXZlOHb4NdKg',
                         user_agent='Praw Test')
    subreddit = reddit.subreddit(subreddit_name)

    hot_subreddit = subreddit.hot()
    x = {}
    # hate_network = na.NeuralAnalyzer("Neural/neural_networks/hate_neural/hate_model",
    #                                  "Neural/neural_networks/hate_neural/tokenizer.pickle")
    for submission in hot_subreddit:
        # predicted_value = hate_network.predict_text([submission.title])
        x.update({submission.title: random.random()})   # random represents test value for nlp
        # x.update({submission.title: predicted_value})

    return x


if __name__ == '__main__':
    main()
