def passing_count(scores, passing_score):
    passes = [score for score in scores if score >= passing_score]
    return len(passes)
