from typing import Optional
from pydantic import HttpUrl, parse_obj_as


NEBULA_API_CONTENT_VIDEO_CHANNELS = parse_obj_as(
    HttpUrl, "https://content.api.nebula.app/video/channels/{CHANNEL_SLUG}/"
)
# {
#     "details": {
#         "id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#         "type": "video_channel",
#         "slug": "techaltar",
#         "title": "TechAltar",
#         "published_at": "2021-05-27T13:30:38Z",
#         "description": "Video essays about the past, present and future of consumer technology.",
#         "assets": {
#             "avatar": {
#                 "16": {
#                     "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                     "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                 },
#                 "32": {
#                     "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                     "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                 },
#                 "64": {
#                     "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                     "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                 },
#                 "128": {
#                     "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                     "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                 },
#                 "256": {
#                     "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                     "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                 },
#                 "512": {
#                     "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                     "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                 }
#             },
#             "banner": {
#                 "240": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=240",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=240"
#                 },
#                 "360": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=360",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=360"
#                 },
#                 "480": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=480",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=480"
#                 },
#                 "720": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=720",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=720"
#                 },
#                 "960": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=960",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=960"
#                 },
#                 "1440": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=1440",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=1440"
#                 },
#                 "1920": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=1920",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=1920"
#                 },
#                 "2560": {
#                     "original": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.jpeg?width=2560",
#                     "webp": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801.webp?width=2560"
#                 }
#             },
#             "hero": {
#                 "240": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=240",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=240"
#                 },
#                 "360": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=360",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=360"
#                 },
#                 "480": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=480",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=480"
#                 },
#                 "720": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=720",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=720"
#                 },
#                 "960": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=960",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=960"
#                 },
#                 "1440": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=1440",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=1440"
#                 },
#                 "1920": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=1920",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=1920"
#                 },
#                 "2560": {
#                     "original": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.jpeg?width=2560",
#                     "webp": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96.webp?width=2560"
#                 }
#             },
#             "featured": {
#                 "240": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=240",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=240"
#                 },
#                 "360": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=360",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=360"
#                 },
#                 "480": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=480",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=480"
#                 },
#                 "720": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=720",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=720"
#                 },
#                 "960": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=960",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=960"
#                 },
#                 "1440": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=1440",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=1440"
#                 },
#                 "1920": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=1920",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=1920"
#                 },
#                 "2560": {
#                     "original": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.jpeg?width=2560",
#                     "webp": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179.webp?width=2560"
#                 }
#             }
#         },
#         "images": {
#             "avatar": {
#                 "formats": [
#                     "jpeg",
#                     "png",
#                     "webp"
#                 ],
#                 "width": 288,
#                 "height": 288,
#                 "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#             },
#             "banner": {
#                 "formats": [
#                     "jpeg",
#                     "png",
#                     "webp"
#                 ],
#                 "width": 2560,
#                 "height": 1440,
#                 "src": "https://dj423fildxgac.cloudfront.net/bd294151-8053-467b-ab81-10eceb207801"
#             },
#             "hero": {
#                 "formats": [
#                     "jpeg",
#                     "png",
#                     "webp"
#                 ],
#                 "width": 2560,
#                 "height": 1440,
#                 "src": "https://dj423fildxgac.cloudfront.net/41af10a5-61db-4ce0-ba63-f8120d5e6b96"
#             },
#             "featured": {
#                 "formats": [
#                     "jpeg",
#                     "png",
#                     "webp"
#                 ],
#                 "width": 2560,
#                 "height": 1440,
#                 "src": "https://dj423fildxgac.cloudfront.net/f889bcf0-54e8-43e5-bcdc-b033e20f3179"
#             }
#         },
#         "genre_category_title": "Technology",
#         "genre_category_slug": "technology",
#         "categories": [
#             {
#                 "id": "category:b373d1c7-a77a-401d-9f3e-166fd02970fd",
#                 "type": "category",
#                 "slug": "technology",
#                 "title": "Technology",
#                 "assets": {
#                     "avatar": "https://dj423fildxgac.cloudfront.net/99a1a75c-1947-4120-b766-f8597e9ab897.webp",
#                     "avatar-big-dark": "https://dj423fildxgac.cloudfront.net/7f8b6da6-748b-4de4-b8c7-67977ddb42f2.webp",
#                     "avatar-big-light": "https://dj423fildxgac.cloudfront.net/1f25d49f-de0a-4877-8ecf-e6ef3cb28148.webp"
#                 },
#                 "images": {
#                     "avatar": {
#                         "formats": [
#                             "webp",
#                             "png"
#                         ],
#                         "width": 128,
#                         "height": 128,
#                         "src": "https://dj423fildxgac.cloudfront.net/99a1a75c-1947-4120-b766-f8597e9ab897?format=webp"
#                     },
#                     "avatar-big-dark": {
#                         "formats": [
#                             "webp",
#                             "png"
#                         ],
#                         "width": 672,
#                         "height": 672,
#                         "src": "https://dj423fildxgac.cloudfront.net/7f8b6da6-748b-4de4-b8c7-67977ddb42f2?format=webp"
#                     },
#                     "avatar-big-light": {
#                         "formats": [
#                             "webp",
#                             "png"
#                         ],
#                         "width": 672,
#                         "height": 672,
#                         "src": "https://dj423fildxgac.cloudfront.net/1f25d49f-de0a-4877-8ecf-e6ef3cb28148?format=webp"
#                     }
#                 }
#             }
#         ],
#         "website": null,
#         "patreon": null,
#         "twitter": "https://twitter.com/TechAltar/",
#         "instagram": "https://www.instagram.com/techaltar/",
#         "facebook": null,
#         "merch": "https://store.nebula.app/collections/techaltar",
#         "merch_collection": "techaltar",
#         "share_url": "https://nebula.tv/techaltar/",
#         "engagement": {
#             "following": false
#         },
#         "playlists": [
#             {
#                 "id": "video_playlist:6e4ff405-5b91-4f12-bf67-d36fd5d824fa",
#                 "type": "video_playlist",
#                 "slug": "technorama",
#                 "title": "Technorama"
#             },
#             {
#                 "id": "video_playlist:ac65e707-6099-4b6e-b182-2c12ab6342a1",
#                 "type": "video_playlist",
#                 "slug": "techaltarplus",
#                 "title": "Nebula Plus"
#             }
#         ],
#         "zype_id": "5c4fcc7f5819f11153000bee"
#     },
#     "episodes": {
#         "next": "https://content.api.nebula.app/video/channels/techaltar/?cursor=cD0yMDIyLTAyLTIzKzEzJTNBMjElM0E0MCUyQjAwJTNBMDA%3D",
#         "previous": null,
#         "results": [
#             {
#                 "id": "video_episode:491aa6bc-4699-4bba-99aa-f052810c74d2",
#                 "type": "video_episode",
#                 "slug": "techaltar-china-destroyed-its-tech-giants-heres-why",
#                 "title": "China destroyed its tech giants. Here's why.",
#                 "description": "The Chinese government cracked down on Jack Ma, Alibaba, Ant Financial, Tencent and pretty much every Chinese internet company you might have heard of, wiping out trillions of dollars in value. Here's why.\n\nThe Story Behind - ep. 91\n\nBonus video: https://nebula.tv/videos/techaltar-the-ugly-impact-of-chinas-crackdowns\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions & Sources ◄◄◄  \n\nChannel Music by Edemski: https://soundcloud.com/edemski\nOther music by Epidemic Sound: http://epidemicsound.com/creator",
#                 "short_description": "The Chinese government cracked down on Jack Ma, Alibaba, Ant Financial, Tencent and pretty much every Chinese internet company you might have heard of, wiping out trillions of dollars in value. Here's why.\n\nThe Story Behind - ep. 91",
#                 "duration": 853,
#                 "duration_to_complete": 836,
#                 "published_at": "2022-10-06T18:09:33Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/d59dad60-5cf5-402c-aa1e-b7cf02eba500"
#                     }
#                 },
#                 "attributes": [],
#                 "share_url": "https://nebula.tv/videos/techaltar-china-destroyed-its-tech-giants-heres-why/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-china-destroyed-its-tech-giants-heres-why",
#                     "updated_at": "2022-10-06T18:10:33Z",
#                     "progress": 706,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "633f12b0bf6eb400010fc704"
#             },
#             {
#                 "id": "video_episode:bc454ebc-74ac-46b4-8663-369ff34d895c",
#                 "type": "video_episode",
#                 "slug": "techaltar-the-ugly-impact-of-chinas-crackdowns",
#                 "title": "The ugly impact of China's crackdowns",
#                 "description": "This is a bonus video accompanying this episode:\n\nChina destroyed its tech giants. Here's why. - https://nebula.tv/videos/techaltar-china-destroyed-its-tech-giants-heres-why\n\nHere I discuss whether the crackdowns on the tech giants actually worked, and what its positive, and sometimes unintended consequences seem to be.\n\nHigh five for supporting us on Nebula!",
#                 "short_description": "This is a bonus video accompanying \"China destroyed its tech giants. Here's why.\"\n\nHere I discuss whether the crackdowns on the tech giants actually worked, and what its positive, and sometimes unintended consequences seem to be.",
#                 "duration": 194,
#                 "duration_to_complete": 184,
#                 "published_at": "2022-10-06T17:06:53Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/36e51d34-3375-4628-b36f-a203135f68aa"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_plus"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-the-ugly-impact-of-chinas-crackdowns/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-the-ugly-impact-of-chinas-crackdowns",
#                     "updated_at": "2022-10-06T17:42:48Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "633f093619c8b6000172b992"
#             },
#             {
#                 "id": "video_episode:f65cf75a-5665-4a11-848e-f2c0cace2905",
#                 "type": "video_episode",
#                 "slug": "techaltar-ads-apples-next-billion-dollar-empire",
#                 "title": "Ads: Apple's next billion dollar empire",
#                 "description": "Apple announced their iOS privacy changes last year, stopping apps from tracking users across apps. At the same time, they also increased their ad revenue 10-fold and are planning to roll out ads to Maps, TV, Books, Podcasts & more to build out their own ad empire. \n\nThe Story Behind - ep. 90\n\nBonus video: https://nebula.app/videos/techaltar-why-google-facebook-secretly-love-the-ios-privacy-changes\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions & Sources ◄◄◄  \n\n1: Toni Sacconaghi, Bernstein, via Barrons: https://www.barrons.com/articles/apples-advertising-business-is-bigger-than-you-think-it-could-get-bigger-still-51628004419\n2: Mark Gurman, Bloomberg: https://www.bloomberg.com/news/newsletters/2022-08-14/apple-aapl-set-to-expand-advertising-bringing-ads-to-maps-tv-and-books-apps-l6tdqqmg\n3: Neil Shah, Counterpoint: https://www.counterpointresearch.com/advertising-walled-gardens/\n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "Apple announced their iOS privacy changes last year, stopping apps from tracking users across apps. At the same time, they also increased their ad revenue 10-fold and are planning to build out their own ad empire. \n\nThe Story Behind - ep. 90",
#                 "duration": 680,
#                 "duration_to_complete": 667,
#                 "published_at": "2022-09-02T15:46:01Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/395b0046-718b-49d9-833c-d97c19aa0034"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-ads-apples-next-billion-dollar-empire/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-ads-apples-next-billion-dollar-empire",
#                     "updated_at": "2022-09-02T15:46:52Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "63121fffc76bc90001f50bd9"
#             },
#             {
#                 "id": "video_episode:67bdfdad-3482-4eab-8e8e-9ffe2a29e90e",
#                 "type": "video_episode",
#                 "slug": "techaltar-why-google-facebook-secretly-love-the-ios-privacy-changes",
#                 "title": "Why Google & Facebook secretly love the iOS privacy changes",
#                 "description": "This is a bonus video accompanying the following video:\n\nAds: Apple's next billion dollar empire.",
#                 "short_description": "This is a bonus video accompanying the following video:\n\nAds: Apple's next billion dollar empire.",
#                 "duration": 159,
#                 "duration_to_complete": 149,
#                 "published_at": "2022-09-02T14:59:47Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/5900599f-ac11-4455-a88f-a50adaf5ce78"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_plus",
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-why-google-facebook-secretly-love-the-ios-privacy-changes/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-why-google-facebook-secretly-love-the-ios-privacy-changes",
#                     "updated_at": "2022-09-02T14:59:52Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "631218f7c850230001df63a1"
#             },
#             {
#                 "id": "video_episode:0dcf1764-69dd-4e79-90a5-df344e87d1b5",
#                 "type": "video_episode",
#                 "slug": "techaltar-how-circular-space-stations-conquered-sci-fi",
#                 "title": "How “Circular” Space Stations Conquered Sci-Fi",
#                 "description": "Discuss this episode on [Reddit.](https://www.reddit.com/r/watchnebula/comments/wrjq7j/technorama_how_circular_space_stations_conquered/)\r\n\r\nThe rotating wheel space station is a staple of science fiction. From 2001: A Space Odyssey to Solaris, Elysium and Interstellar, it has dominated how we imagine life in space. In this episode we explore its history in the real world and in cinema, as well as what it means for storytelling.\r\n\r\nTechnorama Season 2 - Episode 3\r\n\r\nWatch other Technorama episodes: https://nebula.app/technorama\r\n\r\nSelect video clips courtesy of Getty Images and AP Archive.\r\n\r\nMovies mentioned:\r\nSolaris (1972)\r\n2001: A Space Odyssey (1968)\r\n2001: A Space Odyssey | a Look behind the Future (1966)\r\nStar Trek: Deep Space Nine (1993-1995)\r\nElysium (2013)\r\nMission to Mars (2000)\r\nFoundation (2021)\r\nDoctor Who - The Long Game (2005)\r\nConquest of Space (1955)\r\nDisneyland - Man in Space (1955)\r\nDisneyland - Man and the Moon (1955)\r\nDisneyland - Mars and Beyond (1955)\r\nThe Cloverfield Paradox (2018)\r\nThe Green Slime (1968)\r\nStar Wars: Episode I - The Phantom Menace (1999)\r\nThunderbirds (2004)\r\nStar Trek Beyond (2016)\r\nThe Wandering Earth (2019)\r\nStar Trek: The Motion Picture (1979)\r\nStar Trek II: The Wrath of Khan (1982)\r\nEnemy Mine (1985)\r\nStar Trek IV: The Voyage Home (1986)\r\nArena (1989)\r\nZenon: Girl of the 21st Century (1999)\r\nRed Planet (2000)\r\nSolaris (2002)\r\nLockout (2012)\r\nEnder’s Game (2013)\r\nSpace Station 76 (2014)\r\nThe 100 (2014)\r\n\r\nSources & further Reading:\r\n1968 Science Fiction is Today’s Reality https://www.nasa.gov/mission_pages/station/main/2001_anniversary.htm\r\nAndrei Tarkovsky Calls Kubrick’s 2001: A Space Odyssey a ‘Phony’ Film ‘with Only Pretensions to Truth’ | Open Culture www.openculture.com/2015/07/andrei-tarkovsky-calls-kubricks-2001-a-space-odyssey-a-phony-film-with-only-pretensions-to-truth.html.\r\nBlast from the past: hopeful retrofuturism in science fiction film. https://www.researchgate.net/publication/336123527_Blast_from_the_past_hopeful_retrofuturism_in_science_fiction_film\r\nDefining Science Fiction. www.sfcenter.ku.edu, www.sfcenter.ku.edu/SF-Defined.htm.\r\nDeveloping New Habitats for Life Science Experiments on the International Space Station. https://www.ou.edu/journals/dis/DIS85/Reports/Bhattacharya.pdf\r\nKubrick: And beyond the Cinema Frame. www.collativelearning.com/2001 chapter 9.html.\r\nModular Extended-Stay HyperGravity Facility Design Concept: An Artificial-Gravity Space-Settlement Ground Analogue https://www.researchgate.net/publication/292137374_Modular_Extended-Stay_HyperGravity_Facility_Design_Concept_An_Artificial-Gravity_Space-Settlement_Ground_Analogue\r\nNotes on Cinema. “Andrei Tarkovsky: Dialogue on Science Fiction.” Notes on Cinema diaryofascreenwriter.blogspot.com/2018/10/andrei-tarkovsky-dialogue-on-science.html.\r\nReal Engineering - Can We Create Artificial Gravity? https://youtu.be/im-JM0f_J7s\r\nSolaris (1972) Mosfilm https://youtu.be/Z8ZhQPaw4rE\r\nSolaris: Inner Space. The Criterion Collection www.criterion.com/current/posts/239-solaris-inner-space\r\nStrange Forgotten Space Station Concepts That Never Flew https://www.wired.com/2012/01/space-station-concepts/\r\nThe Mars Society - 23rd Annual International Mars Society Convention Interview with NASA Administrator Jim Bridenstine\r\nThe Space Race www.history.com/topics/cold-war/space-race.\r\nWernher von Braun Space Station Design ****https://www.researchgate.net/figure/Wernher-von-Braun-Space-Station-Design-Bonestell-in-von-Braun-1952_fig1_292137374\r\nYes, the ‘Von Braun’ Space Hotel Idea Is Wild. But Could We Build It by 2025? ****https://www.space.com/gateway-foundation-von-braun-space-station.html",
#                 "short_description": "The rotating wheel space station is a staple of science fiction. From 2001: A Space Odyssey to Solaris, Elysium and Interstellar, it has dominated how we imagine life in space.",
#                 "duration": 951,
#                 "duration_to_complete": 932,
#                 "published_at": "2022-08-18T13:30:00Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar",
#                     "technorama"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "originals",
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/e778a404-660c-42c3-9fef-ff8dcef65392"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_original"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-how-circular-space-stations-conquered-sci-fi/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-how-circular-space-stations-conquered-sci-fi",
#                     "updated_at": "2022-08-18T13:40:45Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62fcfcff4acc6f00017317d6"
#             },
#             {
#                 "id": "video_episode:580139b5-24d5-4eef-9efd-f398998a1a0c",
#                 "type": "video_episode",
#                 "slug": "techaltar-the-insane-cost-of-cars",
#                 "title": "The Insane Cost of Cars",
#                 "description": "People underestimate how much owning a car costs by 52%. Even a cheap car costs a fortune to its owner, and yet another fortune to society. Let's compare it to some alternatives to show the insane real cost of cars.\n\nThe Story Behind - ep. 89\n\nCowboy e-bike (affiliate link): https://www.tkqlhce.com/click-100602223-15188758\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Mentioned videos & sources ◄◄◄  \n\nSources & calculations https://1drv.ms/x/s!AnEbV6tNc655iOxRCEGuJwAYd6SCEw?e=rQilM0\n\nNot Just Bikes - Swiss trains https://www.youtube.com/watch?v=muPcHs-E4qc\nMetamodernism - Hostile Transit https://www.youtube.com/watch?v=1vrQHMhZ3k4\nNot Just Bike - Paris https://www.youtube.com/watch?v=sI-1YNAmWlk\nPropel - Emeryville https://www.youtube.com/watch?v=FlVWv9O0qQ4\nRM Transit - Toronto https://www.youtube.com/watch?v=ufgQdU5DUI8\nNot Just Bikes - Finland, Oulu: https://youtu.be/Uhx-26GfCBU\n\nDensity maps: https://twitter.com/undertheraedar\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "People underestimate how much owning a car costs by 52%. Even a cheap car costs a fortune to its owner, and yet another fortune to society. Let's compare it to some alternatives to show the insane real cost of cars.\n\nThe Story Behind - ep. 89",
#                 "duration": 1197,
#                 "duration_to_complete": 1174,
#                 "published_at": "2022-08-01T23:28:18Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/ed2c00fd-b01f-42f8-b0e7-bf54d07f2f3b"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-the-insane-cost-of-cars/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-the-insane-cost-of-cars",
#                     "updated_at": "2022-08-01T23:28:38Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62e8571201e52a00011491b3"
#             },
#             {
#                 "id": "video_episode:43800e5e-e8bf-4c3c-adec-4a8b32dd2362",
#                 "type": "video_episode",
#                 "slug": "techaltar-why-brands-are-abandoning-their-colors",
#                 "title": "Why brands are abandoning their colors",
#                 "description": "Brands like Apple, Samsung, OPPO, Vivo, Huawei and Xiaomi are increasingly losing their colors and instead are starting to use black and white logos. Here's why.\n\nThe Story Behind - ep. 88\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "Brands like Apple, Samsung, OPPO, Vivo, Huawei and Xiaomi are increasingly losing their colors and instead are starting to use black and white logos. Here's why.\n\nThe Story Behind - ep. 88",
#                 "duration": 453,
#                 "duration_to_complete": 443,
#                 "published_at": "2022-07-18T20:19:29Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/805e18fa-3dc2-44c3-935e-4b9f22ef8429"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-why-brands-are-abandoning-their-colors/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-why-brands-are-abandoning-their-colors",
#                     "updated_at": "2022-07-18T20:20:08Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62d5bd3b96e5980001db30ec"
#             },
#             {
#                 "id": "video_episode:8cce1138-49ae-46a1-811b-26627ae98afc",
#                 "type": "video_episode",
#                 "slug": "techaltar-how-japan-avoided-technophobia",
#                 "title": "How Japan Avoided Technophobia",
#                 "description": "Discuss this episode on [Reddit.](https://www.reddit.com/r/watchnebula/comments/vnik5k/technorama_how_japan_avoided_technophobia/)\r\n\r\nUnlike in the rest of the world, science fiction in Japan managed to avoid depicting technology, and robots as a mostly negative element that is to be feared. Instead, robots are often the protagonists of their stories. Let's find out why!\r\n\r\nTechnorama Season 2 - Episode 2\r\n\r\nMovies mentioned:\r\nTetsujin 28: The Movie (2005)\r\nTetsujin 28-gou (2004)\r\nAstro Boy (1963)\r\nTetsujin 28 gou (1963)\r\nGiant Robo (1967)\r\nSuper Robot Red Baron (1973)\r\nMobile Suit Gundam (1979)\r\nMazinger Z (1972)\r\nBrave (1990-1998)\r\nBrave Exkaizer (1990)\r\nTale of Two Cities (Hiroshima-Nagasaki) (1949)\r\nMiracle in Asia (1963)\r\nMobile Suit Gundam: The Witch from Mercury (2022)\r\nNeon Genesis Evangelion (1995)\r\nThe End of Evangelion (1997)\r\nAkira (1988)\r\nTetsuo The Iron Man (1989)\r\nDeath Powder (1986)\r\n964 Pinocchio (1991)\r\nRubber's Lover (1996)\r\n\r\nSources & further reads:\r\n- Robot and ukiyo-e: implications to cultural varieties in human–robot relationships - Osamu Sakura 2021\r\n- Iron Man. The Cinema of Shinya Tsukamoto - Tom Mes 2005\r\n- Who is Afraid of the Humanoid? Investigating Cultural Differences in the Acceptance of Robots - Frederic Kaplan 2004\r\n- The Role of Thing-Making Cultures in Japan's Manufacturing Industry: Toward Social Robots and Super Smart Society in the Digitalization-Servitization Shift - Mateja Kovacic 2018\r\n- Comparing the Development and Commercialization of Care Robots in the European Union and Japan - James Wright 2020\r\n- Cognition and emotions in Japanese humanoid robotics - Yulia Frumer 2018\r\n- New Flesh Cinema: Japanese Cyberpunk-Body Horror and Cinema as Catharsis in the Age of Technology - Sarah Henry 2020\r\n- Why the pioneering Japanese anime ‘Akira’ is still relevant 30 years later - Hau Chu 2018 [https://www.washingtonpost.com/entertainment/why-the-pioneering-japanese-anime-akira-remains-relevant-30-years-later/2018/07/12/b7577c74-813f-11e8-b851-5319c08f7cee_story.html](https://www.washingtonpost.com/entertainment/why-the-pioneering-japanese-anime-akira-remains-relevant-30-years-later/2018/07/12/b7577c74-813f-11e8-b851-5319c08f7cee_story.html)\r\n- Post-Human Nightmares – The World of Japanese Cyberpunk Cinema - Mark Player 2011 [http://www.midnighteye.com/features/post-human-nightmares-the-world-of-japanese-cyberpunk-cinema/](http://www.midnighteye.com/features/post-human-nightmares-the-world-of-japanese-cyberpunk-cinema/)",
#                 "short_description": "Unlike in the rest of the world, science fiction in Japan managed to avoid depicting technology, and robots as a mostly negative element that is to be feared. Instead, robots are often the protagonists of their stories.",
#                 "duration": 1161,
#                 "duration_to_complete": 1138,
#                 "published_at": "2022-06-29T15:30:00Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar",
#                     "technorama"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "originals",
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/d4b58713-6e94-40bc-b54c-47da86befdfe"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_original"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-how-japan-avoided-technophobia/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-how-japan-avoided-technophobia",
#                     "updated_at": "2022-06-29T16:59:21Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62bc4f45adf4bf0001bf6fa0"
#             },
#             {
#                 "id": "video_episode:a6fd35e6-8fae-4547-bf8f-0eff0d916429",
#                 "type": "video_episode",
#                 "slug": "techaltar-how-to-build-a-phone-brand-out-of-nothing",
#                 "title": "How to Build a Phone Brand Out of Nothing",
#                 "description": "Carl Pei has now launched 3 different phone brands: OnePlus, OnePlus Nord and Nothing. In this video we break down how he builds hype, how he creates a myth, and how he makes products people can't help but care about.\n\nThe Story Behind - ep. 87\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "Carl Pei has now launched 3 different phone brands: OnePlus, OnePlus Nord and Nothing. In this video we break down how he builds hype, how he creates a myth, and how he makes products people can't help but care about.\n\nThe Story Behind - ep. 87",
#                 "duration": 662,
#                 "duration_to_complete": 649,
#                 "published_at": "2022-06-28T09:28:22Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/49f9ee2c-21c2-4cee-848a-6c0a5f6c5beb"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-how-to-build-a-phone-brand-out-of-nothing/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-how-to-build-a-phone-brand-out-of-nothing",
#                     "updated_at": "2022-06-28T09:29:22Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62bac401e6f2e50001f70824"
#             },
#             {
#                 "id": "video_episode:972cb4f6-db64-4dc1-b760-95a37fcd8089",
#                 "type": "video_episode",
#                 "slug": "techaltar-why-phone-batteries-arent-getting-better",
#                 "title": "Why phone batteries aren't getting better",
#                 "description": "Bonus video 1 (Fast charging): https://nebula.app/videos/techaltar-how-fast-charging-took-over\n\nBonus video 2 (Interview with Counterpoint): https://nebula.app/videos/techaltar-interview-with-peter-richardson-counterpoint-research\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► This video ◄◄◄  \n\nLithium-Ion batteries were commercialized in the 1990s by Sony, and since then, very little has changed in the battery market. Capacity increases are slow and incremental, and only fast charging is improving at quick rates. Let's take a look at why.\n\nThe Story Behind - ep. 86\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "Lithium-Ion batteries were commercialized in the 1990s by Sony, and since then, very little has changed in the battery market. Capacity increases are slow and incremental, and only fast charging is improving at quick rates. Let's take a look at why.",
#                 "duration": 930,
#                 "duration_to_complete": 912,
#                 "published_at": "2022-05-31T00:07:06Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/2eb2b7d4-9dc2-413d-852c-8ac4555eb87b"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-why-phone-batteries-arent-getting-better/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-why-phone-batteries-arent-getting-better",
#                     "updated_at": "2022-05-31T00:07:16Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62955489e3e4a60001160d1c"
#             },
#             {
#                 "id": "video_episode:65b52b8f-713f-468b-bf9a-1692a604b127",
#                 "type": "video_episode",
#                 "slug": "techaltar-how-fast-charging-took-over",
#                 "title": "How Fast Charging Took Over",
#                 "description": "This is a Bonus video that is accompanying my video about smartphone battery technologies.\r\n\r\nHere we explore how fast charging has evolved on phones, and where it is going next.\r\n\r\nInterview with Peter Richardson from Counterpoint Research here: https://nebula.app/videos/techaltar-interview-with-peter-richardson-counterpoint-research",
#                 "short_description": "This is a Bonus video that is accompanying my video about smartphone battery technologies.\r\n\r\nHere we explore how fast charging has evolved on phones, and where it is going next.",
#                 "duration": 448,
#                 "duration_to_complete": 438,
#                 "published_at": "2022-05-30T23:02:36Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/eb0e1de0-d9ed-413d-9003-32e985b9df3d"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_plus",
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-how-fast-charging-took-over/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-how-fast-charging-took-over",
#                     "updated_at": "2022-05-30T23:14:47Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "6295493bde4284000162c458"
#             },
#             {
#                 "id": "video_episode:062c6de3-df8d-41d0-83e2-7b0a98e8f2f6",
#                 "type": "video_episode",
#                 "slug": "techaltar-interview-with-peter-richardson-counterpoint-research",
#                 "title": "Interview with Peter Richardson, Counterpoint Research",
#                 "description": "This is a Bonus video that is accompanying my video about smartphone battery technologies.\n\nInterview with Peter Richardson, Counterpoint Research. We discussed battery and charging techonologies in smartphones.",
#                 "short_description": "This is a Bonus video that is accompanying my video about smartphone battery technologies.\n\nInterview with Peter Richardson, Counterpoint Research. We discussed battery and charging techonologies in smartphones.",
#                 "duration": 1942,
#                 "duration_to_complete": 1904,
#                 "published_at": "2022-05-30T22:35:00Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/4d19247e-d14c-41ec-b80f-4ccb2801718b"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_plus",
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-interview-with-peter-richardson-counterpoint-research/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-interview-with-peter-richardson-counterpoint-research",
#                     "updated_at": "2022-05-30T22:35:16Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "6295458317a0410001527e1d"
#             },
#             {
#                 "id": "video_episode:203f268d-d6c2-4e69-9fcb-306cc308c9f9",
#                 "type": "video_episode",
#                 "slug": "techaltar-i-have-to-make-some-big-changes",
#                 "title": "I have to make some big changes",
#                 "description": "I made my last channel update video 4 years ago. A lot has changed since. Welcome to TechAltar 3.0.\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Mentioned in the video ◄◄◄  \n\nKilian's channels:\nOrbit (English): https://www.youtube.com/channel/UCloDDgLMTwfIy80-TrqgRuA\niKnowReview (German): https://www.youtube.com/user/iKnowReview\n\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "I made my last channel update video 4 years ago. A lot has changed since. Welcome to TechAltar 3.0.",
#                 "duration": 547,
#                 "duration_to_complete": 537,
#                 "published_at": "2022-05-11T13:01:44Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/c6006228-ca75-49a1-bb9e-e38e2cf9f302"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-i-have-to-make-some-big-changes/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-i-have-to-make-some-big-changes",
#                     "updated_at": "2022-05-16T14:11:48Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "627bafa7de2990000184bb82"
#             },
#             {
#                 "id": "video_episode:cacfb315-b3b5-43f0-ae8c-77bd5e86bb4f",
#                 "type": "video_episode",
#                 "slug": "techaltar-how-russia-is-disconnecting-from-the-global-internet",
#                 "title": "How Russia Is Disconnecting From the Global Internet",
#                 "description": "Putin and his government have announced plans to disconnect Russia from the global internet and create an independent RuNet. Meanwhile international organizations like Cogent, Lumen, and LINX are increasingly isolating the country as well. Let's explore what all of this looks like in reality.\n\nThe Story Behind - ep. 85\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nTechnorama:\nhttps://nebula.app/technorama\n\nMerch:  \nhttp://enthusiast.store\n\nSocial media:  \nhttps://twitter.com/TechAltar \nhttps://instagram.com/TechAltar\nhttps://facebook.com/TechAltar   \nhttps://discord.gg/npKQebe \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "Putin and his government have announced plans to disconnect Russia from the global internet and create an independent RuNet. Meanwhile international organizations are increasingly isolating the country as well.\n\nThe Story Behind - ep. 85",
#                 "duration": 791,
#                 "duration_to_complete": 776,
#                 "published_at": "2022-04-27T14:10:31Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/8e49780e-21de-4f7f-9c3d-bcfb61757783"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-how-russia-is-disconnecting-from-the-global-internet/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-how-russia-is-disconnecting-from-the-global-internet",
#                     "updated_at": "2022-05-16T14:11:52Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "626948d22a7d34000193455c"
#             },
#             {
#                 "id": "video_episode:13f5b487-5757-44ae-adeb-9fe63c591362",
#                 "type": "video_episode",
#                 "slug": "techaltar-jetpacks-the-fututre-that-never-came",
#                 "title": "Jetpacks: The Future That Never Came",
#                 "description": "Discuss this episode on [Reddit.](https://www.reddit.com/r/watchnebula/comments/u8ocpf/technorama_jetpacks_the_future_that_never_came/)\r\n\r\nJet packs have captured our imagination for almost a century as *the* gadgets of the future. And yet, they never seem to become real. We explore our unyielding fascination with them.\r\n\r\nTechnorama Season 2 - Episode 1\r\n\r\nWatch other Technorama episodes: https://nebula.app/technorama\r\n\r\nMovies mentioned:\r\nIron Sky (2012)\r\nKind of The Rocket Men (1949)\r\nCommando Cody: Sky Marshal of the Universe (1953)\r\nThe Rocketeer (1991)\r\nLost in Space S3E24 (1968)\r\nArk II (1976)\r\nThunderball (1965)\r\nDie Another Day (2002)\r\nFahrenheit 451 (1966)\r\nLatitude Zero (1969)\r\nGillian's Island S3E27 (1967)\r\nThe Jetsons (1962)\r\nThe Lord of the Rings: The Fellowship of the Ring (2001)\r\nSky Captain and the World of Tomorrow (2004)\r\nKick-Ass (2010)\r\nRobocop 3 (1993)\r\nIron Angels 3 (1989)\r\nBuffy The Vampire Slayer S6E19 (2002)\r\nNCIS S7E11 (2010)\r\nTomorrowland (2015)\r\nMinority Report (2002)\r\nThe Mandalorian (2020)\r\nGuardians of the Galaxy Vol. 2 (2017)\r\nArrested Development S3E5 (2003)\r\nSleeper (1973)\r\nMan in Black 3 (2012)\r\nFor Y'ur Height Only (1981)\r\n\r\nFurther reading:\r\nhttps://publicdomainreview.org/collection/a-19th-century-vision-of-the-year-2000\r\nPierre Cardin's Space-Age Fashion Takes Us Back to the Future - Jason Farago The New York Times (2019)\r\nBlast from the past: hopeful retrofuturism in science fiction film - Joe P.L. Davidson University of Cambridge (2019)\r\nA stunning look at the profound impact of the jet plane on the mid-century aesthetic, from Disneyland to Life magazine - Vanessa R. Schwartz (2020)\r\nJetpack Dreams: One Man's Up and Down (But Mostly Down) Search for the Greatest Invention That Never Was - Mac Montandon (Oct 2008)",
#                 "short_description": "Jet packs have captured our imagination for almost a century as *the* gadgets of the future. And yet, they never seem to become real. We explore our unyielding fascination with them.\r\n\r\nTechnorama Season 2 - Episode 1",
#                 "duration": 1101,
#                 "duration_to_complete": 1079,
#                 "published_at": "2022-04-21T14:00:00Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar",
#                     "technorama"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "originals",
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/771a5935-6bde-4a69-a8b9-f27a14d1c085"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_original"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-jetpacks-the-fututre-that-never-came/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-jetpacks-the-fututre-that-never-came",
#                     "updated_at": "2022-05-16T14:11:54Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "6260655ee7138e00013f533d"
#             },
#             {
#                 "id": "video_episode:c582df56-e890-4065-a36f-f95eb3942096",
#                 "type": "video_episode",
#                 "slug": "techaltar-we-need-to-talk-about-electric-bikes-cowboy-4",
#                 "title": "We need to talk about electric bikes - Cowboy 4",
#                 "description": "I got my first electric bike for review - the Cowboy 4 ST. It gave me lots to think about the future of e-bikes, bikes and urban mobility in general.\n\n▶️  Nebula Plus video (The story of my bike theft): https://nebula.app/videos/techaltar-the-story-of-my-stolen-bike-chase\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Links from this video ◄◄◄  \n\nThese are affiliate links, I earn money from purchases:\n\n🚴  Cowboy bike: https://cowboy.com/\n📷  Insta360 camera (I used the One X2): https://store.insta360.com/springsale?insrc=INR1HE2\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "I got reviewed my first e-bike - the Cowboy 4 ST. It gave me lots to think about the future of e-bikes & urban mobility.\n\n▶️  Nebula Plus video (The story of my bike theft): https://nebula.app/videos/techaltar-the-story-of-my-stolen-bike-chase",
#                 "duration": 622,
#                 "duration_to_complete": 610,
#                 "published_at": "2022-04-15T08:41:44Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/6eaecfac-5cae-4dc2-a57e-400fbd1616e8"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-we-need-to-talk-about-electric-bikes-cowboy-4/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-we-need-to-talk-about-electric-bikes-cowboy-4",
#                     "updated_at": "2022-05-16T14:11:56Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62592958cd005c00016cbf06"
#             },
#             {
#                 "id": "video_episode:5a96d650-a81f-4b2e-a7db-98dde07d81f0",
#                 "type": "video_episode",
#                 "slug": "techaltar-the-story-of-my-stolen-bike-chase",
#                 "title": "The story of my stolen bike chase",
#                 "description": "The story of how my bike got stolen and how I tried to chase it down. \n\nThis is a companion video to my main Cowboy 4 review that will be uploaded shortly after this video.",
#                 "short_description": "The story of how my bike got stolen and how I tried to chase it down. \n\nThis is a companion video to my main Cowboy 4 review that will be uploaded shortly after this video.",
#                 "duration": 610,
#                 "duration_to_complete": 598,
#                 "published_at": "2022-04-14T13:10:49Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/c27ced89-0e40-44ea-aa4e-2568be3b013c"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_plus",
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-the-story-of-my-stolen-bike-chase/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-the-story-of-my-stolen-bike-chase",
#                     "updated_at": "2022-05-16T14:11:56Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "6258179de1dbeb000154a9d5"
#             },
#             {
#                 "id": "video_episode:98826ce4-0203-4066-b6cb-a46ce7ba3ccd",
#                 "type": "video_episode",
#                 "slug": "techaltar-sanctions-will-they-defeat-putin",
#                 "title": "Sanctions: Will they defeat Putin?",
#                 "description": "After Putin's attacks on Ukraine, the US White House, the EU and much of the rest of the world hit Russia with strong sanctions targeting their access to key technologies and the global financial system. From chip imports to SWIFT, the sanctions are hard and many companies also decided to pull out. Will they work?\n\nThe Story Behind - ep. 84\n\nBonus video (Nebula Plus): https://nebula.app/videos/techaltar-putins-cyberattacks-are-weak-for-now\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "After Putin's attacks, the US, the EU & others hit Russia with sanctions targeting their access to key technologies and the global financial system. From chip imports to SWIFT, the sanctions are hard and many companies also decided to pull out.",
#                 "duration": 959,
#                 "duration_to_complete": 940,
#                 "published_at": "2022-03-10T00:57:13Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/8c8f41cf-ad09-4f9c-9b44-4bdf3e3c4c46"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-sanctions-will-they-defeat-putin/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-sanctions-will-they-defeat-putin",
#                     "updated_at": "2022-05-16T14:12:09Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "622943f6d13cd10001dc1a70"
#             },
#             {
#                 "id": "video_episode:5e5dd403-78b1-4e45-bbff-279579f841ba",
#                 "type": "video_episode",
#                 "slug": "techaltar-putins-cyberattacks-are-weak-for-now",
#                 "title": "Putin's cyber-attacks are weak. For now.",
#                 "description": "As Putin launched his attack on Ukraine, many expected cyber attacks to clear the way first, devastating the country's internet infrastructure, communication networks & more. But that didn't happen. Yet.\n\nNebula Plus content.\n\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► TechAltar links ◄◄◄  \n\nMerch:  \nhttp://enthusiast.store   \n\nSocial media:  \nhttps://twitter.com/TechAltar  \nhttps://instagram.com/TechAltar \nhttps://facebook.com/TechAltar  \nhttps://discord.gg/npKQebe  \n\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \n\n►►► Attributions ◄◄◄  \n\nMusic by Edemski: https://soundcloud.com/edemski",
#                 "short_description": "As Putin launched his attack on Ukraine, many expected cyber attacks to clear the way first, devastating the country's internet infrastructure, communication networks & more. But that didn't happen. Yet.\n\nNebula Plus content.",
#                 "duration": 464,
#                 "duration_to_complete": 454,
#                 "published_at": "2022-03-08T17:16:19Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/4451268d-4261-41a6-912a-071aea125591"
#                     }
#                 },
#                 "attributes": [
#                     "is_nebula_plus",
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-putins-cyberattacks-are-weak-for-now/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-putins-cyberattacks-are-weak-for-now",
#                     "updated_at": "2022-05-16T14:12:10Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62278b631c64a300019054fa"
#             },
#             {
#                 "id": "video_episode:f65fdb53-72c9-41e2-a47b-0a44faed61ff",
#                 "type": "video_episode",
#                 "slug": "techaltar-which-tech-giant-does-the-biggest-acquisitions",
#                 "title": "Which tech giant does the biggest acquisitions?",
#                 "description": "Microsoft, Facebook, Apple, Google and Amazon - these companies seem to be buying up half the world. But which of the 5 big tech giants does the most acquisitions?\r\n\r\nCharter - ep. 1\r\n\r\n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \r\n\r\n►►► TechAltar links ◄◄◄  \r\n\r\nMerch:  \r\nhttp://enthusiast.store   \r\n\r\nSocial media:  \r\nhttps://twitter.com/TechAltar  \r\nhttps://instagram.com/TechAltar \r\nhttps://facebook.com/TechAltar  \r\nhttps://discord.gg/npKQebe  \r\n\r\nIf you want to support TechAltar directly:  https://flattr.com/@techaltar   \r\n\r\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  \r\n\r\n►►► Attributions ◄◄◄  \r\n\r\nMusic by Epidemic Sound: http://epidemicsound.com/creator\r\n\r\nData sources:\r\nhttps://www.cbinsights.com/research/tech-giants-billion-dollar-acquisitions-infographic/\r\nhttps://www.statista.com/chart/22986/largest-video-game-acquisitions/\r\n+ the respective financial statements of the 5 big tech giants.",
#                 "short_description": "Microsoft, Facebook, Apple, Google and Amazon - these companies seem to be buying up half the world. But which of the 5 big tech giants does the most acquisitions?\r\n\r\nCharter - ep. 1",
#                 "duration": 208,
#                 "duration_to_complete": 198,
#                 "published_at": "2022-02-23T13:21:40Z",
#                 "channel_id": "video_channel:702bb67a-c7c3-4b70-8ad3-f40ad79b8683",
#                 "channel_slug": "techaltar",
#                 "channel_slugs": [
#                     "techaltar"
#                 ],
#                 "channel_title": "TechAltar",
#                 "category_slugs": [
#                     "technology"
#                 ],
#                 "assets": {
#                     "channel_avatar": {
#                         "16": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=16",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=16"
#                         },
#                         "32": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=32",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=32"
#                         },
#                         "64": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=64",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=64"
#                         },
#                         "128": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=128",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=128"
#                         },
#                         "256": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=256",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=256"
#                         },
#                         "512": {
#                             "original": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.jpeg?width=512",
#                             "webp": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8.webp?width=512"
#                         }
#                     },
#                     "thumbnail": {
#                         "240": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.jpeg?height=240",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.webp?height=240"
#                         },
#                         "480": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.jpeg?height=480",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.webp?height=480"
#                         },
#                         "720": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.jpeg?height=720",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.webp?height=720"
#                         },
#                         "1080": {
#                             "original": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.jpeg?height=1080",
#                             "webp": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100.webp?height=1080"
#                         }
#                     }
#                 },
#                 "images": {
#                     "channel_avatar": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 288,
#                         "height": 288,
#                         "src": "https://dj423fildxgac.cloudfront.net/3357451c-4e49-4b58-8226-7b6757e22ba8"
#                     },
#                     "thumbnail": {
#                         "formats": [
#                             "jpeg",
#                             "png",
#                             "webp"
#                         ],
#                         "width": 1920,
#                         "height": 1080,
#                         "src": "https://dj423fildxgac.cloudfront.net/d6488bc8-2d70-4592-8714-d524d7594100"
#                     }
#                 },
#                 "attributes": [
#                     "free_sample_eligible"
#                 ],
#                 "share_url": "https://nebula.tv/videos/techaltar-which-tech-giant-does-the-biggest-acquisitions/",
#                 "channel": null,
#                 "engagement": {
#                     "content_slug": "techaltar-which-tech-giant-does-the-biggest-acquisitions",
#                     "updated_at": "2022-05-16T14:12:15Z",
#                     "progress": 0,
#                     "completed": false,
#                     "watch_later": false
#                 },
#                 "zype_id": "62163339de450d00019d781a"
#             }
#         ]
#     }
# }

