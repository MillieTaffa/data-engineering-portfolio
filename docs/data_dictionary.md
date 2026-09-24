# SocialPulse Data Dictionary

## Source dataset

The pipeline reads `data/raw/social_media_engagement_dataset.csv`. Each row represents
one social-media post, identified by `Post_ID`.

| Field | Meaning |
|---|---|
| `Post_ID` | Unique identifier for a post. |
| `Timestamp` | Date and time the post was published, in `YYYY-MM-DD HH:MM:SS` format. |
| `Platform` | Social network where the post was published. |
| `Content_Type` | Format of the post, such as a photo, video, carousel, or document. |
| `Category` | Subject category of the post. |
| `Likes`, `Comments`, `Shares`, `Saves` | Engagement actions recorded for the post. |
| `Views` | Number of views recorded for the post. |
| `Follower_Count` | Creator's follower count. |
| `Engagement_Rate` | Rate supplied by the source dataset. Its formula is unknown, so it is retained unchanged. |
| `Hour_of_Day` | Publishing hour from 0 to 23. The cleaning stage recalculates it from `Timestamp`. |
| `Day_of_Week` | Publishing day name. The cleaning stage recalculates it from `Timestamp`. |
| `Hashtag_Count` | Number of hashtags included in the post. |
| `Content_Length` | Length of the post content in the source dataset's units. |
| `Sentiment` | Source sentiment label: Positive, Neutral, or Negative. |
| `Influencer_Tier` | Creator audience tier: Nano, Micro, Mid-tier, or Macro. |
| `Has_Media` | Whether the post includes media. |
| `Is_Verified` | Whether the creator is verified. |

## Derived fields

The transformation stage creates these fields. They are saved in both the processed
CSV and the SQLite `posts` table.

| Field | Formula or meaning |
|---|---|
| `total_interactions` | `Likes + Comments + Shares + Saves` |
| `computed_engagement_rate` | `total_interactions / Views * 100` |
| `comment_rate` | `Comments / Views * 100` |
| `share_rate` | `Shares / Views * 100` |
| `post_date` | Calendar date extracted from `Timestamp`, used for daily charts. |

When `Views` is zero, rate fields are left empty because a rate cannot be calculated.
`computed_engagement_rate` is intentionally separate from the source
`Engagement_Rate` field.
