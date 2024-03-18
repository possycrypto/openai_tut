# from openai import OpenAI


# openai=OpenAI()

# prompt = "The human who falls into love with AI-Powered manekin"
# model="dall-e-3"


# def main() -> None:
#     #Generate image based on prompt
#     response = openai.images.generate(prompt=prompt, model=model)
    
#     #Prints response containing a URL link to image
#     print(response)

# if __name__ == "__main__":
#     main()

#!/usr/bin/env python

from openai import OpenAI

# gets OPENAI_API_KEY from your environment variables
openai = OpenAI()

prompt = "An astronaut lounging in a tropical resort in space, pixel art"
model = "dall-e-3"


def main() -> None:
    # Generate an image based on the prompt
    response = openai.images.generate(prompt=prompt, model=model)

    # Prints response containing a URL link to image
    print(response)


if __name__ == "__main__":
    main()


# RateLimitError: Error code: 429 - 
# {'error': 
#     {'code': 'rate_limit_exceeded', 
#      'message': 'Rate limit exceeded for images per minute in organization org-n9vhm5QAo7lYDhrPUvfDfGsU. Limit: 0/1min. Current: 1/1min. Please visit https://platform.openai.com/docs/guides/rate-limits to learn how to increase your rate limit.', 
#      'param': None, 'type': 'requests'}}