NEBULA_API_CONTENT_VIDEO_CHANNELS_CURSOR = parse_obj_as(
    HttpUrl,
    "https://content.api.nebula.app/video/channels/{CHANNEL_SLUG}/?cursor={CURSOR}",
)


NEBULA_API_VIDEO_STREAM_INFORMATION = parse_obj_as(
    HttpUrl, "https://content.api.nebula.app/video/{VIDEO_SLUG}/stream/"
)
# {
#     "manifest": "https://content.api.nebula.app/video/techaltar-china-destroyed-its-tech-giants-heres-why/manifest/xzz5MySuOMOvxA3VFcooZm6kSTn4qJ3FaHgKSZ83bMc.m3u8",
#     "download": "https://content.api.nebula.app/video/techaltar-china-destroyed-its-tech-giants-heres-why/download/xzz5MySuOMOvxA3VFcooZm6kSTn4qJ3FaHgKSZ83bMc/",
#     "iframe": "https://content.api.nebula.app/video/techaltar-china-destroyed-its-tech-giants-heres-why/iframe/xzz5MySuOMOvxA3VFcooZm6kSTn4qJ3FaHgKSZ83bMc/",
#     "bif": {
#         "hd": "https://bif.watchnebula.com/efec556c-d5c4-4f54-86be-f86acb8958c3/hd.bif",
#         "sd": "https://bif.watchnebula.com/efec556c-d5c4-4f54-86be-f86acb8958c3/sd.bif",
#         "fhd": "https://bif.watchnebula.com/efec556c-d5c4-4f54-86be-f86acb8958c3/fhd.bif"
#     },
#     "subtitles": [
#         {
#             "language_code": "en",
#             "url": "https://standard-subtitles-production.s3.amazonaws.com/subtitles/final-633f12b0bf6eb400010fc704.20221009.014554.vtt",
#             "language": "English"
#         }
#     ]
# }


NEBULA_USERAPI_AUTHORIZATION = parse_obj_as(
    HttpUrl, "https://users.api.nebula.app/api/v1/authorization/"
)
# {
#     "token": "TOKEN"
# }

TOKEN_NEBULA_USERAPI_AUTHORIZATION: str = "TOKEN"

TOKEN_NEBULA_FINAL_AUTHORIZATION: Optional[str] = ""
