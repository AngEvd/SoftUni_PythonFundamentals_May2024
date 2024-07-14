title, content = input(), input()

comments = []

while True:
    user_input = input()

    if user_input == "end of comments":
        break

    comments.append(user_input)

print(f"""<h1>
    {title}
</h1>""")

print(f"""<article>
    {content}
</article>""")

for comment in comments:
    print(f"""<div>
    {comment}
</div>""")
