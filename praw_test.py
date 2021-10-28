"""
    Testing praw and flask interactions
"""
import praw
import random


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
    for submission in hot_subreddit:
        x.update({submission.title: random.random()})   # random represents test value for nlp

    return x


if __name__ == '__main__':
    main()
