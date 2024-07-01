from src.comment_sentiment import comment_sentiment


def comment_sorting(url: str, sorting_parameter: str,  subfeddit_id: int = 0, skip: int =  0, limit: int = 25, start_time: int = 0, end_time: int = 0):
	final_result = comment_sentiment(url, subfeddit_id, skip, limit)
	if sorting_parameter == "created_time":
		# Filter comments by a specific time range
		final_result = [comment for comment in final_result if comment["created_time"] >= start_time and comment["created_time"] <= end_time]
	elif sorting_parameter == "polarity":
		final_result = sorted(final_result, key=lambda x: x["polarity"], reverse=True)
	return final_result