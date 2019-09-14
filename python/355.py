from collections import defaultdict


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet_count = 0
        self.recent_tweet_ids = []
        self.followers = defaultdict(set)
        self.user_tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweet_count += 1
        self.user_tweets[userId].append(tweetId)
        heapq.heappush(self.recent_tweet_ids, (-self.tweet_count, tweetId, userId))
        self.followers[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        all_users = self.followers[userId]
        current_tweets = self.recent_tweet_ids.copy()
        k = 0
        result = []
        while k < 10 and len(current_tweets) > 0:
            if len(current_tweets) > 0:
                el = heapq.heappop(current_tweets)
                if el[2] in all_users:
                    k += 1
                    result.append(el[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].add(followerId)
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId and (followeeId in self.followers[followerId]):
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# SECOND SOLUTION (FASTER)
#
# from collections import defaultdict
# import heapq
# class Twitter(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.followers = defaultdict(set)
#         self.tweets = defaultdict(list)
#         self.tweetcount = 0
#
#
#     def postTweet(self, userId, tweetId):
#         """
#         Compose a new tweet.
#         :type userId: int
#         :type tweetId: int
#         :rtype: None
#         """
#         self.tweetcount += 1
#         self.tweets[userId].append((-self.tweetcount, tweetId))
#
#
#
#     def getNewsFeed(self, userId):
#         """
#         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
#         :type userId: int
#         :rtype: List[int]
#         """
#         user_tweets, follower_tweets = self.tweets[userId][-10:], []
#         for user in self.followers[userId]:
#             follower_tweets.extend(self.tweets[user])
#         all_tweets = user_tweets + follower_tweets
#         heapq.heapify(all_tweets)
#         result = []
#         for i in range(10):
#             if len(all_tweets) > 0:
#                 result.append(heapq.heappop(all_tweets)[1])
#         return result
#
#
#
#     def follow(self, followerId, followeeId):
#         """
#         Follower follows a followee. If the operation is invalid, it should be a no-op.
#         :type followerId: int
#         :type followeeId: int
#         :rtype: None
#         """
#         if followerId != followeeId:
#             self.followers[followerId].add(followeeId)
#
#
#     def unfollow(self, followerId, followeeId):
#         """
#         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
#         :type followerId: int
#         :type followeeId: int
#         :rtype: None
#         """
#         self.followers[followerId].discard(followeeId)
#
#
#
# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)
