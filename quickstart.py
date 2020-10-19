"""
This template is written by @Nuzzo235

What does this quickstart script aim to do?
- This script is targeting followers of similar accounts and influencers.
- This is my starting point for a conservative approach: Interact with the
audience of influencers in your niche with the help of 'Target-Lists' and
'randomization'.

NOTES:
- For the ease of use most of the relevant data is retrieved in the upper part.
"""

import random
from instapy import InstaPy
from instapy import smart_run
import time
import sys
# login credentials
insta_username = 'nthallroom54@gmail.com'
insta_password = 'Shweta@2020'

# restriction data
dont_likes = []
ignore_users = []

""" Prevent commenting on and unfollowing your good friends (the images will 
still be liked)...
"""
friends = []

""" Prevent posts that contain...
"""
ignore_list = []

# TARGET data
""" Set similar accounts and influencers from your niche to target...
"""
targets = ['aishasharma25','saba_ka_jahaan','jissapaull','bandgikalra','kshama3091','arshiamoorjani','mensxpofficial','trendelitee','treatyowselff','malvikasitlaniofficial','shreyajain26','stylefashionetc','komalpandeyofficial','aanamc','corallistablog','shrutiarjunanand','ispeakwhatyoulove','kaush_m','deepikamakeup','anchalmua','himaniwright','ttlmakeupjunkie','shreyajain26','natasshapatel','magali_c','therightshadeofred','bighairloudmouth']
#
""" Skip all business accounts, except from list given...
"""
target_business_categories = ['Beauty, Cosmetic & Personal Care','Beauty Salon','Fashion Model','Health/Beauty']

# COMMENT data
comments = ['Nice shot! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:','Nice Photo @{}','Great Pic @{}','Lots of Love @{}',]

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # HEY HO LETS GO
    # general settings
    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)
    session.set_ignore_users(ignore_users)
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=sys.maxsize,
                                    max_following=sys.maxsize,
                                    min_followers=0,
                                    min_following=0,
                                    min_posts=0)

    session.set_skip_users(skip_private=False,
                           skip_no_profile_pic=True,
                           skip_business=True,
                           dont_skip_business_categories=[
                               target_business_categories])

    session.set_user_interact(amount=50, randomize=True, percentage=60,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=60)
    session.set_do_comment(enabled=True, percentage=60)
    session.set_comments(comments, media='Photo')
    session.set_do_follow(enabled=True, percentage=100, times=100)

    # activities

    # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """

    """ Interact with the chosen targets...
    """
    while 1 == 1:
        number = random.randint(1, 5)
        random_targets = targets
        if len(targets) <= number:
            random_targets = targets
        else:
            random_targets = random.sample(targets, number)

        try:
            session.follow_user_followers(random_targets, amount=random.randint(30, 60), randomize=True, sleep_delay=600, interact=True)
        except:
            pass


    # UNFOLLOW activity
    """ Unfollow nonfollowers after one day...
    """
    try:
        session.unfollow_users(amount=random.randint(75, 100), nonFollowers=True,style="FIFO", unfollow_after=24 * 60 * 60, sleep_delay=600)
    except:
        pass
    """ Unfollow all users followed by InstaPy after one week to keep the 
    following-level clean...
    """
    try:
        session.unfollow_users(amount=random.randint(75, 100),allFollowing=True, style="FIFO", unfollow_after=168 * 60 * 60, sleep_delay=600)
    except:
        pass
    """ Joining Engagement Pods...
    """
    session.join_pods()

"""
Have fun while optimizing for your purposes, Nuzzo
"""
