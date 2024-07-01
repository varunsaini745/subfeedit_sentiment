from textblob import TextBlob
import requests
from src.model import Comment


def analyze_sentiment(text: str):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    classification = "positive" if polarity >= 0 else "negative"
    return polarity, classification


def comment_sentiment(url: str, subfeddit_id: int = 0,
                      skip: int = 0, limit: int = 25):
    final_result = []
    response_subfeddit = requests.get(
        url, params={"subfeddit_id": subfeddit_id,
                     "skip": skip, "limit": limit}
    )
    response_subfeddit = response_subfeddit.json()
    print(response_subfeddit)
    for i in response_subfeddit["comments"]:
        comment = Comment(
            id=i["id"],
            text=i["text"],
            polarity=analyze_sentiment(i["text"])[0],
            classification=analyze_sentiment(i["text"])[1],
            created_time=i["created_at"],
        )
        final_result.append(comment.model_dump())
    return final_result


if __name__ == "__main__":
    text = "I love the weather today"
    # response = get_data("http://0.0.0.0:8080/api/v1/comments", 1, 0, 25)
    # print(response["comments"])
    # polarity, classification = analyze_sentiment(text)
    # print(f"Polarity: {polarity}")
    # print(f"Classification: {classification}")
    result = comment_sentiment("http://0.0.0.0:8080/api/v1/comments", 1, 0, 25)
    print(result)
