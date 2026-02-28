# from fastmcp import FastMCP
# import feedparser

# mcp = FastMCP(name="FreeCodeCamp Feed Parser")

# @mcp.tool()
# def fcc_news_search(query: str, max_results: int = 3):
#     """
#     search FreeCodeCamp news feed via RSS by title / description
#     """
#     feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
#     results = []

#     query_lower = query.lower()

#     for entry in feed.entries:
#         title = entry.get("title", "")
#         description = entry.get("description", "")

#         if query_lower in title.lower() or query_lower in description.lower():
#             results.append({
#                 "title": title,
#                 "url": entry.get("link", "")
#             })

#         if len(results) >= max_results:
#             break

#     return results or [{"message": "No results found"}]


# @mcp.tool()
# def fcc_youtube_search(query: str, max_results: int = 3):
#     """
#     Search FreeCodeCamp's YouTube channel for videos matching a query.

#     This tool demonstrates how to:
#     1. Parse a YouTube RSS feed
#     2. Search through video entries
#     3. Return formatted results

#     Args:
#         query (str): The search term to look for in video titles
#         max_results (int, optional): Maximum number of results to return. Defaults to 3.

#     Returns:
#         list: A list of dictionaries containing matching videos
#     """
#     # Step 4.1: Parse the YouTube RSS feed
#     feed = feedparser.parse(
#         "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
#     )

#     # Step 4.2: Prepare for search
#     results = []
#     query_lower = query.lower()

#     # Step 4.3: Search through entries
#     for entry in feed.entries:
#         title = entry.get("title", "")

#         # Check if query appears in title
#         if query_lower in title.lower() :
#             # Add matching video to results
#             results.append({
#                 "title": title,
#                 "url": entry.get("link", "")
#             })

#             # Stop if we have enough results
#             if len(results) >= max_results:
#                 break

#     # Step 4.4: Return results or a "no results" message
#     return results or [{"message": "No videos found"}]

# @mcp.tool()
# def print_secret_message(message: str):
#     """Reveal the secret message of FreeCodeCamp"""

#     return "Keep yourself out of Comfort Zone"

# if __name__ == "__main__":
#     mcp.run()


from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="FreeCodeCamp Feed Searcher")

@mcp.tool()
def fcc_news_search(query:str, max_results:int=3):
    """Search FreeCodeCamp news feed via RSS by title/description"""
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({"title":title, "url":entry.get("link", "")})
        if len(results) >= max_results:
            break #unlikely to occur

    return results or [{"message":"No results found"}]

@mcp.tool()
def fcc_youtube_search(query:str, max_results:int=3):
    """Search FreeCodeCamp Youtube channnel via RSS by title"""
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({"title":title, "url":entry.get("link", "")})
        if len(results) >= max_results:
            break #unlikely to occur
    return results or [{"message":"No videos found"}]

@mcp.tool()
def fcc_secret_message():
    """Returns a secret message of FreeCodeCamp"""
    return "Keep exploring! and happy coding!"

if __name__ == "__main__":
    mcp.run(transport="http") #STDIO