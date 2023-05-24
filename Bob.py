def response(hey_bob):
    remark =hey_bob
    remark = remark.strip()  # Remove leading and trailing whitespace

    if remark == "":
        return "Fine. Be that way!"
    elif remark.isupper():
        if remark.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif remark.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
